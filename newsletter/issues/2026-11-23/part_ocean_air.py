"""Voyage 002 · ocean, Red Sea/Hormuz, carriers & costs, air, logistics pages. Imported by edition_content.py.
Every figure is from research/research_ocean.md or research/research_air_logistics.md (fetched pages, 16–22 Nov 2026)."""
CN = "Container News"
GC = "gCaptain"
LS = "The Loadstar"
ACN = "Air Cargo News"
ST = "STAT Times"
FW = "FreightWaves"
SB = "Ship & Bunker"

SOURCES = {
    # ---------------- ocean
    "drewry": ("Drewry", "World Container Index – 19 Nov", "19 Nov 2026", "https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry"),
    "drewry_redsea": ("Drewry", "Red Sea Diversion Tracker – 17 Nov", "17 Nov 2026", "https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/red-sea-diversion-tracker"),
    "drewry_blank": ("Drewry", "Cancelled Sailings Tracker – 20 Nov", "20 Nov 2026", "https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/cancelled-sailings-tracker"),
    "freightos17": ("Freightos", "November 17, 2026 Update", "17 Nov 2026", "https://www.freightos.com/freight-resources/us-air-cargo-recovering-from-outage-new-us-cn-tensions-ahead-of-talks-november-17-2026-update/"),
    "xeneta20": ("Xeneta", "Weekly ocean freight market update, 20 November 2026", "20 Nov 2026", "https://www.xeneta.com/news/ocean-freight-market-update-2026-11-20"),
    "xeneta13": ("Xeneta", "Weekly Ocean Container Shipping Market Update – 13.11.26", "13 Nov 2026", "https://www.xeneta.com/news/xeneta-weekly-ocean-container-shipping-market-update-13.11.26"),
    "cn_msc_fak": (CN, "MSC raises December FAK rates to Mediterranean and Black Sea", "12 Nov 2026", "https://container-news.com/msc-raises-december-fak-rates-to-mediterranean-and-black-sea/"),
    "cn_asiamed": (CN, "Asia–Mediterranean freight pricing: The costs beyond headline rates", "10 Nov 2026", "https://container-news.com/asia-mediterranean-freight-pricing-the-costs-beyond-headline-rates/"),
    "cn_cma_dec": (CN, "CMA CGM announces new Asia–Mediterranean rates and Mozambique surcharge", "18 Nov 2026", "https://container-news.com/cma-cgm-announces-new-asia-mediterranean-rates-and-mozambique-surcharge/"),
    "cn_hapag_fak": (CN, "Hapag-Lloyd raises Far East–Europe freight rates from December", "15 Nov 2026", "https://container-news.com/hapag-lloyd-raises-far-east-europe-freight-rates-from-december/"),
    "cn_gemini": (CN, "Maersk and Hapag-Lloyd return three more Gemini services to Suez", "17 Nov 2026", "https://container-news.com/maersk-and-hapag-lloyd-return-three-more-gemini-services-to-suez/"),
    "ls_gemini": (LS, "Gemini carriers target complete return to Suez transits by mid-January", "17 Nov 2026", "https://theloadstar.com/gemini-carriers-target-complete-return-to-suez-transits-by-mid-january/"),
    "gc_houthi": (GC + " / Reuters", "Houthis Order Ships to Leave Saudi Red Sea Ports After Hodeidah Airstrikes", "20 Nov 2026", "https://gcaptain.com/houthis-order-ships-to-leave-saudi-red-sea-ports-after-hodeidah-airstrikes/"),
    "sb_oil": (SB, "Third weekly loss for oil as Houthi threats on Saudi ports fail to impress", "20 Nov 2026", "https://shipandbunker.com/news/world/472653-third-weekly-loss-for-oil-based-on-glut-fears-as-houthi-threats-on-saudi-ports-fail-to-impress"),
    "gc_hormuz20": (GC, "Another Tanker Hit in Strait of Hormuz as Maritime Attacks Surge Worldwide", "20 Nov 2026", "https://gcaptain.com/another-tanker-hit-in-strait-of-hormuz-as-maritime-attacks-surge-worldwide/"),
    "gc_taragas": (GC, "TARA GAS Burning Off Oman as Another Tanker Attack Leaves 11 Injured", "18 Nov 2026", "https://gcaptain.com/tara-gas-burning-off-oman-as-another-tanker-attack-leaves-11-injured/"),
    "gc_iran_attacks": (GC + " / Bloomberg", "Iran Intensifies Hormuz Tanker Attacks Just as Oil Prices Slide", "19 Nov 2026", "https://gcaptain.com/iran-intensifies-hormuz-tanker-attacks-just-as-oil-prices-slide/"),
    "gc_oman21": (GC + " / Reuters", "Two Tanker Incidents Reported Near Oman; Vessel Hit Mine East Of Hormuz", "21 Nov 2026", "https://gcaptain.com/two-tanker-incidents-reported-near-oman-vessel-hit-mine-east-of-hormuz/"),
    "cn_msc_fuj": (CN, "MSC expands regional network with two new services", "21 Nov 2026", "https://container-news.com/msc-expands-regional-network-with-two-new-services/"),
    "sb_prices": (SB, "Bunker prices – Global 20 Ports Average (values dated 20 Nov)", "20 Nov 2026", "https://shipandbunker.com/prices"),
    "sb_hapag_mfs": (SB, "Hapag-Lloyd to Introduce New Marine Fuel Surcharge from 2027", "19 Nov 2026", "https://shipandbunker.com/news/world/135496-hapag-lloyd-to-introduce-new-marine-fuel-surcharge-from-2027"),
    "cn_zim": (CN, "ZIM net profit surges to $830 million in Q3 as freight rates climb", "18 Nov 2026", "https://container-news.com/zim-net-profit-surges-to-830-million-in-q3-as-freight-rates-climb/"),
    "imo_cal": ("IMO", "Meeting summaries and calendar (MEPC 85, MEPC.ES/2)", "accessed 22 Nov 2026", "https://www.imo.org/en/MediaCentre/MeetingSummaries/Pages/Default.aspx"),
    "gc_imo_assoc": (GC, "Shipping Industry Presses for Global IMO Climate Deal as Divisions Over Rules Persist", "18 Nov 2026", "https://gcaptain.com/shipping-industry-presses-for-global-imo-climate-deal-as-divisions-over-rules-persist/"),
    "gc_imo_fin": (GC, "IMO Finds Just $10.5 Billion in Maritime Climate Finance", "20 Nov 2026", "https://gcaptain.com/imo-finds-just-10-5-billion-in-maritime-climate-finance/"),
    "sb_fmc": (SB, "IBIA 2026: US says IMO Net-Zero Framework 'cannot be adopted'", "11 Nov 2026", "https://shipandbunker.com/news/am/638910-ibia-2026-us-says-imo-net-zero-framework-cannot-be-adopted-will-never-be-enforced"),
    "cn_gemini_oct": (CN, "Maersk expands Gemini network overhaul", "19 Oct 2026", "https://container-news.com/maersk-expands-gemini-network-overhaul/"),
    "hsn_maersk": ("Hellenic Shipping News (Maersk)", "Maersk Europe Market Update November 2026", "Nov 2026", "https://www.hellenicshippingnews.com/maersk-europe-market-update-november-2026/"),
    "gc_lalb": (GC + " / Reuters", "Southern California Port Employers, Watchmen Union Reach Tentative Deal", "21 Nov 2026", "https://gcaptain.com/southern-california-port-employers-watchmen-union-reach-tentative-deal/"),
    "cn_scfi": (CN, "Container freight rates remain under pressure as major benchmarks decline", "16 Nov 2026", "https://container-news.com/container-freight-rates-remain-under-pressure-as-major-benchmarks-decline/"),
    # ---------------- air & logistics
    "st_wcd45": (ST, "Global air cargo traffic falls 2% as rates rise (WorldACD wk 45)", "17 Nov 2026", "https://www.stattimes.com/air-cargo/global-air-cargo-traffic-falls-2-as-rates-continue-to-increase-1361323"),
    "ls_kal": (LS, "Korean Air maximises Americas capacity as AI cargo adds to peak pressure", "17 Nov 2026", "https://theloadstar.com/korean-air-maximises-americas-capacity-as-ai-cargo-adds-to-peak-pressure/"),
    "ls_tatl": (LS, "Transatlantic airfreight rates at highest level for four years", "18 Nov 2026", "https://theloadstar.com/transatlantic-airfreight-rates-at-highest-level-for-four-years/"),
    "ls_cap": (LS, "Expected airfreight capacity boost 'flatters the picture' – not new space", "20 Nov 2026", "https://theloadstar.com/expected-airfreight-capacity-boost-flatters-the-picture-not-new-space/"),
    "iata_fuel": ("IATA", "Jet Fuel Price Monitor", "accessed 22 Nov 2026", "https://www.iata.org/en/publications/economics/fuel-monitor/"),
    "iata_icao": ("IATA", "Governments back global agenda for air transport (ATConf/7)", "20 Nov 2026", "https://www.iata.org/en/pressroom/2026-releases/11-20-governments-back-global-agenda-for-more-competitive-sustainable-air-transport-industry/"),
    "st_cx": (ST, "Cathay Cargo volumes rise 8% in October", "20 Nov 2026", "https://www.stattimes.com/financial/cathay-cargo-volumes-rise-8-in-october-1361363"),
    "st_ai_peak": (ST, "AI shipments challenge festive season air cargo capacity", "20 Nov 2026", "https://www.stattimes.com/air-cargo/ai-shipments-challenge-festive-season-air-cargo-capacity-1361369"),
    "acn_dgf_india": (ACN, "DHL Global Forwarding adds India through new Asia–Europe freighter flight", "16 Nov 2026", "https://www.aircargonews.net/freight-forwarder/2026/11/dhl-global-forwarding-adds-india-through-new-asia-europe-freighter-flight/"),
    "fw_dgf": (FW, "DHL Forwarding launches first-ever dedicated freighter service for India", "18 Nov 2026", "https://www.freightwaves.com/news/dhl-forwarding-launches-first-ever-dedicated-freighter-service-for-india"),
    "ls_cmagap": (LS, "CMA CGM shipping profit boom exposes logistics earnings gap", "16 Nov 2026", "https://theloadstar.com/cma-cgm-shipping-profit-boom-exposes-logistics-earnings-gap/"),
    "ls_ekol": (LS, "Sale of Neovia and Turkey's Ekol marks return of M&A", "19 Nov 2026", "https://theloadstar.com/sale-of-neovia-in-the-us-and-turkeys-ekol-marks-return-of-ma-to-logistics/"),
    "ls_expd": (LS, "Expeditors opens door to M&A after decades of organic growth", "19 Nov 2026", "https://theloadstar.com/expeditors-opens-door-to-ma-after-decades-of-organic-growth/"),
    "acn_ups": (ACN, "UPS plans to buy Smartways Logistics to expand in Australasia", "18 Nov 2026", "https://www.aircargonews.net/business/2026/11/ups-plans-to-buy-smartways-logistics-to-expand-in-australasia/"),
    "st_dhlsc": (ST, "DHL Supply Chain Q3 revenue up 12%", "18 Nov 2026", "https://www.stattimes.com/financial/dhl-supply-chain-q3-revenue-up-12-2026-tcv-to-top-8-billion-1361341"),
    "eu_cust": ("European Commission, DG TAXUD", "EU Customs Reform", "accessed 22 Nov 2026", "https://taxation-customs.ec.europa.eu/customs/eu-customs-reform_en"),
    "ls_bf": (LS, "Black Friday bundles test retail margins as EU parcel charges bite", "18 Nov 2026", "https://theloadstar.com/black-friday-bundles-test-retail-margins-as-eu-parcel-charges-bite/"),
    "acn_dawb": (ACN, "IATA urged to revise DAWB framework over forwarder liability concerns", "16 Nov 2026", "https://www.aircargonews.net/freight-forwarder/2026/11/iata-urged-to-revise-dawb-framework-over-forwarder-liability-concerns/"),
    "fw_dhlx": (FW, "DHL Express makes customs clearance easier for small cross-border shippers", "21 Nov 2026", "https://www.freightwaves.com/news/dhl-express-makes-customs-clearance-easier-for-small-cross-border-shippers"),
    "acn_cargoai": (ACN, "CargoAi launches platform to improve air cargo operational performance", "18 Nov 2026", "https://www.aircargonews.net/technology/2026/11/cargoai-launches-platform-to-improve-air-cargo-operational-performance/"),
    "acn_bkk": (ACN, "Forwarders warn of Bangkok air cargo delays as congestion continues", "19 Nov 2026", "https://www.aircargonews.net/ground-handler/2026/11/forwarders-warn-of-bangkok-air-cargo-delays-as-congestion-continues/"),
    "acn_us_gs": (ACN, "US air cargo supply chains recover following ground stop", "16 Nov 2026", "https://www.aircargonews.net/cargo-airport/2026/11/us-air-cargo-supply-chains-recover-following-ground-stop/"),
    "acn_ekvs": (ACN, "Emirates SkyCargo and Virgin Cargo look to expand BSA agreements", "17 Nov 2026", "https://www.aircargonews.net/airlines/2026/11/emirates-skycargo-and-virgin-cargo-look-to-expand-bsa-agreements/"),
    "ls_indgulf": (LS, "More pain for India-Gulf shippers as costly box returns add to rising rates", "17 Nov 2026", "https://theloadstar.com/more-pain-for-india-gulf-shippers-as-costly-box-returns-add-to-rising-rates/"),
    "ls_jfk": (LS, "JFK holiday-pay complaints heat up AGI dispute with union", "19 Nov 2026", "https://theloadstar.com/jfk-holiday-pay-complaints-heat-up-agi-dispute-with-union/"),
}


def P(text, src=None, cls=""):
    return {"k": "p", "text": text, "src": src, "cls": cls}


def brief(tag, head, text, src, why_=None):
    b = {"k": "brief", "tag": tag, "head": head, "text": text if isinstance(text, list) else [text], "src": src}
    if why_:
        b["why"] = why_
    return b


# ------------------------------------------------------------------ ocean freight
p_ocean = {"section": "Ocean freight", "title": "Ocean freight", "label": "Rates · December tariffs · surcharges", "blocks": [
    {"k": "grid", "cols": "1.18fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "Lead · Asia → Mediterranean", "head": "Every lane fell except ours",
         "deck": "Asia–Med spot rose 6–7% last week while every other main lane slipped. Egypt's importers now pay about $1,550 a box more than North Europe's.",
         "text": [
             "Drewry's World Container Index fell 3% to $4,176 per 40ft on 19 November, its fourth weekly fall, because transpacific rates dropped. Shanghai–Genoa, Drewry's closest proxy for Egypt's Mediterranean ports, went the other way: up 6% to $4,436 after three flat weeks. Shanghai–Rotterdam held at $3,496.",
             "Xeneta's data show the same split. Far East–Mediterranean spot rose 6.8% to $4,989 per 40ft, while Far East–North Europe fell 2.3% to $3,438 and every other fronthaul eased. Average Med rates are now $1,551 a box above North Europe. Xeneta ties the move to the Red Sea: Bab el-Mandeb container transits have fallen from 16.6 a day on 25 October to 11.9 on 19 November, and Med trades are the most exposed.",
             "Freightos, whose data run to mid-week, still had Asia–Med flat at about $4,300. The rise came late in the week: check the date of any index you are quoted.",
         ], "src": ["drewry", "xeneta20", "freightos17"],
         "why": "Last week the gap between December tariffs and the spot market was about $2,000 a box. This week the three big carriers' December tariffs ($6,500–6,800) sit about $1,500–1,800 above Xeneta's average, and the market is rising towards them. December's increases are more likely to stick on Asia–Med than they were in November; book early in the month and get the surcharges in writing."},
    ], [
        {"k": "chart", "type": "hbar", "width_mm": 66, "max": 7400, "prefix": "$",
         "sub": "US$ per 40ft · Asia → Egypt / East Med", "title": "Spot vs December tariff",
         "legend": [["spot", "Spot index (market average)"], ["gold", "Published tariff (FAK)"]],
         "rows": [["Freightos FBX13 · Asia → Med · 17 Nov", 4300, "spot"], ["Drewry · Shanghai → Genoa · 19 Nov", 4436, "spot"],
                  ["Xeneta · Far East → Med · 19 Nov", 4989, "spot"], ["MSC FAK · Far East → E. Med · 1 Dec", 6500, "gold"],
                  ["Hapag-Lloyd FAK · → Egypt/E. Med · 1 Dec", 6600, "gold"], ["CMA CGM FAK · Asia → E. Med · 1–14 Dec", 6800, "gold"]],
         "note": "Spot = weekly market averages. FAK = published base tariff before local charges and some surcharges.",
         "src": ["freightos17", "drewry", "xeneta20", "cn_msc_fak", "cn_hapag_fak", "cn_cma_dec"]},
        {"k": "chart", "type": "hbar", "width_mm": 66, "max": 5600, "prefix": "$",
         "sub": "Xeneta · average spot, US$ per 40ft", "title": "The Med premium widens",
         "rows": [["Far East → Med · 13 Nov", 4666, "spot"], ["Far East → Med · 19 Nov", 4989, "gold"],
                  ["Far East → N. Europe · 13 Nov", 3588, "spot"], ["Far East → N. Europe · 19 Nov", 3438, "gold"]],
         "note": "Premium of Med over North Europe: $1,078 on 13 Nov, $1,551 on 19 Nov.", "src": ["xeneta13", "xeneta20"]},
    ]]},
    {"k": "table", "caption": "December rate actions to Egypt and the Med · as announced", "head": ["Carrier", "Trade", "Charge", "Amount", "Effective"], "num_cols": [3],
     "rows": [
         {"cells": ["Maersk", "Far East → Mediterranean (Egypt in scope)", "Peak season surcharge", "$750 / $1,500 (20' / 40', 45')", "from 23 Nov"], "src": ["cn_asiamed"]},
         {"cells": ["MSC", "Far East → East Med", "FAK", "$5,100 / $6,500 (+$800 on 40')", "1–14 Dec"], "src": ["cn_msc_fak"]},
         {"cells": ["MSC", "Far East → West Med & Adriatic", "FAK", "$6,500 per 40' (+$1,200)", "1–14 Dec"], "src": ["cn_msc_fak"]},
         {"cells": ["MSC", "Far East → Algeria / Libya & Tunisia / Casablanca", "FAK", "$8,200 / $8,000 / $7,000 (40')", "1–14 Dec"], "src": ["cn_msc_fak"]},
         {"cells": ["MSC", "Global fuel surcharge (inside the FAK)", "GFS", "$304 per TEU (Nov: $266)", "December"], "src": ["cn_msc_fak"]},
         {"cells": ["Hapag-Lloyd", "Far East → Egypt, Türkiye, East Med", "FAK", "$5,300 / $6,600 (20' / 40')", "1 Dec"], "src": ["cn_hapag_fak"]},
         {"cells": ["CMA CGM", "Asia → East Med / North Africa", "FAK (incl. bunker, EU ETS, LSS)", "$5,500 / $6,800 · $6,400 / $8,800", "1–14 Dec"], "src": ["cn_cma_dec"]},
         {"cells": ["Hapag-Lloyd", "All 2027 contracts", "New Marine Fuel Surcharge", "Q1 rates published 1 Dec", "1 Jan 2027"], "src": ["sb_hapag_mfs"]},
     ], "note": "Carrier figures as reported by Container News and Ship & Bunker; carriers' own sites could not be read. Drewry counts December PSS of $1,000–1,600 per 40ft across Asia–Europe/Med. MSC's piracy-risk and Suez surcharges apply on top. Hapag-Lloyd names Egypt explicitly; whether CMA CGM's East Med zone includes Egyptian ports is not stated."},
]}

# ------------------------------------------------------------------ Suez, Red Sea, Hormuz
p_straits = {"section": "Suez, Red Sea & Hormuz", "title": "Suez, Red Sea & Hormuz", "label": "Ships return · risk rises", "blocks": [
    {"k": "grid", "cols": "1.2fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "The Red Sea", "head": "More ships through Suez, just as the risk rises",
         "deck": "Gemini moves its last three North Europe loops back to the canal. In Yemen, the Houthis have taken the Red Sea coast.",
         "text": [
             "Maersk and Hapag-Lloyd will move their NE1, NE2 and NE3 Asia–North Europe services from the Cape to Suez “on a structural basis”. The first westbound sailings are *Mary Maersk* from Ningbo around 4 December, *Alette Maersk* from Shanghai around 20 December and the 23,700 TEU *Damietta Express* from Shanghai around 14 January. Drewry says 60% of Asia–Europe capacity is back on the Suez route.",
             "The security picture moved the other way. Drewry reports a “material deterioration” around Bab el-Mandeb and warns against extrapolating better traffic into December and January. Reuters reports that the Houthis have seized Yemen's Red Sea coast and pushed government forces back to Aden. The Saudi-led coalition said it struck Hodeidah port on 20 November; Houthi spokesman Yahya Saree told shipping companies to “immediately evacuate their ships” from Saudi Red Sea ports, and the group said it would target ports “in Jeddah and the Red Sea”. Yemen's information minister said Hodeidah remains fully operational. No attack on a merchant ship there was verified in the week.",
         ], "src": ["cn_gemini", "ls_gemini", "drewry_redsea", "gc_houthi", "sb_oil"],
         "why": "The Suez return is what is pushing capacity and rates down in 2027 forecasts. Keep Cape-routing and war-risk clauses in every Red Sea contract, and for Saudi deliveries ask what the plan is if Jeddah calls are suspended."},
    ], [
        {"k": "box", "kicker": "New mainline calls in Egypt", "title": "Port Said and Damietta join Gemini loops", "blocks": [
            {"k": "ticks", "items": [
                "**AE11:** Port Said replaces the westbound Tangier call, from *Estelle Maersk* leaving Shanghai on 17 November.",
                "**AE19:** Damietta added, from *Ane Maersk* leaving Xingang on 18 November.",
                "**AE12:** already calls Port Said East both ways; Colombo added from about 12 January.",
                "Maersk lists AE5, AE11, AE12, AE15, AE19, ME1 and ME2 as routed via Suez; NE1–NE3 follow from December.",
            ], "srcs": [["cn_gemini_oct"], ["cn_gemini_oct"], ["cn_gemini_oct"], ["hsn_maersk", "cn_gemini"]]},
            P("Schedules as announced in October; we could not confirm the 17–18 November departures sailed as planned.", cls="small"),
        ]},
        {"k": "tiles", "cols": 2, "items": [
            {"value": "57", "label": "container ships through Suez in the week to 15 Nov (+73% y/y)", "asof": "Drewry", "src": ["drewry_redsea"]},
            {"value": "60%", "label": "of Asia–Europe capacity back on the Suez route", "asof": "Drewry, 17 Nov", "src": ["drewry_redsea"]},
            {"value": "11.9", "label": "container transits a day at Bab el-Mandeb, down from 16.6 on 25 Oct", "asof": "Xeneta, 19 Nov", "src": ["xeneta20"]},
            {"value": "126", "label": "Cape of Good Hope transits, the fewest since January", "asof": "Drewry", "src": ["drewry_redsea"]},
        ]},
    ]]},
    {"k": "rule"},
    {"k": "h", "text": "Hormuz: attacks at their highest since October"},
    {"k": "flow", "n": 2, "blocks": [
        P("UKMTO's weekly overview of 20 November counted 115 outbound and 148 inbound Hormuz transits, down from 139 and 169 a week earlier, and six verified attacks in the period to 18 November. In the Gulf, Orbital Risk counted seven strikes on six ships, four of them tankers within 13nm of Khasab. JMIC rates the threat as SEVERE.", ["gc_hormuz20"]),
        {"k": "tiles", "cols": 2, "items": [
            {"value": "115 / 148", "label": "outbound / inbound Hormuz transits (was 139 / 169)", "asof": "UKMTO, 20 Nov", "src": ["gc_hormuz20"]},
            {"value": "15", "label": "attacks and piracy incidents worldwide in 7 days (+50%)", "asof": "Orbital Risk", "src": ["gc_hormuz20"]},
            {"value": "~10m b/d", "label": "Hormuz oil flows, 7-day average (13.4m at start of Nov)", "asof": "Kpler via Bloomberg", "src": ["gc_iran_attacks"]},
            {"value": "6", "label": "verified attacks to 18 Nov (4 in the Strait, 2 in the Gulf)", "asof": "UKMTO", "src": ["gc_hormuz20"]},
        ]},
        P("The LPG tanker *TARA GAS* was hit on 16 and 17 November and abandoned; one Indian seafarer is missing. *NAVIG8 MESSI*, managed by ADNOC L&S, was hit on 17 November, with one crew member missing and 11 injured. UKMTO reported further tanker strikes near Khasab on 20 and 21 November. Iran's navy claimed a mine strike east of Hormuz; Reuters could not verify it.", ["gc_taragas", "gc_hormuz20", "gc_oman21"]),
        {"k": "html", "html": '<div class="why"><b>Why it matters</b>MSC is adding a second Fujairah shuttle (Colombo–Khor Fakkan–Fujairah–Sohar) from December, outside the Strait. For Egypt–Gulf cargo, plan on Gulf of Oman discharge plus trucking, or Saudi gateways, and price in landside congestion (page 7).</div>'},
    ]},
]}

# ------------------------------------------------------------------ carriers & costs
p_costs = {"section": "Carriers & costs", "title": "Carriers & costs", "label": "Fuel · reliability · results · carbon", "blocks": [
    {"k": "grid", "cols": "1fr 1fr", "gap": "8mm", "columns": [[
        brief("Fuel", "Bunkers fall; MSC's fuel surcharge rises", "Ship & Bunker's Global 20 Ports average put VLSFO at $838 a tonne on 20 November, down $25.50 in a week (Fujairah $800, Singapore $842, Rotterdam $705.50); MGO fell to $1,364. Brent was about $92 and has lost roughly 15% in November. MSC's December fuel surcharge nevertheless rises to $304 per TEU from $266.", ["sb_prices", "sb_oil", "cn_msc_fak"],
              "Fuel is cheaper than a month ago. Challenge any December BAF or GFS increase in your quotes."),
        brief("2027 contracts", "Hapag-Lloyd rewrites its fuel charge", "From 1 January 2027 Hapag-Lloyd replaces its Marine Fuel Recovery with a Marine Fuel Surcharge based on a full return to Suez routings, reviewed quarterly. First-quarter rates are published on 1 December.", ["sb_hapag_mfs"],
              "A Suez-based fuel charge should come in below the Cape-era one. Compare the 1 December figures before signing 2027 terms."),
        {"k": "chart", "type": "hbar", "width_mm": 76, "max": 1000, "prefix": "$", "dp": 2,
         "sub": "Ship & Bunker · VLSFO, US$ per tonne", "title": "What a tonne of fuel costs now",
         "rows": [["Global 20 Ports · 13 Nov", 863.5, "spot"], ["Global 20 Ports · 20 Nov", 838.0, "gold"], ["Fujairah · 20 Nov", 800.0, "spot"],
                  ["Singapore · 20 Nov", 842.0, "spot"], ["Rotterdam · 20 Nov", 705.5, "spot"]],
         "note": "MGO averaged $1,364 per tonne on 20 November.", "src": ["sb_prices"]},
    ], [
        brief("Reliability", "Two in three ships arrive late", "Drewry says East–West on-time performance fell from 40% in September to 34% in October. It expects 42 blank sailings out of 724 on the main East–West trades in weeks 48–52 (6%); the transpacific accounts for 48% of them, Asia–Europe/Med 33%.", ["drewry_blank"],
              "Build buffer stock and free-time allowances into December–January plans; Asia–Med capacity cuts are modest, so the rate push rests on surcharges."),
        brief("Results", "ZIM's profit jumps to $830m", "ZIM reported Q3 net income of $830m (Q3 2025: $123m) on revenue of $2.71bn, up 53%. Its average freight rate rose 55% to $2,480 per TEU, and it lifted 2026 adjusted EBITDA guidance to $3.3–3.5bn.", ["cn_zim"]),
        brief("Carbon · IMO", "No global carbon price yet; two weeks to decide", "IMO's GHG working group meets 23–27 November and MEPC 85 runs 30 November–3 December. The resumed session to adopt the Net-Zero Framework is pencilled for 4 December, “subject to confirmation by MEPC 85”. Nine shipping associations, including BIMCO, ICS and WSC, called for a global deal on 18 November without endorsing the current text. The US Federal Maritime Commission chair said on 11 November that the framework “cannot be adopted, will never be enforced”.", ["imo_cal", "gc_imo_assoc", "sb_fmc"],
              "No global carbon charge reaches freight bills in 2027 either way. EU ETS charges already do: MSC's carbon surcharge to the Med is $133 per TEU."),
        brief("US West Coast", "Watchmen strike averted", "The Pacific Maritime Association and ILWU Local 26 reached a tentative deal on 21 November, averting a strike at Los Angeles and Long Beach. Ratification is pending.", ["gc_lalb"]),
    ]]},
    {"k": "panel", "kicker": "Rockit explains · in one paragraph", "title": "Why Asia–Med moved when everything else fell", "blocks": [
        P("Asia–Mediterranean services have no short way around Bab el-Mandeb: for a Med port, the Cape detour adds proportionally far more sailing than it does for Rotterdam. So when Red Sea transits fall, as they did by 28% between 25 October and 19 November, Med capacity tightens first and Med spot rates react first; Xeneta calls these trades the most operationally exposed to the region. That is how one security shock can lift Egypt's freight while the global index falls.", ["xeneta20"]),
    ]},
]}

# ------------------------------------------------------------------ air cargo
p_air = {"section": "Air cargo", "title": "Air cargo", "label": "Peak season · rates · capacity", "blocks": [
    {"k": "grid", "cols": "1.2fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "Air freight", "head": "Middle East lanes lead a 31% rise",
         "deck": "Global air rates are a third above last year. Rates out of the Middle East and South Asia have risen fastest, and Saudi Arabia has lost a third of its air cargo.",
         "text": [
             "WorldACD's figures for week 45 (2–8 November) put the global average at $3.45 per kg, up 2% in the week and 31% on a year earlier, while tonnage fell 2%. Middle East & South Asia (MESA) rose most, 63%; MESA–Europe was up 66% and Dubai origins 83%. Africa-origin rates, which include Egypt, rose 7% in a single week. Saudi Arabia's tonnage was 33% below its level before Houthi attacks began in early October.",
             "Freightos data reported by The Loadstar show Europe–US rates up 12% in a week to $3.27 per kg, the highest since December 2022, and China–North America up 16% to $9.25. Asia–Europe space is still available, CH Robinson says.",
             "Gulf hubs are still short of space. Consultancy Aevean says combined capacity at Doha, Dubai and Abu Dhabi is about 12% below pre-conflict levels, roughly 2,200 tonnes a day; Emirates, Qatar Airways and Etihad are back above 2025 levels, but foreign freighter capacity at the three hubs is down 49%. Xeneta sees air rates 5–10% lower in 2027, but only with a lasting Gulf peace deal.",
         ], "src": ["st_wcd45", "ls_tatl", "st_ai_peak", "ls_cap"],
         "why": "Egyptian exporters routing via Gulf hubs should book home-carrier space, not foreign freighters, and budget 2027 air contracts for a no-relief case. Importers from Europe for December delivery should book now."},
    ], [
        {"k": "chart", "type": "hbar", "width_mm": 76, "max": 90, "prefix": "+", "suffix": "%",
         "sub": "WorldACD · week 45 · rates year on year", "title": "Where air rates rose most",
         "rows": [["Dubai → Europe", 83, "gold"], ["MESA → US", 79, "spot"], ["India → Europe", 70, "spot"], ["MESA → Europe", 66, "gold"],
                  ["MESA origin (all)", 63, "spot"], ["Asia Pacific → US", 44, "spot"], ["Global", 31, "gold"], ["Asia Pacific → Europe", 26, "spot"]],
         "note": "Global average $3.45 per kg in week 45 (2–8 Nov).", "src": ["st_wcd45"]},
        {"k": "tiles", "cols": 2, "items": [
            {"value": "$3.45/kg", "label": "WorldACD global average rate", "delta": "▲ 2% w/w, +31% y/y", "dir": "up", "asof": "week 45", "src": ["st_wcd45"]},
            {"value": "−33%", "label": "Saudi Arabia air tonnage vs early October", "asof": "WorldACD", "src": ["st_wcd45"]},
            {"value": "−12%", "label": "Gulf hub capacity vs pre-conflict (≈2,200 t/day)", "asof": "Aevean, 20 Nov", "src": ["ls_cap"]},
            {"value": "$169.82", "label": "Jet fuel per barrel, global average (−5.1% w/w)", "asof": "IATA monitor; week not dated", "src": ["iata_fuel"]},
        ]},
    ]]},
    {"k": "rule"},
    {"k": "flow", "n": 2, "blocks": [
        brief("Asia", "Cathay grows; AI fills the transpacific", "Cathay Cargo carried 162,747 tonnes in October, up 7.5%, on capacity up just 0.5%. Korean Air reports “compounded capacity pressure” on the transpacific from Q4 consumer goods plus AI hardware.", ["st_cx", "ls_kal"]),
        brief("Forwarders' fleets", "DHL buys its own India freighter", "DHL Global Forwarding launched a twice-weekly 747 freighter linking Hong Kong, Navi Mumbai and Liège, targeting 25–30 tonnes per flight on the India sectors. It expects only about 20 freighters to be delivered worldwide in 2027, mostly to express firms.", ["acn_dgf_india", "fw_dgf"],
              "With few new freighters coming, shippers without contracted space will compete for what is left."),
        brief("Hubs", "Bangkok backlog; US recovers", "Bangkok's Thai Airways cargo terminal still has more than 1,000 lots outstanding after September floods; exports may roll two to three days. US networks recovered by 15–16 November from a four-hour nationwide ground stop on 13 November.", ["acn_bkk", "acn_us_gs"]),
        brief("Policy", "IATA: keep the EU ETS off international flights", "After ICAO's air transport conference (16–20 November), IATA urged EU states to back CORSIA rather than extend the EU ETS to international flights, and said 2026 passenger growth will be the weakest since 2009 outside the pandemic years.", ["iata_icao"],
              "Weaker passenger growth means less belly space on Cairo routes than airlines planned."),
    ]},
]}

# ------------------------------------------------------------------ the logistics business
p_logi = {"section": "The logistics business", "title": "The logistics business", "label": "Results · deals · rules · technology", "blocks": [
    {"k": "grid", "cols": "1fr 1fr", "gap": "8mm", "columns": [[
        {"k": "box", "kicker": "Rockit's read", "title": "What changed for forwarders this week", "blocks": [
            P("Two things land directly on our desks. First, airlines' revised Direct Air Waybill terms can make a forwarder liable for a shipper's misdeclaration, so we confirm each carrier's terms before tendering. Second, the EU now charges €5 per line on low-value parcels, which pushes e-commerce sellers towards consolidated shipments into EU warehouses."),
        ]},
        brief("Liability", "Forwarders push IATA to rewrite the DAWB", "The US Airforwarders Association and NCBFAA published a white paper on 16 November asking IATA to amend its revised Direct Air Waybill framework, in force since 1 July. Without a separate airline agreement, they say, a forwarder acting for a named shipper may carry liability for misdeclarations, undeclared dangerous goods and packaging failures. Australia's IFCBAA and Canada's CIFFA back the paper.", ["acn_dawb"],
              "Shippers: accurate descriptions and DG declarations protect you and your forwarder."),
        brief("E-commerce", "Europe's parcel charges bite: −63%", "The European Commission confirms its €2 handling fee applies from 1 November, on top of the €3 duty per item on parcels up to €150 since 1 July. Its preliminary count shows 555m low-value items entered the EU in Q3, against 1.51bn a year earlier. Each line on a declaration now adds €5.", ["eu_cust", "ls_bf"]),
    ], [
        {"k": "table", "caption": "Deals and results · 16–22 Nov", "head": ["Company", "What happened"],
         "rows": [
             {"cells": ["CMA CGM / CEVA", "Q3 group EBITDA $4.78bn (+61.6%); logistics EBITDA −14.4%, margin 9.3% → 6.7%; CEVA reorganised by 1 Jan 2027"], "src": ["ls_cmagap"]},
             {"cells": ["Arvato ← Ekol", "Buys Ekol's Turkish domestic business: 1.2m m², 26 warehouses"], "src": ["ls_ekol"]},
             {"cells": ["Logisteed ← Neovia", "Buys US contract logistics firm Neovia ($589m revenue, 2025)"], "src": ["ls_ekol"]},
             {"cells": ["UPS ← Smartways", "Buys Australia/NZ healthcare logistics firm; closing H1 2027"], "src": ["acn_ups"]},
             {"cells": ["Expeditors", "First investor day in 11 years: now evaluating acquisitions"], "src": ["ls_expd"]},
             {"cells": ["DHL Supply Chain", "Q3 revenue +12%; 2026 contracts to “far exceed €8 billion”"], "src": ["st_dhlsc"]},
         ]},
        brief("Technology", "Photos into customs descriptions", "DHL Express now turns a customer's photo of an item into a customs-compliant description in seconds, live in 10 Americas markets with more in 2027. CargoAi launched CargoQUALITY to benchmark airline and handler stations.", ["fw_dhlx", "acn_cargoai"],
              "Vague descriptions are a leading cause of customs holds, including under Egypt's ACI."),
        brief("Gulf corridors", "UAE landside strain", "India–Gulf shippers face booking curbs, congestion at Khor Fakkan and empty-return charges of up to $1,200 per 40ft to the Sajaa dry port. Emirates SkyCargo and Virgin Atlantic Cargo signed an MoU to widen interline and block-space deals.", ["ls_indgulf", "acn_ekvs"],
              "For Egypt–UAE cargo, allow extra clearance time and ask about empty-return charges."),
    ]]},
    {"k": "p", "text": "Turkey is a major sourcing market for Egypt: DFDS, which runs the Trieste–Damietta ro-ro, already owns Ekol's international road business.", "src": ["ls_ekol"]},
]}
