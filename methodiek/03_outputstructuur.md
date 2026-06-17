# Outputstructuur (sectie J) en deliverables

Lever het rapport in onderstaande structuur. Bij grootschaligheidsmodus is het onderdeel **Dekking & methode** verplicht.

## In-chat / Word-rapportstructuur

1. **Managementsamenvatting & vrijgaveadvies** — conclusie (Voldoet / Voldoet onder voorwaarden / Voldoet niet / Onvoldoende aantoonbaar); belangrijkste risico's, tekortkomingen, verificatiegaten, ontbrekende documenten; blokkerende vs niet-blokkerende punten; acties vóór vrijgave; expliciete vermelding van de reviewdekking.
2. **Documentenregister** — per document/onderdeel: ID; titel; nummer; revisie; datum; status; veld; type; locatie (deel/pagina); rol (hoofdbron/ondersteunend/raakvlak/informatief); opmerking. Plus een aparte lijst "aangehaald maar niet aangeleverd".
3. **Bevindingentabel** — ID; prioriteit; discipline; type (fout/inconsistentie/ontbrekend bewijs/risico/raakvlak/status/redactioneel); document & locatie (blad/pagina); bevinding; onderbouwing; eis/uitgangspunt; risico/effect; aanbevolen actie; eigenaar; status. Toetsbaar formuleren met concrete verwijzing.
4. **Eisentraceability** — eisnummer/bron; omschrijving; bron/spec; resultaat ON; resultaat QA; bewijsdocument; **in set aanwezig? (ja/nee/Assai)**; onafhankelijke beoordeling; actie. Markeer eisen zonder bewijs, met te algemeen bewijs, met bewijs buiten de set, of afhankelijk van open punten.
5. **Raakvlakkenmatrix** — RV-ID; disciplines; onderwerp; afgesproken uitgangspunt; bewijsplaats; beoordeling; risico; actie; eigenaar. Markeer niet-afgestemde raakvlakken.
6. **Numerieke consistentiecheck** — grootheid; waarde/eenheid; bron 1; bron 2; consistent ja/nee/te verifiëren; toelichting; actie. Controleer o.a. spanningsniveaus, CT/VT-ratio's, kortsluitstromen, afschakeltijden, smeltpatroon/selectiviteit, kabel-/aderaantallen, vulgraad, componentratings, coderingen.
7. **Open punten & informatieverzoeken** — ID; verzoek; aanleiding; gekoppelde bevinding; prioriteit; impact op vrijgave; eigenaar. Concreet, bv. "Lever Kabelberekening 0114-…-00030 ter onderbouwing van selectiviteit".
8. **Signaal-/IO-sluitcontrole** (secundair-specifiek) — per veld: aantal signalen in IO-lijst; aantal in schema; schemasignalen niet in IO-lijst; IO-lijstsignalen niet in schema (en of gedocumenteerd); oordeel.
9. **Dekking & methode** (VERPLICHT bij grootschaligheidsmodus) — per onderdeel/hoofdstuk/veld: methode (tekstlaag volledig / visueel gesteekproefd / niet beoordeeld), dekking, toelichting. Vermeld hoeveel bladen visueel zijn bekeken t.o.v. het totaal en wat niet visueel is beoordeeld. Sluit af met de beoordelingsregel: geen "Voldoet" zonder herleidbaar bewijs; ontbrekend/extern bewijs = onvoldoende aantoonbaar; dit register vervangt geen integrale verificatie door het verantwoordelijke engineeringteam.

Eindig met een duidelijk **vrijgaveadvies**, onderbouwd en met dekkingsvermelding.

## Excel-bevindingenregister (aanbevolen voor grote sets)

Gebruik de `xlsx`-skill. Eén tabblad per onderdeel hierboven, met deze vaste set (pas aan op de set):

1. `1. Samenvatting` — managementsamenvatting + vrijgaveadvies + telling bevindingen.
2. `2. Documentenregister` — + lijst "aangehaald maar niet aangeleverd".
3. `3. Bevindingen` — prioriteit-kolom kleuren (Kritiek rood / Hoog oranje / Middel geel / Laag groen).
4. `4. Eisentraceability` — met kolom "in set aanwezig?".
5. `5. Raakvlakken`.
6. `6. Open punten`.
7. `7. Numerieke consistentie`.
8. `8. IO-signaalcontrole` (secundair-specifiek).
9. `9. Dekking & methode` (verplicht).

Voor een **veldreview** een apart bestand met: `Samenvatting veld`, `Hoofdstukbeoordeling` (per stroomkringschema-hoofdstuk: visueel/catalogus + oordeel), `Bevindingen veld`, `IO-signaalcontrole`, `Positieve verificaties`.

### Opmaakrichtlijnen
- Lettertype Arial; donkere kop-balk per tabblad; headerrij met kleurvulling en tekstterugloop; randen; afwisselende rijkleur; bevroren headerrij; passende kolombreedtes.
- Geen formules nodig (register, geen model); houd het foutloos. Valideer met het recalc-script van de `xlsx`-skill.
- Bestandsnaam: `Bevindingenregister_<project>.xlsx` resp. `Veldreview_<veld>_<project>.xlsx`. Lever af met `present_files`.
