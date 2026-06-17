# -*- mode: python ; coding: utf-8 -*-
# PyInstaller-spec voor de Ontwerpchecker. Bouwt een zelfstandige executable
# (geen Python-installatie nodig om hem te draaien).
#
#   pyinstaller --noconfirm Ontwerpchecker.spec
#
# De meegeleverde mappen web/ en methodiek/ worden ingebakken; ontwerpchecker.app_dir()
# vindt ze terug via sys._MEIPASS wanneer de app 'frozen' draait.

from PyInstaller.utils.hooks import collect_all

datas = [("web", "web"), ("methodiek", "methodiek"), ("templates", "templates")]
binaries = []
hiddenimports = []

# PyMuPDF (PDF-motor) volledig meenemen; review praat via directe HTTP (geen SDK nodig)
for pkg in ("fitz", "openpyxl"):
    try:
        d, b, h = collect_all(pkg)
        datas += d; binaries += b; hiddenimports += h
    except Exception:
        pass

a = Analysis(
    ["webapp.py"],
    pathex=["."],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports + ["ontwerpchecker"],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz, a.scripts, a.binaries, a.datas, [],
    name="Ontwerpchecker",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,            # toont een venster met de server-URL/log; sluiten = stoppen
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
