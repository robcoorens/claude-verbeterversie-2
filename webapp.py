#!/usr/bin/env python3
"""
webapp.py - lokaal bedieningspaneel voor de ontwerpchecker.

Start een kleine webserver op je eigen machine; je bedient triage / voorbereiden /
reviewen via de browser. Het rekenwerk draait in-process (geen losse Python-
processen), zodat dit ook werkt als gebundelde .exe.

Starten (vanaf broncode):   pip install flask PyMuPDF anthropic
                            python webapp.py
Als .exe:                   dubbelklik Ontwerpchecker.exe
"""
from __future__ import annotations
import argparse, json, os, queue, sys, tempfile, threading, webbrowser, zipfile
from pathlib import Path

try:
    from flask import Flask, request, Response, send_file, abort, jsonify
except ImportError:
    sys.exit("Flask ontbreekt. Installeer met:  pip install flask")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ontwerpchecker as oc  # noqa: E402

WEB = Path(oc.app_dir()) / "web"
SAFE_EXT = {".md", ".txt", ".json", ".jpg", ".jpeg", ".png", ".pdf"}

app = Flask(__name__, static_folder=None)


# ---------------------------------------------------------------- helpers
def cfg_from(d):
    cfg = dict(oc.DEFAULTS)
    for ui, key in (("maxFileMb", "max_file_mb"), ("maxPagesPerPdf", "max_pages_per_pdf"),
                    ("rasterDpi", "raster_dpi"), ("maxRasterPages", "max_raster_pages"),
                    ("maxImages", "max_images"),
                    ("maxUploadFiles", "max_upload_files"), ("contextTokens", "context_tokens")):
        v = d.get(ui)
        if v not in (None, "", "null"):
            cfg[key] = type(oc.DEFAULTS[key])(v)
    return cfg


def stream_job(target):
    """Draai target(emit) in een thread; yield NDJSON-regels met log/result/error."""
    q: queue.Queue = queue.Queue()

    def emit(msg):
        q.put(("log", str(msg)))

    def run():
        try:
            res = target(emit)
            q.put(("result", res))
        except SystemExit as e:
            q.put(("error", str(e)))
        except Exception as e:
            q.put(("error", f"{type(e).__name__}: {e}"))
        finally:
            q.put(("__end__", None))

    threading.Thread(target=run, daemon=True).start()
    while True:
        kind, payload = q.get()
        if kind == "__end__":
            break
        if kind == "log":
            yield json.dumps({"log": payload}) + "\n"
        elif kind == "error":
            yield json.dumps({"error": payload}) + "\n"
        elif kind == "result":
            yield ("RESULT", payload)  # afgehandeld door de route


def classify(rel):
    p = rel.replace("\\", "/")
    table = {"00_TRIAGE.md": "triage", "MANIFEST.md": "manifest",
             "SCANS.md": "scans-md", "Reviewrapport.md": "report"}
    if p in table:
        return table[p]
    for pre, kind in (("corpus/", "corpus"), ("outline/", "outline"),
                      ("scans/", "scan-image"), ("split/", "split"), ("upload/", "upload")):
        if p.startswith(pre):
            return kind
    return "other"


def package_summary(out_dir):
    base = Path(out_dir)
    files = [{"rel": str(f.relative_to(base)), "size": f.stat().st_size,
              "kind": classify(str(f.relative_to(base)))}
             for f in sorted(base.rglob("*")) if f.is_file()]

    def read(n):
        p = base / n
        return p.read_text(encoding="utf-8", errors="replace") if p.exists() else None

    return {"root": str(base), "files": files,
            "triage_md": read("00_TRIAGE.md"), "scans_md": read("SCANS.md"),
            "manifest_md": read("MANIFEST.md"),
            "counts": {"corpus": sum(f["kind"] == "corpus" for f in files),
                       "scan_images": sum(f["kind"] == "scan-image" for f in files),
                       "splits": sum(f["kind"] == "split" for f in files)}}


# ---------------------------------------------------------------- routes
@app.get("/")
def index():
    return (WEB / "index.html").read_text(encoding="utf-8")


@app.get("/api/health")
def api_health():
    return jsonify(ok=True, service="ontwerpchecker", version=getattr(oc, "VERSION", "?"))


@app.post("/api/triage")
def api_triage():
    d = request.get_json(force=True)
    folder = d.get("folder", "").strip()
    if not folder or not os.path.isdir(folder):
        return jsonify(ok=False, error=f"Map niet gevonden: {folder or '(leeg)'}"), 400
    cfg = cfg_from(d)
    try:
        inv = oc.inventory(folder, cfg)
        strat = oc.decide_strategy(inv, cfg)
    except SystemExit as e:
        return jsonify(ok=False, error=str(e)), 400
    except Exception as e:
        return jsonify(ok=False, error=f"{type(e).__name__}: {e}"), 500
    pdfs = [{k: v for k, v in p.items() if k != "path"} for p in strat["per_pdf"]]
    return jsonify(ok=True, total_pages=inv["total_pages"], mode=inv["mode"],
                   approach=strat["approach"], est_tokens=strat["est_corpus_tokens"],
                   context_tokens=cfg["context_tokens"], pdfs=pdfs)


@app.post("/api/prepare")
def api_prepare():
    d = request.get_json(force=True)
    folder = d.get("folder", "").strip()
    out = d.get("out", "").strip() or str(Path(folder).parent / "review_pakket")
    if not os.path.isdir(folder):
        return jsonify(ok=False, error=f"Map niet gevonden: {folder}"), 400
    cfg = cfg_from(d)
    cfg["ai_label"] = (d.get("aiLabel") or "").strip() or "je AI-chat"
    cfg["ai_key"] = (d.get("ai") or "claude").strip()

    def gen():
        result = None
        for item in stream_job(lambda emit: oc.do_prepare(folder, out, cfg, emit=emit)):
            if isinstance(item, tuple) and item[0] == "RESULT":
                result = item[1] or {}
            else:
                yield item
        if result is not None:
            summ = package_summary(out)
            summ["bundle"] = result.get("bundle")
            yield json.dumps({"done": True, "summary": summ}) + "\n"

    return Response(gen(), mimetype="application/x-ndjson")


@app.get("/api/file")
def api_file():
    root = request.args.get("root", "")
    rel = request.args.get("rel", "")
    base = os.path.realpath(root)
    full = os.path.realpath(os.path.join(base, rel))
    if os.path.splitext(full)[1].lower() not in SAFE_EXT:
        abort(404)
    try:
        if os.path.commonpath([base, full]) != base:
            abort(404)
    except ValueError:
        abort(404)
    if not os.path.isfile(full):
        abort(404)
    return send_file(full, as_attachment=request.args.get("dl") == "1")


@app.get("/api/zip")
def api_zip():
    root = request.args.get("root", "")
    sub = request.args.get("sub", "upload")
    base = os.path.realpath(root)
    folder = os.path.realpath(os.path.join(base, sub))
    try:
        if os.path.commonpath([base, folder]) != base:
            abort(404)
    except ValueError:
        abort(404)
    if not os.path.isdir(folder):
        abort(404)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
    tmp.close()
    with zipfile.ZipFile(tmp.name, "w", zipfile.ZIP_DEFLATED) as z:
        for f in Path(folder).rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(folder))
    return send_file(tmp.name, as_attachment=True, download_name=f"{sub}_pakket.zip")


@app.post("/api/upload")
def api_upload():
    files = request.files.getlist("files")
    if not files:
        return jsonify(ok=False, error="Geen bestanden ontvangen."), 400
    d = tempfile.mkdtemp(prefix="oc_upload_")
    n = 0
    for f in files:
        name = os.path.basename(f.filename or "")
        if name.lower().endswith(".pdf"):
            f.save(os.path.join(d, name)); n += 1
    if n == 0:
        return jsonify(ok=False, error="Geen PDF's tussen de uploads."), 400
    return jsonify(ok=True, folder=d, count=n)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--no-browser", action="store_true")
    args = ap.parse_args()
    if not (WEB / "index.html").exists():
        sys.exit(f"web/index.html niet gevonden in {WEB}.")
    url = f"http://{args.host}:{args.port}"
    print(f"Ontwerpchecker-bedieningspaneel draait op  {url}")
    print("Sluit dit venster om te stoppen.")
    if not args.no_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    app.run(host=args.host, port=args.port, threaded=True, debug=False)


if __name__ == "__main__":
    main()
