# Werkwijze A t/m K — Ontwerpchecker Secundair

Dit bestand bevat de volledige werkwijze. Lees per stap wat van toepassing is. De kernregels uit `SKILL.md` gelden onverkort: geen positief oordeel zonder herleidbaar bewijs, geen externe kennis, claim nooit meer dekking dan onderzocht.

## Inhoud
- A. Begrijp eerst het ontwerp
- B. Documentenregister (outline-gedreven)
- C. Inhoudelijke controle per document
- D. Tekeningen / schema's
- E. Berekeningen
- F. Eisconformiteit
- G. Raakvlakken
- H. Ontbrekende info, aannames, afwijkingen, verificatiegaten
- I. Classificatie van bevindingen
- J. Outputstructuur → zie `outputstructuur.md`
- K. Schrijfstijl en beoordelingsregels
- Bijlage: OCR-fallback en gereedschap

---

## A. Begrijp eerst het ontwerp

Bepaal en benoem: projectnaam en -nummer; locatie/station; discipline(s); ontwerpfase (VO/DO/UO); documentstatus; revisies; scope van het ontwerp; scope van de review; hoofdbronnen; ondersteunende documenten; ontbrekende-maar-noodzakelijke documenten; aangeleverde-maar-buiten-scope documenten.

Bij secundair specifiek: identificeer de velden (koppel-, lijn-, transformator-, spoelveld), de spanningsniveaus en hun rol (hoofd-/koppel-/tertiaire spanning), het beveiligingsconcept (redundantie), en de gehanteerde typicals (TYP.xxx) als eisbasis.

Bepaal de documentrangorde, bv.: (1) contract/projectspecifieke eisen; (2) vergunningen/bevoegd gezag; (3) klant-/assetmanagement-eisen (PVE/OIR); (4) generieke eisen/SPE; (5) Relatics/SEIS; (6) ontwerpbasis/uitgangspunten (ontwerpnota); (7) berekeningen; (8) tekeningen/schema's; (9) datasheets/leveranciersdocumentatie; (10) typicals; (11) normen. Leg vast wanneer de rangorde niet is opgegeven of conflicten niet oplosbaar zijn op basis van de stukken.

## B. Documentenregister (outline-gedreven)

Bouw het register bij voorkeur uit de PDF-outline (`scripts/secundair_scan.py` levert deze). Neem per document/onderdeel op: titel; nummer; revisie; datum; status; veld; documenttype; locatie (deel/pagina); rol in de verificatie (hoofdbron / ondersteunend bewijs / raakvlak / informatief); relatie met andere documenten; ontbrekende bijlagen of verwijzingen.

Signaleer direct: ontbrekende revisies; tegenstrijdige statussen (bv. ingesloten Concept-bladen in een definitieve set); onduidelijke hiërarchie; documenten zonder goedkeuring/datum/scope; verwijzingen naar niet-aangeleverde of verouderde documenten; documenten die niet passen bij de ontwerpfase.

Maak een aparte lijst **"aangehaald maar niet aangeleverd"** (zie scan-output): kerncalculaties, IO-lijsten, datasheets, indelings-/vormtekeningen, en cloud-/Relatics-/Assai-verwijzingen.

## C. Inhoudelijke controle per document

Per (type) document: doel, scope, belangrijkste inhoud en conclusies, gebruikte uitgangspunten, gebruikte normen/eisen, interne consistentie, traceerbaarheid naar eisen, en bruikbaarheid als bewijs. Voor de secundair-specifieke controles per documenttype: zie `secundair_checklist.md`.

## D. Tekeningen / schema's

Tekeningen visueel beoordelen (raster + `view`). Controleer titelblok (nummer, blad, revisie, datum, status, opsteller/controleur), maatvoering/labeling, kruisverwijzingen tussen bladen, en of de tekening klopt met de bijbehorende lijsten (IO-lijst, kabellijst, klemmenstrook, stuklijst). Bij grote sets risicogericht steekproeven, met expliciete dekkingsverantwoording (zie K en `outputstructuur.md`).

## E. Berekeningen

Per berekening: invoer herleidbaar? methode/norm benoemd? resultaat consistent met tekeningen/lijsten? randvoorwaarden expliciet? Voor secundair vaak: kabelberekening & selectiviteit, DC-capaciteit/accu, vulgraad kabelgoten, smeltpatroon-selectiviteit. Als de berekening wordt aangehaald maar niet is bijgevoegd: verificatiegat (zie H). Reken niets na op basis van externe kennis; toets uitsluitend interne herleidbaarheid en consistentie met de overige stukken.

## F. Eisconformiteit

Maak een eisentoets op basis van de aangeleverde eisenset/PVE/OIR/SPE/normen/typicals. Status per eis: **Voldoet / Voldoet niet / Onvoldoende bewijs / Niet van toepassing / Onzeker (nader te verifiëren)**. Geef nooit "Voldoet" als de onderbouwing niet expliciet in de aangeleverde stukken staat.

Vermeld per eis: eisnummer/bron; omschrijving; bewijsplaats (document/paragraaf/pagina/tabel/figuur/tekeningdetail); beoordeling; toelichting; actie. Markeer expliciet: eisen zonder bewijs; bewijs zonder eis; te algemene bewijsverwijzing; eisen afgedekt door verkeerde revisie; alleen administratief afgevinkte eisen; **eisen waarvan het bewijs buiten de aangeleverde set ligt (Relatics/Assai/cloud)** — die zijn niet onafhankelijk herleidbaar; eisen die afhangen van open punten of nog uit te voeren testen; conflicterende eisen. Let bij verificatierapporten op of de resultaatkolommen (ON/QA) daadwerkelijk gevuld zijn — controleer dit visueel, want tabelcellen extraheren vaak slecht als tekst.

## G. Raakvlakken

Controleer of het secundair ontwerp aansluit op andere disciplines en systemen:
- Secundair ↔ primair (aandrijfkasten, hulpcontacten, meettransformatoren, interlocking, kabelroutes, klemmenkasten, aarding/EMC, bedieningsconcept).
- Secundair ↔ tertiair (AC/DC-voedingen, UPS/batterijen, panelen, selectiviteit, monitoring; tertiaire/spoelvelden).
- Secundair ↔ bouwkundig/civiel (ruimtes, kabelgoten/-kelders, doorvoeren, ventilatie/koeling, brandveiligheid, sparingen, septic tank, veldhuisjes).
- Secundair ↔ naburige stations (signaal-/standmeldoverdracht; controleer concrete kast-/documentreferenties naar het andere station; verwerking aan de andere zijde is meestal niet aantoonbaar uit deze set → markeer).
- Secundair ↔ DC/gelijkrichters (selectiviteit, smeltpatroon, accu-kortsluitstroom).

Noteer per raakvlak: disciplines; documenten; overeengekomen uitgangspunt; bewijsplaats; ontbrekende informatie; risico; actie; eigenaar. Markeer raakvlakken die niet aantoonbaar zijn afgestemd.

## H. Ontbrekende info, aannames, afwijkingen, verificatiegaten

Identificeer ontbrekende documenten/bijlagen/berekeningen/datasheets/normartikelen/eisverificaties/raakvlakafspraken/revisies/goedkeuringen/uitgangspunten/testresultaten. Beoordeel aannames (expliciet? acceptabel? herleidbaar? nog geldig? afgestemd? impact op veiligheid/functie/eisen? vóór vrijgave te bevestigen?). Beoordeel afwijkingen (benoemd? goedgekeurd? impact beoordeeld? mitigatie? welke eisen geraakt? — het afwijkingenregister zit vaak in Relatics en niet in de set: markeer). Identificeer verificatiegaten: eisen zonder bewijs, ontwerpkeuzes zonder onderbouwing, berekeningen zonder herleidbare invoer of die ontbreken, raakvlakken zonder eigenaar, open punten met vrijgave-impact, bewijs dat buiten de set ligt.

## I. Classificatie van bevindingen

- **Kritiek** — veiligheidsrisico of normatieve non-conformiteit; niet aantoonbaar veilig/functioneel ontwerp (bv. selectiviteit/kortsluitvastheid niet aantoonbaar, essentiële berekening ontbreekt).
- **Hoog** — eis niet gehaald; ontwerpuitgangspunt ontbreekt; foutieve berekening met impact; ontbrekend raakvlak; revisieconflict met impact; vrijgave-blokkerende status (bv. Concept-kastenbouw).
- **Middel** — inconsistentie, onvolledige onderbouwing, raakvlakrisico of ontbrekende verificatie zonder directe veiligheidsimpact.
- **Laag** — redactioneel, verduidelijking, kleine inconsistentie zonder ontwerpimpact.

Maak bij elke bevinding onderscheid: bewezen fout; niet aantoonbaar; mogelijke inconsistentie; risico; aanbeveling; open vraag. Wees terughoudend met "Kritiek": gebruik die alleen bij aantoonbaar bewijs, niet bij een vermoeden dat voortkomt uit beperkte dekking — een dekkingsgat is een verificatiegat (Hoog), geen bewezen fout.

## K. Schrijfstijl en beoordelingsregels

Zakelijk, technisch, concreet. Verwijs steeds naar document/blad/paragraaf/pagina/tekeningnummer/revisie. Onderscheid bewezen fouten, risico's, ontbrekend bewijs, aannames, afwijkingen, verificatiegaten en redactionele punten. Geen speculatie. Herhaal in elke twijfel de kernregels: geen goedkeuring op waarschijnlijkheid, geen externe kennis, alleen aantoonbaar bewijs, en eerlijke dekking.

---

## Bijlage — OCR-fallback en gereedschap

**Tekstlaag ontbreekt (gescande set):** controleer met `pdffonts`. Geen fonts/tekst → OCR nodig. Gebruik `ocrmypdf` of `pytesseract` op gerasterde pagina's (zie de `pdf`- en `pdf-reading`-skills). Meld OCR-gebruik als beperking (herkenningsfouten mogelijk).

**Gereedschap:**
- `pdfinfo <pdf>` — paginatal, paginagrootte (groot formaat ≈ tekeningen).
- `pdffonts <pdf>` — tekstlaag aanwezig?
- `pdftotext -layout <pdf> out.txt` — tekstextractie; `\f` scheidt pagina's.
- `pdftoppm -jpeg -r 90..110 -f N -l N <pdf> prefix` — pagina N rasteren (A0/A1 leesbaar bij 90-110 dpi).
- `pypdf` → `reader.outline` en `reader.get_destination_page_number(item)` voor het bladwijzerregister.
- Waarschuwingen als "Illegal annotation destination" zijn cosmetisch; leesbaarheid blijft intact (eventueel als Laag/Info noteren).
