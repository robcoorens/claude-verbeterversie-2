# Secundair-specifieke checklist

Aandachtspunten per documenttype en per technisch thema in een secundair pakket. Gebruik dit tijdens stap 3 (visuele inspectie) en stap 4 (inhoudelijke toetsing). Toets alleen wat aantoonbaar is uit de stukken; markeer de rest als onvoldoende bewijs.

## Per documenttype

### Technische specificaties / notitiepagina (per veld)
- Oogst alle notities en hun revisie. Let op formuleringen die open punten verraden: "nog niet geschikt", "wordt in UO-fase aangepast/gecontroleerd", "nog te kiezen", "TenneT zoekt dit uit", geel gearceerd.
- Controleer of verwezen IO-lijsten, berekeningen en standaarden (S380 → projectspecifiek) aanwezig of aangehaald zijn.

### IO-lijst (signaallijst, vaak IEC104)
- Aanwezigheid per veld; IOCheck-/controlepagina aanwezig en zonder waarschuwingen?
- **Signaal-/IO-sluitcontrole** (kerncontrole van deze skill): vergelijk DI_/DO_/AI_-signalen in de IO-lijst met die in de stroomkringschema's van hetzelfde veld.
  - Schemasignaal niet in IO-lijst → mogelijk ongedekt signaal.
  - IO-lijstsignaal niet in schema → controleer of het gedocumenteerd verwijderd/toegevoegd is (notitie); zo niet → inconsistentie.
- Let op signalen die "door de IO-generator worden gegenereerd maar niet in de stroomkringschema's staan".

### Functieschema (logica)
- Vergrendelings-/ontgrendelingslogica (bediening scheiders/aarders): &/≥1-poorten, DI-signalen, VBS-bediening. Controleer of de logica aansluit op de uitschakelmatrix en de IO-lijst.

### Grondschema / uitschakelmatrix
- CT-kernverdeling: aantal kernen, ratio, klasse en burden per kern (meting bv. 0.2s FsX; beveiliging bv. 5PRxx, Rct<…; impedantie/afstand bv. TPZ/TPY). Past de klasse bij de toepassing van de kern?
- Uitschakelmatrix: welke beveiligingen sturen welke schakelaars (alle relevante zijden: hoofd/koppel/tertiair)? Tijdvertragingen (bv. "170 ms naar andere zijde") consistent met de tijdrelais op de beveiligingsbladen?
- Redundantie zichtbaar (twee onafhankelijke systemen)?

### Stroomkringschema (hoofdstukken)
Typische indeling per veld: C Voeding AC/DC · E/F Primaire apparatuur · G Transformator (regelschakelaar/tap) · K Verwarming buitenapparatuur · M Stuursignalen · N Stroom-/Spanningscircuits · P Beveiliging 1/Uitschakeling 1 · Q Beveiliging 2/Uitschakeling 2 · R Inschakeling · S Overdracht · T Beveiliging Algemeen · V Verlichting · W Signalering · X Overige Klemmen · Y Overzichtblad. Behandel elk hoofdstuk expliciet als "visueel beoordeeld" of "alleen catalogus".

### Kabellijst
- Per kabel: type/lengte, van-naar (kast/strook), aderbeheer (Bezet/Gereserveerd/Vrij). Sluiten de kabeltypes aan op de aderaantal-selectie uit de ontwerpnota? Zijn er reserveaders conform uitgangspunt?

### Klemmenstrook
- Klemtypen, draadbruggen, kruisverwijzingen, aderparen/-kleuren, beide-zijdige aansluitingen. Volledig uitgewerkt of nog "in UO te controleren"? Sluit aan op kabellijst en stroomkringschema.

### Kastenbouw
- Status per blad (Concept vs Definitief). Ingesloten "Concept"-kasten in een definitieve set → vrijgave-blokkerend voor kastenbouw (Hoog). Let op: het elektrische schema van een kast kan wél uitgewerkt zijn terwijl het kastenbouw-(opstellings)blad nog Concept is — benoem dat onderscheid.

### Bestellijst / Stuklijst
- Steekproef: komen door de ontwerpnota voorgeschreven wijzigingen (bv. ander relaistype, vergroot smeltpatroon) terug in bestel-/stuklijst?

## Per technisch thema

### Beveiliging — redundantie & segregatie
- Twee onafhankelijke systemen (bv. UV1/UV2 in gescheiden kasten, Diff.Bev. 1 en 2)? Gescheiden voedingen en trip-circuits?
- Trip-circuit supervision / nulspanningsbewaking aanwezig (NS-UV1/UV2/RB)?

### CT/VT-circuits
- CT-secundairs op één punt geaard per groep; kortsluitbruggen voor veilig kortsluiten; aderdoorsnede benoemd. VT-secundairs met zekeringen/beveiliging.

### In- en uitschakeling
- Inschakeling: aanwezigheid Nood-UIT in de keten; POW/synchroon-gestuurd schakelen waar vereist; commando-uitgangen herleidbaar naar IO-lijst.
- Uitschakeling: redundante uitschakelspanningen; trip-paden naar alle relevante schakelaars.

### Overdracht / raakvlak naburig station
- Concrete kast- en documentreferenties naar het andere station aanwezig? Verwerking aan de andere zijde is doorgaans niet aantoonbaar uit deze set → markeer als raakvlak.
- Spanningslabel-consistentie: dezelfde zijde overal gelijk aangeduid (geen achtergebleven labels van een ander spanningsniveau)?

### DC/AC-hulpvoorziening
- DC: selectiviteit en smeltpatroon onderbouwd? Hangt de selectiviteit af van een nog niet gekozen accu/kortsluitstroom? → afhankelijkheid markeren.
- AC: aardlekbeveiliging (RCD, bv. 30 mA) op verlichting/WCD; hoofdschakelaar-/groepsindeling.

### Spanningsniveaus
- Identificeer hoofd-, koppel- en tertiaire/spoelspanning en hun rol. Meerdere niveaus (bv. 380/150/50 kV) zijn vaak legitiem (hoofdnet, koppeling met naburig station, tertiair t.b.v. spoelvelden) — verifieer de consistentie van de labeling, niet de "juistheid" met externe kennis.

### Typicals & standaarden
- Welke typicals (TYP.xxx) en standaarden (bv. een stationsstandaard → projectspecifiek) vormen de eisbasis? Zijn standaard-gebaseerde onderdelen al projectspecifiek gemaakt waar de notities dat eisen?
