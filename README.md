# Ontwerpchecker Secundair — tool

Voorbereiding van grote secundaire ontwerppakketten voor hoogspanningsstations, zodat
je ze daarna in Claude, ChatGPT of Copilot kunt laten beoordelen. De tool:

1. **kijkt eerst hoe de set het best te beoordelen is** (triage t.o.v. de upload- en
   contextlimieten),
2. **maakt de set hanteerbaar** — tekst eruit, outline-register, sleutelpagina's
   rasteren, en waar nodig PDF's splitsen — en bundelt alles tot een **upload-pakket
   van maximaal 20 bestanden** dat je in je eigen chat uploadt.

De PDF-motor draait op **PyMuPDF** (pure pip-bibliotheek, geen externe programma's),
dus de tool is tot één zelfstandige `.exe` te bundelen.

## Mapinhoud

```
ontwerpchecker-tool/
├── ontwerpchecker.py        ← de motor (command line + functies)
├── webapp.py                ← lokaal bedieningspaneel in de browser
├── web/index.html           ← het bedieningspaneel
├── methodiek/               ← de beoordelingsmethodiek (komt mee in het upload-pakket)
├── templates/               ← Excel-sjabloon dat de AI invult (komt mee in het pakket)
├── Ontwerpchecker.spec      ← bouwrecept voor de .exe (PyInstaller)
├── build.bat                ← bouw de .exe op Windows (dubbelklik)
├── .github/workflows/       ← bouw de .exe in de cloud (zonder lokale Python)
└── README.md
```

## De .exe maken (geen Python nodig om te draaien)

De resulterende `.exe` heeft geen Python nodig. Voor het éénmalig **bouwen** zijn er
twee routes.

### Route A — bouwen op je eigen Windows-machine
Vereist eenmalig Python. Plaats de map op een Windows-pc en **dubbelklik `build.bat`**.
Na afloop staat de executable in `dist\Ontwerpchecker.exe`. Dubbelklik die voortaan;
je browser opent vanzelf op `http://127.0.0.1:8765`. Sluit het zwarte venster om te
stoppen.

### Route B — bouwen in de cloud (zónder lokale Python)
1. Maak een (gratis) GitHub-account en een nieuw, leeg repository.
2. Upload de inhoud van deze map naar dat repository (zorg dat `.github/` meegaat).
3. Open het tabblad **Actions**, kies **Bouw Windows-exe**, klik **Run workflow**.
4. Download na een paar minuten het **Artifact** `Ontwerpchecker-exe` en pak het uit.

## Draaien vanaf de broncode (zonder .exe)

```bash
pip install flask PyMuPDF openpyxl
python webapp.py            # opent http://127.0.0.1:8765
```

Of via de command line:

```bash
python ontwerpchecker.py triage  --in ./pdfs
python ontwerpchecker.py prepare --in ./pdfs --out ./review_pakket
python ontwerpchecker.py bundle  --pakket ./review_pakket --max-upload-files 20
```

## Bedienen (browser)

Drie stappen, één voor één: **Triage → Voorbereiden → Naar je AI**. Kies bovenaan eerst
met welke **AI** je gaat reviewen (Claude, ChatGPT of Copilot); daarmee worden de
drempels in stap 1 en het maximum aantal upload-bestanden in stap 2 ingevuld als
voorstel — die blijven aanpasbaar. Vul daarna het pad naar je PDF-map in (of sleep PDF's
erin), klik Triage, en het paneel toont per bestand of het direct upload-baar is plus
een aanbevolen aanpak. Daarna bouw je het pakket — met live voortgang, een galerij van
de gerasterde sleutelpagina's, en het **upload-pakket** als zip.

In stap 3 staat een knop **Open [AI]** die je gekozen chat in een nieuw tabblad opent,
samen met de zip-download en de **opdracht** die je in de chat plakt (identiek aan
`01_LEESMIJ.md` in het pakket). De opdracht is per AI specifiek gemaakt — zelfde
kwaliteit en zelfde Excel-output in alle drie, alleen de manier van afleveren verschilt
per platform. Hij eist een review over de **volledige breedte** van het pakket (alle
velden/delen, geen steekproef) en levert het resultaat als **Excel-bestand**: elke AI
vult het meegeleverde sjabloon `Bevindingen_template.xlsx` in (tabbladen Samenvatting,
Bevindingen, Open punten, Verwijzingen buiten set, Signalen, Dekking) en geeft het als
`.xlsx` terug. Zo krijg je in Claude, ChatGPT én Copilot dezelfde gestructureerde uitkomst.

## Wat komt eruit (`review_pakket/`)

- `00_TRIAGE.md` — strategie + per-bestand-advies
- `MANIFEST.md` — wat upload je waar, met welke opdracht
- `corpus/deel_N.txt` — tekstlaag per PDF
- `outline/outline_deel_N.txt` — veld-/documenttype-register met paginanummers
- `scans/` — gerasterde sleutelpagina's (grondschema/uitschakelmatrix, beveiliging,
  CT/VT, functieschema, …) voor de visuele steekproef
- `SCANS.md` — geautomatiseerde tekstbevindingen (status, open punten, signalen)
- `upload/` — **kant-en-klaar voor je chat.** Alle tekst + outline samengevoegd tot
  `tekst_*.md`, alle sleutelpagina's in `03_sleutelpaginas.pdf`, `01_LEESMIJ.md` (de
  volledige per-AI opdracht + triage + methodiek), `02_SCANS.md`, en het Excel-sjabloon
  `Bevindingen_template.xlsx` dat de AI invult en als `.xlsx` teruggeeft. Upload deze map
  in één gesprek.

Claude.ai staat maximaal 20 bestanden per gesprek toe. De bundelstap respecteert dat
(instelbaar via "Max bestanden voor Claude-upload" of `--max-upload-files`): de tekst
wordt over zo min mogelijk bestanden verdeeld en de sleutelpagina's worden tot één PDF
samengevoegd. Past de tekst qua omvang niet in één gesprek, dan meldt de tool dat en
adviseert de delen veld-voor-veld in losse gesprekken te uploaden.

## Instelbare drempels

De AI-keuze bovenaan stap 1 vult de drempels in als voorstel: **Claude** (~30 MB,
100 pag./PDF, 20 bestanden, **max 20 afbeeldingen**, ~200k tokens), **ChatGPT** (≤25 MB,
ruimere PDF's, ~10 bestanden/afbeeldingen, ~128k tokens) en **Copilot** (PDF's tot ~50
pag., weinig bestanden/afbeeldingen, ~128k tokens). Het aantal gerasterde sleutelpagina's
wordt begrensd door "max afbeeldingen" (de sleutelpagina's tellen in de chat als
afbeeldingen — Claude staat er 20 per gesprek toe). **Deze getallen verschillen per plan
en veranderen** — pas ze aan in het paneel of via de CLI-vlaggen `--max-file-mb`,
`--max-pages-per-pdf`, `--max-images`, `--max-raster-pages`, `--max-upload-files`.

## Hoe sleutelpagina's en analyses worden bepaald

De visuele steekproef (`03_sleutelpaginas.pdf`) wordt gescoord gekozen: pagina's met
de belangrijkste tekeningtypes (grondschema, uitschakelmatrix, functieschema, …)
krijgen voorrang, grootformaat liggende pagina's (A1/A0 = vrijwel altijd schema's)
krijgen een bonus, en het eerste blad van elk veld/sectie wordt meegenomen. De
trefwoorden matchen op woordgrens (geen valse "ct"/"vt"-treffers), het rasterbudget
wordt eerlijk over alle PDF's verdeeld, en als een PDF geen bruikbare outline heeft
wordt de paginatekst doorzocht. Heeft een pagina geen tekstlaag, dan wordt er OCR op
toegepast als **Tesseract** beschikbaar is (anders gemeld).

`SCANS.md` bevat naast de standaardscans nu ook een heuristische **titelblok-extractie**
(tekeningnr/revisie/status/blad per pagina) en een **signaal-sluitcontrole** die
DI_/DO_/AI_-signalen met slechts één vindplaats markeert (mogelijk niet gesloten). Het
**Dekking**-tabblad van het Excel-sjabloon wordt vooraf gevuld met alle velden/delen,
zodat de AI alleen nog hoeft aan te vinken wat onderzocht is. Grote PDF's worden op
veld-/sectiegrenzen gesplitst in plaats van op vaste paginagetallen.

## Belangrijke kanttekeningen

- De beoordeling werkt op de **tekstlaag**; voor de tekeningen zelf gebruik je de
  gerasterde sleutelpagina's (`03_sleutelpaginas.pdf`) of een visuele check in de chat.
- Gescande PDF's zonder tekstlaag worden gemeld; draai die eerst door OCR.
- De kernregel blijft: geen oordeel "Voldoet" zonder herleidbaar bewijs, met eerlijke
  dekkingsverantwoording. De tool vervangt geen integrale verificatie door het team.
- **Licentie PyMuPDF:** valt onder AGPL (of een commerciële licentie). Voor intern
  gebruik doorgaans prima; bij distributie naar derden: controleer de voorwaarden.
