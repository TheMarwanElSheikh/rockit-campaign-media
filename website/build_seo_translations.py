"""Translated page SEO for www.rockit-transport.com (Wix Studio site 0e184a47-...).

Source: live English Item SEO Tags (read 2026-11-15). Output: seo_translations.json + .md.
Title = "<topic> | Rockit Transport Services & Logistics" (homepage mirrors English order).
Social title/description = same as SEO title/description.
"""
import json, re, sys
from pathlib import Path

B = "Rockit Transport Services & Logistics"
L = ["ar", "de", "es", "fr", "it"]

# page id, path, {lang: (topic, description)}
P = [
("c1dmp", "/", {
 "ar": ("وكيل شحن دولي في مصر", "وكيل شحن في القاهرة منذ 1992: شحن جوي وبحري وبري مع مخلّصين جمركيين مرخّصين تابعين لنا. روّاد شحن الملابس المعلّقة (GOH) والرورو في مصر."),
 "de": ("Spedition Ägypten", "Spedition in Kairo seit 1992: Luft-, See- und Landfracht mit eigenen lizenzierten Zollagenten. Pioniere für Hängeware (GOH) und RoRo in Ägypten."),
 "es": ("Transitario en Egipto", "Transitario en El Cairo desde 1992: carga aérea, marítima y terrestre con agentes de aduanas propios. Pioneros en prendas colgadas (GOH) y RORO en Egipto."),
 "fr": ("Transitaire en Égypte", "Transitaire au Caire depuis 1992 : fret aérien, maritime et routier, déclarants agréés maison. Pionniers du textile sur cintres (GOH) et du RORO en Égypte."),
 "it": ("Spedizioniere in Egitto", "Spedizioniere al Cairo dal 1992: trasporto aereo, marittimo e terrestre e doganalisti interni. Pionieri di capi appesi (GOH) e RORO in Egitto."),
}),
("d3w4l", "/about", {
 "ar": ("من نحن", "ننقل شحنات مصر منذ 1992. وكيل شحن معتمد من IATA وعضو في FIATA وEIFFA وحاصلون على ISO 9001، ولنا مكاتب في أهم خمسة مراكز موانئ ومطارات في مصر."),
 "de": ("Über uns", "Seit 1992 bewegen wir Ägyptens Fracht: IATA-Agent, FIATA- und EIFFA-Mitglied, ISO 9001, mit Büros an Ägyptens fünf wichtigsten Häfen und Flughäfen."),
 "es": ("Sobre nosotros", "Movemos la carga de Egipto desde 1992. Agente IATA, miembro de FIATA y EIFFA, ISO 9001, con oficinas en los cinco grandes puertos y aeropuertos del país."),
 "fr": ("À propos", "Nous transportons le fret égyptien depuis 1992. Agent IATA, membre FIATA et EIFFA, certifié ISO 9001, avec des bureaux sur les cinq grands hubs du pays."),
 "it": ("Chi siamo", "Muoviamo merci in Egitto dal 1992. Agente IATA, membro FIATA ed EIFFA, certificato ISO 9001, con uffici nei cinque principali porti e aeroporti egiziani."),
}),
("agqrf", "/awards", {
 "ar": ("الاعتمادات والجوائز", "وكيل شحن معتمد من IATA، وعضو في FIATA وEIFFA، وحاصلون على شهادة ISO 9001، مع جوائز خدمة من British Airways وLufthansa وSwiss WorldCargo."),
 "de": ("Zertifikate & Auszeichnungen", "IATA-Frachtagent, Mitglied von FIATA und EIFFA, ISO-9001-zertifiziert und ausgezeichnet von British Airways, Lufthansa und Swiss WorldCargo."),
 "es": ("Acreditaciones y premios", "Agente de carga IATA, miembro de FIATA y EIFFA, certificación ISO 9001 y premios de servicio de British Airways, Lufthansa y Swiss WorldCargo."),
 "fr": ("Accréditations et distinctions", "Agent de fret IATA, membre de la FIATA et de l'EIFFA, certifié ISO 9001, récompensé par British Airways, Lufthansa et Swiss WorldCargo."),
 "it": ("Accreditamenti e premi", "Agente cargo IATA, membro FIATA ed EIFFA, certificato ISO 9001, con premi di servizio da British Airways, Lufthansa e Swiss WorldCargo."),
}),
("fjeib", "/offices", {
 "ar": ("مكاتبنا في مصر", "المقر الرئيسي في مصر الجديدة بالقاهرة، مع فرق عمل في الإسكندرية والعين السخنة وبورسعيد ودمياط. تمر جميع الاستفسارات عبر المقر الرئيسي: +20 2 2690 7601"),
 "de": ("Standorte in Ägypten", "Zentrale in Heliopolis, Kairo, mit Teams in Alexandria, Ain Sokhna, Port Said und Damietta. Alle Anfragen laufen über die Zentrale: +20 2 2690 7601."),
 "es": ("Oficinas en Egipto", "Sede en Heliópolis, El Cairo, con equipos en Alejandría, Ain Sokhna, Port Said y Damietta. Todas las consultas pasan por la sede: +20 2 2690 7601."),
 "fr": ("Bureaux en Égypte", "Siège à Héliopolis, Le Caire, avec des équipes à Alexandrie, Ain Sokhna, Port-Saïd et Damiette. Toutes les demandes passent par le siège : +20 2 2690 7601."),
 "it": ("Uffici in Egitto", "Sede a Heliopolis, Il Cairo, con team ad Alessandria, Ain Sokhna, Port Said e Damietta. Ogni richiesta passa dalla sede centrale: +20 2 2690 7601."),
}),
("dfif6", "/air-freight", {
 "ar": ("الشحن الجوي في مصر", "شحن جوي من مصر وإليها عبر وكيل معتمد من IATA: عقود مع شركات الطيران، ورحلات مستأجرة، واستلام من أي مكان، وتخليص الواردات بمطار القاهرة في نحو يومين."),
 "de": ("Luftfracht Ägypten", "Luftfracht von und nach Ägypten vom IATA-Agenten: Airline-Verträge, Charter, landesweite Abholung, Importverzollung am Flughafen Kairo in ca. zwei Tagen."),
 "es": ("Carga aérea Egipto", "Carga aérea desde y hacia Egipto con un agente IATA: contratos con aerolíneas, chárteres, recogida nacional y despacho en El Cairo en unos dos días."),
 "fr": ("Fret aérien Égypte", "Fret aérien vers et depuis l'Égypte par un agent IATA : contrats aériens, affrètements, enlèvement national, dédouanement au Caire en deux jours environ."),
 "it": ("Trasporto aereo Egitto", "Trasporto aereo da e per l'Egitto con un agente IATA: contratti aerei, charter, ritiro in tutto il Paese e sdoganamento al Cairo in circa due giorni."),
}),
("f0jl0", "/ocean-freight", {
 "ar": ("الشحن البحري في مصر", "شحن FCL وLCL والرورو عبر الإسكندرية ودمياط وبورسعيد والعين السخنة، بما فيها الملابس المعلّقة والحاويات المبرّدة، مع التخليص في الميناء بمخلّصينا."),
 "de": ("Seefracht Ägypten", "FCL, LCL und RoRo über Alexandria, Damietta, Port Said und Ain Sokhna, inklusive Hängeware und Kühlcontainer, im Hafen verzollt durch eigene Zollagenten."),
 "es": ("Carga marítima Egipto", "FCL, LCL y RORO por Alejandría, Damietta, Port Said y Ain Sokhna, con prendas colgadas y refrigerados, despachados en puerto por nuestros propios agentes."),
 "fr": ("Fret maritime Égypte", "FCL, LCL et RORO via Alexandrie, Damiette, Port-Saïd et Ain Sokhna, textile sur cintres et reefer compris, dédouanés au port par nos propres déclarants."),
 "it": ("Trasporto marittimo Egitto", "FCL, LCL e RORO via Alessandria, Damietta, Port Said e Ain Sokhna, con capi appesi e reefer, sdoganati in porto dai nostri doganalisti."),
}),
("g9s2e", "/inland-freight", {
 "ar": ("النقل البري في مصر", "شاحناتنا ومقطوراتنا الخاصة تنقل شحنات FCL وLCL من الإسكندرية ودمياط وبورسعيد والسخنة إلى أي عنوان في مصر، مع جهة اتصال واحدة."),
 "de": ("Landtransport Ägypten", "Eigene Lkw und Trailer bringen FCL- und LCL-Fracht von Alexandria, Damietta, Port Said und Sokhna an jede Adresse in Ägypten, mit einem Ansprechpartner."),
 "es": ("Transporte terrestre Egipto", "Camiones y remolques propios llevan carga FCL y LCL desde Alejandría, Damietta, Port Said y Sokhna a cualquier punto de Egipto, con un solo contacto."),
 "fr": ("Transport routier Égypte", "Nos camions et remorques acheminent le fret FCL et LCL d'Alexandrie, Damiette, Port-Saïd et Sokhna partout en Égypte, avec un interlocuteur unique."),
 "it": ("Autotrasporto Egitto", "I nostri camion e rimorchi portano merci FCL e LCL da Alessandria, Damietta, Port Said e Sokhna a qualsiasi indirizzo in Egitto, con un unico referente."),
}),
("mjtrs", "/customs-clearance", {
 "ar": ("التخليص الجمركي في مصر", "مخلّصون جمركيون مرخّصون في موانئ مصر البحرية ومطار القاهرة: تسجيل ACID، والتقديم عبر منصة نافذة، والإفراج المسبق، وتخليص الشحن الجوي في نحو يومين."),
 "de": ("Zollabfertigung Ägypten", "Lizenzierte Zollagenten in Ägyptens Seehäfen und am Flughafen Kairo: ACID-Registrierung, Nafeza, Vorabverzollung, Luftfracht in ca. zwei Tagen frei."),
 "es": ("Despacho de aduanas Egipto", "Agentes de aduanas autorizados en los puertos de Egipto y el aeropuerto de El Cairo: ACID, Nafeza y predespacho; carga aérea despachada en dos días."),
 "fr": ("Dédouanement Égypte", "Déclarants agréés dans les ports égyptiens et à l'aéroport du Caire : ACID, déclaration Nafeza, pré-dédouanement, fret aérien libéré en deux jours environ."),
 "it": ("Sdoganamento Egitto", "Doganalisti autorizzati nei porti egiziani e all'aeroporto del Cairo: ACID, pratiche Nafeza e pre-sdoganamento; merce aerea libera in due giorni."),
}),
("q5dsw", "/project-logistics", {
 "ar": ("شحنات المشروعات في مصر", "تخطيط متكامل لشحنات المشروعات والشحنات خارج المقاس: مسح المسارات، وخطط التنفيذ، واستئجار السفن، والتوصيل متعدد الوسائط من موانئ مصر إلى موقعك."),
 "de": ("Projektfracht Ägypten", "Übermaß- und Projektfracht durchgängig geplant: Streckenprüfung, Method Statements, Charter und multimodale Zustellung ab Ägyptens Häfen bis zur Baustelle."),
 "es": ("Carga de proyectos Egipto", "Carga fuera de gálibo y de proyectos, de punta a punta: estudios de ruta, planes de método, fletamento y entrega multimodal desde Egipto hasta su obra."),
 "fr": ("Fret de projets Égypte", "Colis hors gabarit et fret de projets de bout en bout : études d'itinéraire, modes opératoires, affrètement et livraison multimodale jusqu'à votre site."),
 "it": ("Carichi di progetto Egitto", "Carichi fuori sagoma e di progetto, end-to-end: rilievi di percorso, method statement, noleggio e consegna multimodale dai porti egiziani al cantiere."),
}),
("vp246", "/supply-chain-warehousing", {
 "ar": ("سلاسل الإمداد والتخزين", "تخزين مرن في مصر مع خدمات التجميع وتغليف الصادرات والتوزيع، مرتبط بخدمات الشحن الجوي والبحري والبري لدينا. مجمّعو صادرات مرخّصون."),
 "de": ("Lieferkette & Lagerhaltung", "Flexible Lagerung in Ägypten mit Konsolidierung, Exportverpackung und Distribution, plus Luft-, See- und Landfracht. Lizenzierte Exportkonsolidierer."),
 "es": ("Cadena de suministro y almacén", "Almacenaje flexible en Egipto: consolidación, embalaje para exportar y distribución, junto a carga aérea, marítima y terrestre. Consolidadores autorizados."),
 "fr": ("Logistique et entreposage", "Entreposage flexible en Égypte : groupage, emballage export et distribution, liés à notre fret aérien, maritime et routier. Groupeurs export agréés."),
 "it": ("Supply chain e magazzinaggio", "Magazzini flessibili in Egitto: consolidamento, imballaggio export e distribuzione, con trasporto aereo, marittimo e terrestre. Consolidatori autorizzati."),
}),
("k5xxz", "/industries", {
 "ar": ("لوجستيات القطاعات في مصر", "شحن لقطاعات الأزياء والسيارات والأدوية والكيماويات والسلع سريعة التلف والمعارض والطاقة من مصر وإليها. روّاد شحن الملابس المعلّقة."),
 "de": ("Branchenlogistik Ägypten", "Fracht für Mode, Automobil, Pharma, Chemie, verderbliche Waren, Messen und Energie, von und nach Ägypten. Pioniere im Versand von Hängeware."),
 "es": ("Logística sectorial Egipto", "Carga para moda, automoción, farmacia, química, perecederos, ferias y energía, desde y hacia Egipto. Pioneros en el envío de prendas colgadas."),
 "fr": ("Logistique sectorielle Égypte", "Fret pour la mode, l'automobile, la pharma, la chimie, le périssable, les salons et l'énergie, vers et depuis l'Égypte. Pionniers du textile sur cintres."),
 "it": ("Logistica di settore Egitto", "Spedizioni per moda, automotive, farmaceutico, chimica, deperibili, fiere ed energia, da e per l'Egitto. Pionieri nel trasporto di capi appesi."),
}),
("yp9f9", "/projects", {
 "ar": ("سجل مشروعاتنا", "مختارات من الشحنات التي خطّطت لها Rockit ونفّذتها عبر الموانئ المصرية، من المعدات خارج المقاس والأطوال الكبيرة إلى عمليات النقل متعدد الوسائط المعقدة."),
 "de": ("Projektreferenzen", "Ausgewählte Sendungen, die Rockit über ägyptische Häfen geplant und geliefert hat: von Übermaß und Langgut bis zu komplexen multimodalen Transporten."),
 "es": ("Portafolio de proyectos", "Envíos seleccionados que Rockit ha planificado y entregado por puertos egipcios, de equipos fuera de gálibo y piezas largas a operaciones multimodales."),
 "fr": ("Nos réalisations", "Expéditions planifiées et livrées par Rockit via les ports égyptiens : colis hors gabarit, pièces longues et opérations multimodales complexes."),
 "it": ("Portfolio progetti", "Spedizioni selezionate pianificate e consegnate da Rockit nei porti egiziani: carichi fuori sagoma, pezzi lunghi e complessi trasporti multimodali."),
}),
("acvt4", "/insights", {
 "ar": ("أدلة الجمارك والشحن", "أدلة عملية من قسم الجمارك لدينا في القاهرة: نظام ACID ومنصة نافذة، وإجراءات الموانئ المصرية، وأزمنة العبور، والمستندات التي تُبقي شحناتك في حركة."),
 "de": ("Zoll- & Frachtratgeber", "Praxiswissen unseres Zollteams in Kairo: ACID und Nafeza, Abläufe in Ägyptens Häfen, Transitzeiten und die Dokumente, die Fracht in Bewegung halten."),
 "es": ("Guías de aduanas y fletes", "Guías prácticas de nuestro equipo de aduanas en El Cairo: ACID y Nafeza, trámites en puertos egipcios, tiempos de tránsito y los documentos clave."),
 "fr": ("Guides douane et fret", "Guides pratiques de notre service douane au Caire : ACID et Nafeza, procédures portuaires égyptiennes, délais de transit et documents essentiels."),
 "it": ("Guide doganali e trasporti", "Guide pratiche del nostro ufficio doganale al Cairo: ACID e Nafeza, procedure nei porti egiziani, tempi di transito e documenti per spedire senza intoppi."),
}),
("x9u7i", "/e-services", {
 "ar": ("أدوات شحن مجانية", "سبع أدوات شحن مجانية دون تسجيل دخول: تتبع الحاويات والسفن والرحلات، ومواعيد الإبحار، وخطط التحميل، والوزن المحتسب، والرسوم الجمركية المصرية."),
 "de": ("Kostenlose Frachttools", "Sieben kostenlose Frachttools ohne Anmeldung: Container-, Schiffs- und Flugtracking, Fahrpläne, Ladepläne, Frachtgewicht und ägyptische Zölle."),
 "es": ("Herramientas de flete gratis", "Siete herramientas gratuitas sin registro: rastreo de contenedores, buques y vuelos, itinerarios, planes de carga, peso tasable y aranceles egipcios."),
 "fr": ("Outils fret gratuits", "Sept outils fret gratuits sans inscription : suivi de conteneurs, navires et vols, horaires, plans de chargement, poids taxable et droits de douane."),
 "it": ("Strumenti cargo gratuiti", "Sette strumenti gratuiti, senza login: tracking di container, navi e voli, orari di partenza, piani di carico, peso tassabile e dazi doganali egiziani."),
}),
("fa5kh", "/container-tracking", {
 "ar": ("تتبع الحاويات", "تحقّق من أي رقم حاوية وفق معيار ISO 6346، واعرف خط الملاحة المالك لها، وافتح صفحة التتبع لدى الناقل بنقرة واحدة. مجانًا ودون تسجيل دخول."),
 "de": ("Container-Tracking", "Containernummer nach ISO 6346 prüfen, die Reederei erkennen und deren eigenes Tracking mit einem Klick öffnen. Kostenlos, ohne Anmeldung."),
 "es": ("Rastreo de contenedores", "Valide cualquier número de contenedor según ISO 6346, vea qué naviera lo posee y abra su seguimiento con un clic. Gratis y sin registro."),
 "fr": ("Suivi de conteneurs", "Vérifiez un numéro de conteneur selon ISO 6346, identifiez la compagnie maritime et ouvrez son suivi en un clic. Gratuit, sans inscription."),
 "it": ("Tracking container", "Verifica qualsiasi numero di container secondo ISO 6346, scopri la compagnia armatrice e apri il suo tracking con un clic. Gratis, senza login."),
}),
("t9gjx", "/vessel-tracking", {
 "ar": ("تتبع السفن مباشرةً", "الموقع المباشر عبر AIS والمسار الأخير ووجهة أي سفينة برقم IMO أو MMSI، على خريطة تتمركز حول قناة السويس والبحر الأحمر. مجانًا ودون تسجيل دخول."),
 "de": ("Live-Schiffsverfolgung", "Live-AIS-Position, letzte Route und Ziel jedes Schiffs per IMO- oder MMSI-Nummer, auf einer Karte rund um Suezkanal und Rotes Meer. Kostenlos."),
 "es": ("Seguimiento de buques en vivo", "Posición AIS en vivo, ruta reciente y destino de cualquier buque por número IMO o MMSI, en un mapa centrado en el canal de Suez y el mar Rojo. Gratis."),
 "fr": ("Suivi des navires en direct", "Position AIS en direct, trajet récent et destination de tout navire par n° IMO ou MMSI, sur une carte centrée sur Suez et la mer Rouge. Gratuit."),
 "it": ("Tracking navi in tempo reale", "Posizione AIS in tempo reale, rotta recente e destinazione di ogni nave per IMO o MMSI, su una mappa centrata su Canale di Suez e Mar Rosso. Gratis."),
}),
("lnvef", "/flight-tracking", {
 "ar": ("تتبع الرحلات وبوالص الشحن", "تحقّق من بوليصة الشحن الجوي ذات 11 رقمًا، وانتقل إلى تتبع الشحنات لدى شركة الطيران، وتابع الطائرة مباشرةً برقم الرحلة. مجانًا ودون تسجيل دخول."),
 "de": ("Flug- & AWB-Tracking", "11-stellige Luftfrachtbriefnummer prüfen, direkt zum Cargo-Tracking der Airline springen und das Flugzeug live per Flugnummer verfolgen. Kostenlos."),
 "es": ("Seguimiento de vuelos y AWB", "Valide una guía aérea de 11 dígitos, acceda al rastreo de carga de la aerolínea y siga el avión en directo por número de vuelo. Gratis y sin registro."),
 "fr": ("Suivi des vols et LTA", "Vérifiez une LTA à 11 chiffres, accédez au suivi fret de la compagnie et suivez l'avion en direct par numéro de vol. Gratuit, sans inscription."),
 "it": ("Tracking voli e AWB", "Verifica una lettera di vettura aerea di 11 cifre, apri il tracking cargo della compagnia e segui l'aereo in diretta col numero di volo. Gratis."),
}),
("tquoj", "/vessel-schedules", {
 "ar": ("مواعيد الإبحار في مصر", "رحلات الإبحار من وإلى الإسكندرية ودمياط وبورسعيد والعين السخنة لدى كبرى الخطوط الملاحية، مع رمز UN/LOCODE لكل ميناء. مجانًا ودون تسجيل دخول."),
 "de": ("Schiffsfahrpläne Ägypten", "Abfahrten von und nach Alexandria, Damietta, Port Said und Ain Sokhna bei den großen Reedereien, mit dem UN/LOCODE jedes Hafens. Kostenlos."),
 "es": ("Itinerarios navieros Egipto", "Salidas desde y hacia Alejandría, Damietta, Port Said y Ain Sokhna de las principales navieras, con el UN/LOCODE de cada puerto. Gratis y sin registro."),
 "fr": ("Horaires maritimes Égypte", "Départs vers et depuis Alexandrie, Damiette, Port-Saïd et Ain Sokhna chez les grands armateurs, avec l'UN/LOCODE de chaque port. Gratuit, sans inscription."),
 "it": ("Orari navi Egitto", "Partenze da e per Alessandria, Damietta, Port Said e Ain Sokhna dei principali vettori, con l'UN/LOCODE di ogni porto. Gratis, senza login."),
}),
("tmhs2", "/load-calculator", {
 "ar": ("حاسبة تحميل الحاويات", "اعرف عدد المنصات أو الصناديق التي تتسع لها حاوية 20 أو 40 أو 45 قدمًا أو مقطورة 13.6 م، مع مراعاة حدود التستيف والوزن. مجانًا ودون تسجيل دخول."),
 "de": ("Container-Ladeplaner", "Wie viele Paletten oder Kartons passen in einen 20-, 40- oder 45-Fuß-Container oder einen 13,6-m-Trailer, mit Stapel- und Gewichtsgrenzen. Kostenlos."),
 "es": ("Calculadora de carga", "Calcule cuántos palés o cajas caben en un contenedor de 20, 40 o 45 pies o un remolque de 13,6 m, con límites de apilado y peso. Gratis y sin registro."),
 "fr": ("Calculateur de chargement", "Combien de palettes ou de colis tiennent dans un conteneur 20, 40 ou 45 pieds ou une remorque de 13,6 m, gerbage et poids compris. Gratuit."),
 "it": ("Calcolo carico container", "Scopri quanti pallet o colli entrano in un container da 20, 40 o 45 piedi o in un rimorchio da 13,6 m, con limiti di impilaggio e peso. Gratis."),
}),
("vwpa2", "/chargeable-weight", {
 "ar": ("حاسبة الوزن المحتسب", "الوزن الحجمي والوزن المحتسب للشحن الجوي (1:6000) والسريع (1:5000) والبري (1:3000) والبحري، مع شرح كل قاعدة خطوة بخطوة. مجانًا ودون تسجيل دخول."),
 "de": ("Frachtgewicht-Rechner", "Volumen- und frachtpflichtiges Gewicht für Luft (1:6000), Kurier (1:5000), Straße (1:3000) und See, jede Regel Schritt für Schritt erklärt. Kostenlos."),
 "es": ("Calculadora de peso tasable", "Peso volumétrico y tasable para aéreo (1:6000), courier (1:5000), carretera (1:3000) y marítimo, con cada regla explicada paso a paso. Gratis."),
 "fr": ("Calcul du poids taxable", "Poids volumétrique et taxable pour l'aérien (1:6000), l'express (1:5000), la route (1:3000) et le maritime, chaque règle expliquée pas à pas. Gratuit."),
 "it": ("Calcolo peso tassabile", "Peso volumetrico e tassabile per aereo (1:6000), corriere (1:5000), strada (1:3000) e mare, con ogni regola spiegata passo per passo. Gratis, senza login."),
}),
("ubn1p", "/duties-taxes-calculator", {
 "ar": ("حاسبة الرسوم والضرائب الجمركية", "اعثر على البند الجمركي لبضائعك في التعريفة المصرية، واحصل على الرسوم والضريبة والمصروفات وفق التعريفة الرسمية واتفاقيات التجارة، عبر بريدك الإلكتروني."),
 "de": ("Zollrechner Ägypten", "Finden Sie die ägyptische Zolltarifnummer Ihrer Ware und erhalten Sie Zoll, MwSt. und Gebühren laut offiziellem Tarif inkl. Präferenzsätzen per E-Mail."),
 "es": ("Aranceles e impuestos Egipto", "Encuentre la partida arancelaria egipcia de su mercancía y reciba por correo aranceles, IVA y tasas según el arancel oficial, con tipos preferenciales."),
 "fr": ("Droits et taxes Égypte", "Trouvez la position tarifaire égyptienne de vos marchandises et recevez par e-mail droits, TVA et frais selon le tarif officiel, taux préférentiels inclus."),
 "it": ("Calcolo dazi e tasse Egitto", "Trova la voce doganale egiziana della tua merce e ricevi via email dazi, IVA e diritti secondo la tariffa ufficiale, incluse le aliquote preferenziali."),
}),
("qsa0d", "/get-a-quote", {
 "ar": ("اطلب عرض سعر للشحن", "أرسل المنشأ والوجهة ونوع البضاعة والأبعاد، وسيرد عليك أحد المتخصصين بعرض سعر مخصّص للشحن الجوي أو البحري أو البري شاملًا التخليص الجمركي."),
 "de": ("Frachtangebot anfordern", "Senden Sie Abgangsort, Ziel, Ware und Maße. Ein Spezialist antwortet mit einem Angebot für Luft-, See- oder Landfracht, inklusive Verzollung."),
 "es": ("Solicite una cotización", "Envíe origen, destino, mercancía y medidas. Un especialista le responde con una cotización aérea, marítima o terrestre a medida, con despacho aduanero."),
 "fr": ("Demander un devis fret", "Indiquez origine, destination, marchandise et dimensions. Un spécialiste vous envoie un devis aérien, maritime ou routier sur mesure, dédouanement inclus."),
 "it": ("Richiedi un preventivo", "Indica origine, destinazione, merce e dimensioni. Uno specialista ti invia un preventivo aereo, marittimo o terrestre su misura, sdoganamento incluso."),
}),
("vhupk", "/contact", {
 "ar": ("اتصل بنا", "اتصل على +20 2 2690 7601 أو راسلنا على inquiry@rockit.com.eg من الأحد إلى الخميس، 08:30–16:30 بتوقيت القاهرة. المقر الرئيسي: مصر الجديدة، القاهرة."),
 "de": ("Kontakt", "Rufen Sie +20 2 2690 7601 an oder schreiben Sie an inquiry@rockit.com.eg, So–Do 08:30–16:30 Uhr Kairoer Zeit. Zentrale: Heliopolis, Kairo."),
 "es": ("Contacto", "Llame al +20 2 2690 7601 o escriba a inquiry@rockit.com.eg, de domingo a jueves, 08:30–16:30 hora de El Cairo. Sede: Heliópolis, El Cairo."),
 "fr": ("Contactez-nous", "Appelez le +20 2 2690 7601 ou écrivez à inquiry@rockit.com.eg, du dimanche au jeudi, 08h30–16h30 heure du Caire. Siège : Héliopolis, Le Caire."),
 "it": ("Contatti", "Chiama il +20 2 2690 7601 o scrivi a inquiry@rockit.com.eg, da domenica a giovedì, 08:30–16:30 ora del Cairo. Sede: Heliopolis, Il Cairo."),
}),
("wanv7", "/privacy-policy", {
 "ar": ("سياسة الخصوصية", "كيف تجمع Rockit Transport Services & Logistics البيانات الشخصية من هذا الموقع والاستفسارات ونماذج التواصل وتستخدمها وتحميها، والخيارات المتاحة لك."),
 "de": ("Datenschutzerklärung", "Wie Rockit Transport Services & Logistics personenbezogene Daten aus Website, Anfragen und Formularen erhebt, nutzt und schützt, und Ihre Rechte."),
 "es": ("Política de privacidad", "Cómo Rockit Transport Services & Logistics recoge, usa y protege los datos personales de este sitio, consultas y formularios, y qué opciones tiene usted."),
 "fr": ("Politique de confidentialité", "Comment Rockit Transport Services & Logistics collecte, utilise et protège les données personnelles du site, des demandes et formulaires, et vos choix."),
 "it": ("Informativa sulla privacy", "Come Rockit Transport Services & Logistics raccoglie, usa e protegge i dati personali da sito, richieste e moduli, e quali scelte hai."),
}),
]

MENU_INSIGHTS = {"en": "Insights", "ar": "أدلة ومقالات", "de": "Ratgeber", "es": "Guías", "fr": "Guides", "it": "Guide"}

BANNED = re.compile(r"heavy|schwergut|schwerlast|carga pesada|colis lourds|lourd|pesante|ثقيل|ثقيلة", re.I)
EMAIL = re.compile(r"[\w.+-]+@[\w.-]+")

def title(pid, lang, topic):
    return f"{B} | {topic}" if pid == "c1dmp" else f"{topic} | {B}"

out, errs = [], []
assert len(P) == 24 and len({p[0] for p in P}) == 24
for pid, path, tr in P:
    row = {"id": pid, "path": path, "langs": {}}
    for lg in L:
        topic, desc = tr[lg]
        t = title(pid, lg, topic)
        if len(t) > 72: errs.append(f"{pid}/{lg} title {len(t)}: {t}")
        if len(desc) > 155: errs.append(f"{pid}/{lg} desc {len(desc)}: {desc}")
        if BANNED.search(t + " " + desc): errs.append(f"{pid}/{lg} banned term: {t} / {desc}")
        for e in EMAIL.findall(desc):
            if e not in ("inquiry@rockit.com.eg", "support@rockit.com.eg"): errs.append(f"{pid}/{lg} email {e}")
        row["langs"][lg] = {"url": f"https://www.rockit-transport.com/{lg}{'' if path == '/' else path}",
                            "seoTitle": t, "metaDescription": desc,
                            "socialTitle": t, "socialDescription": desc,
                            "lenTitle": len(t), "lenDesc": len(desc)}
    out.append(row)

if errs:
    print("\n".join(errs)); sys.exit(1)

here = Path(__file__).parent
(here / "seo_translations.json").write_text(json.dumps({"site": "0e184a47-8d16-405a-9018-42d1181fadd1", "menuInsights": MENU_INSIGHTS, "pages": out}, ensure_ascii=False, indent=1))
md = ["# Translated page SEO — rockit-transport.com", "",
      "Enter in Wix Studio editor → language switcher → each page → SEO basics + Social share. Social title/description = SEO title/description.", "",
      "Menu label for Insights (Company menu): " + ", ".join(f"{k}: {v}" for k, v in MENU_INSIGHTS.items()), ""]
for r in out:
    md.append(f"## {r['path']} ({r['id']})")
    for lg, v in r["langs"].items():
        md.append(f"- **{lg}** title ({v['lenTitle']}): {v['seoTitle']}")
        md.append(f"  - description ({v['lenDesc']}): {v['metaDescription']}")
    md.append("")
(here / "seo_translations.md").write_text("\n".join(md))
print("OK", len(out), "pages x", len(L), "languages; max title", max(v['lenTitle'] for r in out for v in r['langs'].values()), "max desc", max(v['lenDesc'] for r in out for v in r['langs'].values()))
