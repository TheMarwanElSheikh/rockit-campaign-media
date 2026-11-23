#!/usr/bin/env python3
"""Full edition, Voyage 002 (23 Nov 2026). Writes edition.json next to this file.

Every figure was read on a fetched source page between 16 and 22 November 2026 (see research/ and AUDIT_EDITION.md).
Ocean, Red Sea/Hormuz, carriers, air and logistics pages live in part_ocean_air.py; the rest is here.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from part_ocean_air import SOURCES as S1, P, brief, p_ocean, p_straits, p_costs, p_air, p_logi  # noqa: E402

GC = "gCaptain"
EAM = "EnterpriseAM"
ZW = "Zawya"
CN = "Container News"
EC = "European Commission, DG TAXUD"

S2 = {
    # ---------------- geopolitics & policy
    "eam_apec": (EAM, "Weekly headlines: Shenzhen summit; Yemen; Bahrain", "20 Nov 2026", "https://enterpriseam.com/egypt/2026/11/20/a-misr-life-float-an-egp-8-5k-wage-floor-and-ai-data-centers/"),
    "ustr_call": ("USTR", "Readout of Greer's call with Vice Premier He Lifeng", "6 Nov 2026", "https://ustr.gov/about/policy-offices/press-office/press-releases/2026/november/readout-ambassador-greers-call-chinas-vice-premier-he-lifeng"),
    "fr_api": ("Federal Register", "Document search, 13–22 Nov: no Section 301 maritime notice", "searched 22 Nov 2026", "https://www.federalregister.gov/api/v1/documents.json"),
    "fr_chips": ("Federal Register (BIS)", "Addressing Remote Access to Advanced Semiconductors (91 FR 74970)", "19 Nov 2026", "https://www.federalregister.gov/documents/2026/11/19/2026-23529/addressing-remote-access-to-advanced-semiconductors"),
    "fr_portfee": ("Federal Register (USTR)", "Section 301 maritime action: fee suspension to 9 Jan (91 FR 72608)", "10 Nov 2026", "https://www.federalregister.gov/documents/2026/11/10/2026-22867/notice-of-modification-of-section-301-action-chinas-targeting-of-the-maritime-logistics-and"),
    "gc_truce": (GC + " / Reuters", "China Extends US Trade Truce by Two Months", "9 Nov 2026", "https://gcaptain.com/china-extends-us-trade-truce-by-two-months/"),
    "ustr_wsj": ("USTR", "Greer letter to the Wall Street Journal on tariffs", "16 Nov 2026", "https://ustr.gov/about/policy-offices/press-office/press-releases/2026/november/ambassador-greer-pens-letter-editor-wall-street-journal-how-tariffs-are-advancing-americans-long"),
    "ustr_agoa": ("USTR", "Intent to remove Rwanda and South Africa from AGOA", "2 Nov 2026", "https://ustr.gov/about/policy-offices/press-office/press-releases/2026/november/ambassador-greer-issues-statement-president-trumps-intent-terminate-rwanda-and-south-africa-agoa"),
    "gc_sts": (GC + " / Reuters", "U.S. Targets Ship-to-Ship Transfers in Expanded Iran Maritime Blockade", "18 Nov 2026", "https://gcaptain.com/u-s-targets-ship-to-ship-transfers-in-expanded-iran-maritime-blockade/"),
    "gc_sts_olym": (GC + " / Bloomberg", "Iranian Oil Transferred Between Tankers as US Widens Blockade", "20 Nov 2026", "https://gcaptain.com/iranian-oil-transferred-between-tankers-as-us-widens-blockade/"),
    "gc_treasury": (GC + " / Reuters", "US Treasury Presses Singapore and Malaysia on Iran Sanctions Compliance", "20 Nov 2026", "https://gcaptain.com/us-treasury-presses-singapore-and-malaysia-on-iran-sanctions-compliance/"),
    "gc_qeshm": (GC + " / Bloomberg", "U.S. Military Strikes Iranian Missile Site Near Strait of Hormuz", "17 Nov 2026", "https://gcaptain.com/u-s-military-strikes-iranian-missile-site-near-strait-of-hormuz/"),
    "gc_betul": (GC, "Cargo Ship Capsizes Off Bulgaria After Reported Sea Drone Attack", "16 Nov 2026", "https://gcaptain.com/cargo-ship-capsizes-off-bulgaria-after-reported-sea-drone-attack/"),
    "gc_gashusky": (GC + " / Reuters", "LPG Tanker Reported to Have Sunk Off Bulgaria's Black Sea Coast", "17 Nov 2026", "https://gcaptain.com/lpg-tanker-reported-to-have-sunk-off-bulgarias-black-sea-coast/"),
    "gc_sulina": (GC + " / Reuters", "Three Ships Struck By Drones In Black Sea Near Romanian Shipping Canal", "15 Nov 2026", "https://gcaptain.com/three-ships-struck-by-drones-in-black-sea-near-romanian-shipping-canal/"),
    "gc_sparta": (GC, "Russian Military-Linked Cargo Ship Burns After Suspected Drone Strike in Gulf of Finland", "21 Nov 2026", "https://gcaptain.com/russian-military-linked-cargo-ship-burns-after-suspected-drone-strike-in-gulf-of-finland/"),
    "gc_eusanc": (GC, "EU Targets Shadow Fleet Shipowners, Managers and Insurers in New Russia Sanctions", "16 Nov 2026", "https://gcaptain.com/eu-targets-shadow-fleet-shipowners-managers-and-insurers-in-new-russia-sanctions/"),
    "ec_cbam_ded": (EC, "CBAM: rules on carbon prices paid outside the EU", "16 Nov 2026", "https://taxation-customs.ec.europa.eu/news/cbam-commission-adopts-rules-recognition-carbon-prices-paid-non-eu-countries-2026-11-16_en"),
    "ec_cbam_no": (EC, "Extension of CBAM to Iceland and Norway", "18 Nov 2026", "https://taxation-customs.ec.europa.eu/news/extension-cbam-iceland-and-norway-2026-11-18_en"),
    "ec_ets_uk": (EC, "EU and UK agree to link Emission Trading Systems (ETS)", "20 Nov 2026", "https://taxation-customs.ec.europa.eu/news/eu-and-uk-agree-link-emission-trading-systems-ets-2026-11-20_en"),
    "ec_euca": (EC, "EU Customs Authority holds first management board meeting in Lille", "20 Nov 2026", "https://taxation-customs.ec.europa.eu/news/eu-customs-authority-holds-first-management-board-meeting-lille-2026-11-20_en"),
    "ec_cbam_price": (EC, "Price of CBAM certificates", "accessed 16 Nov 2026", "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en"),
    "eam_scrap": (EAM, "Brussels weighs a bidding ban; Egypt off the scrap list", "22 Nov 2026", "https://enterpriseam.com/egypt/2026/11/22/brussels-weighs-a-bloc-wide-bidding-ban-for-foreign-firms-caught-with-distortive-subsidies/"),
    "wto_mon": ("WTO", "New trade-restrictive measures surge but WTO members step up trade facilitation efforts", "17 Nov 2026", "https://www.wto.org/english/news_e/news26_e/tmwto_17nov26_552_e.htm"),
    "wto_ctg": ("WTO", "Goods Council agrees to modernize notification reporting, reviews trade concerns", "16 Nov 2026", "https://www.wto.org/english/news_e/news26_e/good_16nov26_556_e.htm"),
    # ---------------- Egypt & region
    "eam_rebate": (EAM, "Export rebates up 35%; state pays up to half the freight to new markets", "8 Nov 2026", "https://enterpriseam.com/egypt/2026/11/08/the-government-is-raising-export-rebates-by-an-average-of-35-and-picking-up-as-much-as-half-the-freight-bill-to-new-markets/"),
    "eam_briefing": (EAM, "Happening today: the exporter rebate briefing", "15 Nov 2026", "https://enterpriseam.com/egypt/2026/11/15/egypts-final-imf-review-moves-to-virtual-talks-with-usd-2-3-bn-at-stake-and-a-15-december-deadline/"),
    "eam_imf": (EAM, "IMF staff-level agreement on the final review: up to USD 2.3 bn", "19 Nov 2026", "https://enterpriseam.com/egypt/2026/11/19/imf-staff-and-the-government-reached-agreement-on-the-final-review-putting-up-to-usd-2-3-bn-on-the-table-before-the-program-expires/"),
    "zw_imf": (ZW + " / Arab Finance", "IMF, Egypt reach staff-level agreement on 8th and final EFF review", "19 Nov 2026", "https://www.zawya.com/en/economy/imf-egypt-reach-staff-level-agreement-on-8th-and-final-eff-review-2392984"),
    "eam_gs": (EAM, "Goldman expects CBE to hold at 20% until late 1Q", "22 Nov 2026", "https://enterpriseam.com/egypt/2026/11/22/goldman-sachs-expects-cbe-to-hold-at-20-until-late-1q-then-cut-by-700-bps-through-2028/"),
    "zw_egp": (ZW + " (Arabic)", "The dollar back above EGP 54 (Arabic)", "22 Nov 2026", "https://www.zawya.com/ar/%D8%A7%D9%84%D8%A3%D8%B3%D9%88%D8%A7%D9%82/%D8%B9%D9%85%D9%84%D8%A7%D8%AA/%D9%85%D8%B5%D8%B1-%D8%A7%D9%84%D8%AF%D9%88%D9%84%D8%A7%D8%B1-%D9%8A%D8%B9%D9%88%D8%AF-%D9%84%D9%84%D8%A7%D8%B1%D8%AA%D9%81%D8%A7%D8%B9-%D9%81%D9%88%D9%82-54-%D8%AC%D9%86%D9%8A%D9%87-%D9%85%D8%B9-%D8%A8%D8%AF%D8%A7%D9%8A%D8%A9-%D8%A7%D9%84%D8%A3%D8%B3%D8%A8%D9%88%D8%B9-2442943"),
    "eam_db": (EAM, "Deutsche Bank sees EGP at 48–60 (CBE quote 12 Nov)", "16 Nov 2026", "https://enterpriseam.com/egypt/2026/11/16/deutsche-bank-research-sees-egp-at-48-60-depending-on-the-iran-war-expects-cbe-to-hold-rates-into-next-year/"),
    "eam_noimf": (EAM, "Egypt may not need a new IMF facility (reserves)", "22 Nov 2026", "https://enterpriseam.com/egypt/2026/11/22/egypt-may-not-need-a-new-imf-facility-but-we-still-have-plenty-of-work-to-do-on-the-fiscal-side-of-the-house/"),
    "zw_deficit": (ZW + " / Arab Finance", "Egypt's trade deficit widens 60.6% in September 2026", "19 Nov 2026", "https://www.zawya.com/en/economy/egypts-trade-deficit-widens-60.6-in-september-2026-2392989"),
    "zw_africa": (ZW + " / Daily News Egypt", "Egypt's trade with African Union countries rises by $1.1bln to $8.2bln in 9M 2026", "19 Nov 2026", "https://www.zawya.com/en/economy/egypts-trade-with-african-union-countries-rises-by-1.1bln-to-8.2bln-in-9m-2026-2377014"),
    "zw_libya": (ZW + " / Arab Finance", "Egypt, Libya sign agreements on gas infrastructure, fisheries and labor", "20 Nov 2026", "https://www.zawya.com/en/projects/commodities/egypt-libya-sign-agreements-on-gas-infrastructure-fisheries-and-labor-2416449"),
    "eam_backsuez": (EAM, "Majid Al Futtaim taps DP World for Egyptian produce", "17 Nov 2026", "https://enterpriseam.com/egypt/2026/11/17/majid-al-futtaim-taps-dp-world-to-move-egyptian-fresh-produce-onto-uae-shelves/"),
    "gc_dhl_suez": (GC, "Suez Canal Return Won't Resolve Global Shipping Congestion, DHL Warns", "16 Nov 2026", "https://gcaptain.com/suez-canal-return-wont-resolve-global-shipping-congestion-dhl-warns/"),
    "cn_reliab": (CN, "Red Sea returns are rewriting carrier reliability, not just transit times", "19 Nov 2026", "https://container-news.com/red-sea-returns-are-rewriting-carrier-reliability-not-just-transit-times/"),
    "zw_gdp": (ZW + " / Arab Finance", "Egypt's economy grows 4.9% in Q1 FY 2026/27", "19 Nov 2026", "https://www.zawya.com/en/economy/egypts-economy-grows-4.9-in-q1-fy-202627-2356705"),
    "cn_yangming": (CN, "Yang Ming expands Egypt coverage through DP World slot-sharing deal", "15 Nov 2026", "https://container-news.com/yang-ming-expands-egypt-coverage-through-dp-world-slot-sharing-deal/"),
    "cn_sidra": (CN, "Sidra Line revises Mediterranean–West Africa service", "22 Nov 2026", "https://container-news.com/sidra-line-revises-mediterranean-west-africa-service/"),
    "eam_mesco": (EAM, "EBRD lends Mesco EGP 585 mn", "19 Nov 2026", "https://enterpriseam.com/egypt/2026/11/19/ebrd-lends-mesco-egp-585-mn-and-takes-half-the-risk-on-egp-500-mn-tube-loan/"),
    "cn_msc_redsea": (CN, "MSC to launch new North India–Red Sea container service", "15 Nov 2026", "https://container-news.com/msc-to-launch-new-north-india-red-sea-container-service/"),
    "eam_whosail": (EAM + " Infrastructure", "Who's still sailing?", "19 Nov 2026", "https://enterpriseam.com/infrastructure/2026/11/19/whos-still-sailing/"),
    "eam_india": (EAM, "Egypt and India target USD 12 bn in trade by 2030", "17 Nov 2026", "https://enterpriseam.com/egypt/2026/11/17/egypt-and-india-target-usd-12-bn-in-trade-by-2030-and-agree-to-explore-a-free-trade-agreement/"),
    "zw_china": (ZW + " / Daily News Egypt", "Egypt-China trade reaches $20bln, Chinese investment exceeds $10bln: Farid", "17 Nov 2026", "https://www.zawya.com/en/economy/belt-road-initiative-bri/egypt-china-trade-reaches-20bln-chinese-investment-exceeds-10bln-farid-2301600"),
    "eam_fert": (EAM, "Fertilizer producers pay 50% more for gas and keep exporting", "16 Nov 2026", "https://enterpriseam.com/egypt/2026/11/16/fertilizer-producers-pay-50-more-for-gas-and-keep-exporting-as-lng-costs-outrun-urea-prices/"),
    "eam_issc": (EAM, "Carbon checks, done at home: Damietta's ISSC accredited under CBAM", "18 Nov 2026", "https://enterpriseam.com/egypt/2026/11/18/etisalat-business-plans-gpu-rentals-in-egypt-as-chipverse-raises-funds-to-double-capacity/"),
    "eam_wage": (EAM, "Private-sector minimum wage EGP 8.5k from January", "16 Nov 2026", "https://enterpriseam.com/egypt/2026/11/16/the-headlines-from-this-morning-22/"),
    "eam_amea": (EAM, "Amea Power inks deals for USD 650 mn Ras Shukeir wind farm and USD 200 mn turbine factory with Chinese partners", "19 Nov 2026", "https://enterpriseam.com/egypt/2026/11/19/amea-power-inks-deals-for-usd-650-mn-ras-shukeir-wind-farm-and-usd-200-mn-turbine-factory-with-chinese-partners/"),
    "zw_saudi": (ZW + " / Saudi Gazette", "Saudi transport and storage registrations rise 31% to 185,554 in Q3 2026", "17 Nov 2026", "https://www.zawya.com/en/business/saudi-transport-and-storage-registrations-rise-31-to-185554-in-q3-2026-2310742"),
}
SOURCES = {**S1, **S2}


def _timeline():
    W, H = 680, 150
    x0, x1, axis = 20, 655, 76
    days = 48  # 23 Nov -> 10 Jan
    ev = [(7, "30 Nov", "IMO MEPC 85 opens", 1), (8, "1 Dec", "December FAKs; Hapag-Lloyd 2027 fuel rates", -1),
          (11, "4 Dec", "Gemini NE1 via Suez · NZF vote (tbc)", 2), (22, "15 Dec", "Egypt IMF programme expires", -2),
          (24, "17 Dec", "CBE rate decision", 1), (38, "31 Dec", "Rebate phase one ends", -1),
          (39, "1 Jan", "Min. wage EGP 8.5k · CBAM Norway", 2), (47.5, "9–10 Jan", "US port-fee pause & China truce end", -2)]
    ly = {1: 44, 2: 14, -1: 102, -2: 130}
    g = ('<linearGradient id="tlg" x1="0" y1="0" x2="1" y2="1">' + "".join(f'<stop offset="{o}%" stop-color="{c}"/>' for c, o in
         [("#A88329", 0), ("#C09934", 17), ("#DEC163", 33), ("#F7E590", 50), ("#DEC161", 67), ("#C29B36", 83), ("#A88228", 100)]) + "</linearGradient>")
    out = [f'<defs>{g}</defs>', f'<line x1="{x0}" y1="{axis}" x2="{x1}" y2="{axis}" stroke="#1b2333" stroke-width="1.4"/>']
    for m, lab in ((0, "NOV"), (8, "DEC"), (39, "JAN")):
        x = x0 + (x1 - x0) * m / days
        out.append(f'<text x="{x}" y="{axis+12}" font-family="IBM Plex Mono" font-size="7.5" fill="#5d6577" letter-spacing="1.5">{lab}</text>')
    for d, date, label, lv in ev:
        x = x0 + (x1 - x0) * d / days
        y = ly[lv]
        anchor = "end" if x > 520 else "start"
        dx = -4 if anchor == "end" else 4
        y_end = y + 14 if lv > 0 else y - 11
        out.append(f'<line x1="{x:.1f}" y1="{axis}" x2="{x:.1f}" y2="{y_end}" stroke="#c9b98f" stroke-width=".8"/>')
        out.append(f'<circle cx="{x:.1f}" cy="{axis}" r="5" fill="url(#tlg)" stroke="#1b2333" stroke-width=".8"/>')
        out.append(f'<text x="{x+dx:.1f}" y="{y}" text-anchor="{anchor}" font-family="IBM Plex Mono" font-weight="600" font-size="8.4" fill="#8a6514">{date}</text>')
        out.append(f'<text x="{x+dx:.1f}" y="{y+11}" text-anchor="{anchor}" font-family="Inter" font-size="8.6" fill="#1b2333">{label}</text>')
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" style="display:block;overflow:visible">{"".join(out)}</svg>'


TIMELINE = _timeline()

cover = {
    "kicker": "Cover story · The Red Sea",
    "headline": "The ships come back. So does the risk.",
    "deck": "Gemini sends its last three North Europe loops back through Suez, just as the Houthis take Yemen's Red Sea coast and threaten Saudi ports. Asia–Med was the only main container lane to rise last week. Sixteen pages on what that means for cargo that touches Egypt.",
    "standfirst": "Drewry counted 57 container ships through the Suez Canal in the week to 15 November, up 73% on a year earlier, and Maersk and Hapag-Lloyd will move three more Asia–Europe services to the canal from 4 December. In the same week Far East–Mediterranean spot rates rose 6.8% to $4,989 a box while every other main lane fell, and Red Sea transits at Bab el-Mandeb dropped 28% from their October peak.",
    "src": ["drewry_redsea", "cn_gemini", "xeneta20", "gc_houthi"],
    "contents": [
        {"p": "02", "sec": "The briefing", "what": "60 seconds · market dashboard"},
        {"p": "03", "sec": "Ocean freight", "what": "the Med premium · December tariffs"},
        {"p": "04", "sec": "Suez, Red Sea & Hormuz", "what": "ships return, risk rises"},
        {"p": "05", "sec": "Carriers & costs", "what": "fuel · reliability · carbon"},
        {"p": "06", "sec": "Air cargo", "what": "Middle East lanes lead"},
        {"p": "07", "sec": "The logistics business", "what": "liability · deals · e-commerce"},
        {"p": "08", "sec": "Geopolitics & trade policy", "what": "no deal in Shenzhen"},
        {"p": "09", "sec": "War, sanctions & carbon", "what": "Black Sea · CBAM · WTO"},
        {"p": "10", "sec": "Egypt desk", "what": "IMF deal · trade · the pound"},
        {"p": "11", "sec": "Egypt & the region", "what": "ports · fertiliser · partners"},
        {"p": "12", "sec": "The toolkit", "what": "Red Sea clauses for December"},
        {"p": "13", "sec": "Calendar & glossary", "what": "dates to diarise"},
        {"p": "14", "sec": "Sources", "what": "every figure, footnoted (pp. 14–15)"},
        {"p": "16", "sec": "About Rockit", "what": "services · offices · tools"},
    ],
    "status_asof": "as reported 16–22 Nov 2026",
    "status": [
        {"name": "Suez Canal", "state": "open", "label": "Returning", "note": "57 container transits in the week to 15 Nov (+73% y/y); Gemini NE1–NE3 follow from 4 Dec.", "src": ["drewry_redsea", "cn_gemini"]},
        {"name": "Bab el-Mandeb", "state": "restricted", "label": "Risk rising", "note": "Houthis hold Yemen's Red Sea coast (Reuters); transits 11.9 a day, down from 16.6.", "src": ["gc_houthi", "xeneta20"]},
        {"name": "Saudi Red Sea ports", "state": "partial", "label": "Threatened", "note": "Houthis told ships to leave on 20 Nov; no attack on a ship there verified.", "src": ["gc_houthi"]},
        {"name": "Strait of Hormuz", "state": "restricted", "label": "Restricted", "note": "115 out / 148 in a week; six verified attacks; JMIC threat SEVERE.", "src": ["gc_hormuz20"]},
        {"name": "Western Black Sea", "state": "restricted", "label": "Attacks", "note": "Wheat ship bound for Egypt capsized off Bulgaria on 16 Nov after a reported drone strike.", "src": ["gc_betul"]},
    ],
    "numbers": [
        {"value": "$4,989", "label": "Far East → Med spot per 40ft (+6.8%)", "src": ["xeneta20"]},
        {"value": "$1,551", "label": "Med premium over North Europe", "src": ["xeneta20"]},
        {"value": "57", "label": "container ships through Suez in a week (+73%)", "src": ["drewry_redsea"]},
        {"value": "$3.45/kg", "label": "global air rate, +31% y/y", "src": ["st_wcd45"]},
        {"value": "$2.3bn", "label": "IMF money agreed for Egypt, pending Board", "src": ["eam_imf"]},
    ],
}

# ------------------------------------------------------------------ page 2: briefing
p_brief = {"section": "The briefing", "title": "The briefing", "label": "If you read one page, read this", "blocks": [
    {"k": "grid", "cols": "1.22fr 1fr", "gap": "8mm", "columns": [[
        {"k": "kicker", "text": "From the desk"},
        P("Welcome to Voyage 002 of *The Rockit Manifest*, our Monday review for exporters, importers, manufacturers and fellow forwarders who move cargo through Egypt. Last week we promised four follow-ups: December rates, APEC in Shenzhen, the IMO carbon vote and the rebate briefing. All four are inside, including where we could not verify what was said.", cls="drop"),
        P("Every figure is footnoted to the page we read it on. Where a claim comes from one side of a conflict, we say so. *Why it matters* and *Rockit's read* are our analysis, kept apart from the reporting. — **The Rockit desk, Cairo**"),
        {"k": "kicker", "text": "The week in 60 seconds"},
        {"k": "ticks", "items": [
            "**Ocean:** Asia–Med was the only main lane to rise: Xeneta +6.8% to $4,989 per 40ft, Drewry Shanghai–Genoa +6% to $4,436. Maersk's $1,500 Med peak surcharge applies from today.",
            "**December:** MSC, Hapag-Lloyd and CMA CGM have filed $6,500–6,800 per 40ft for Asia to the East Med.",
            "**Red Sea:** Gemini moves three more loops to Suez from 4 Dec, but the Houthis now hold Yemen's Red Sea coast and told ships to leave Saudi ports.",
            "**Hormuz:** transits fell again to 115 out / 148 in; attacks worldwide were the highest since mid-October.",
            "**Air:** global rates $3.45/kg, +31% y/y; Middle East–Europe +66%; Saudi air tonnage down a third.",
            "**Policy:** no verified trade deal came out of Shenzhen, so the 9–10 January deadlines stand.",
            "**Egypt:** IMF staff-level deal puts about $2.3bn on the table before 15 December; September imports +29.7%.",
            "**Money:** CBE deposit rate 20.0%; the dollar back above EGP 54 on 22 Nov; Goldman sees a hold until late Q1.",
        ], "srcs": [["xeneta20", "drewry", "cn_asiamed"], ["cn_msc_fak", "cn_hapag_fak", "cn_cma_dec"], ["cn_gemini", "gc_houthi"], ["gc_hormuz20"],
                    ["st_wcd45"], ["eam_apec", "fr_api"], ["eam_imf", "zw_deficit"], ["eam_gs", "zw_egp"]]},
    ], [
        {"k": "box", "kicker": "Rockit's read", "title": "Three moves for this week", "blocks": [
            {"k": "ticks", "items": [
                "**Importing from Asia?** Spot to the Med is rising towards December's tariffs. Book early in December, and get the peak, fuel, piracy and Suez surcharges named in writing.",
                "**Shipping to or via Saudi Red Sea ports?** Ask your carrier what happens to your box if Jeddah calls are suspended, and confirm war-risk cover on the Red Sea leg.",
                "**Signing 2027 contracts?** Wait for Hapag-Lloyd's Suez-based fuel rates on 1 December and the IMO decision on 4 December before you fix fuel and carbon terms.",
            ]},
        ]},
        {"k": "space", "mm": 4},
        {"k": "panel", "kicker": "How to read this issue", "blocks": [
            P("Small gold numbers after a sentence point to the numbered source list on pages 14–15. Spot indices are market averages, not quotations. Tariffs (FAK) are carriers' published base rates, before local charges."),
            P("Dashboard colours show cost to you: red costs you more, green costs you less, grey is context."),
        ]},
    ]]},
    {"k": "rule"},
    {"k": "kicker", "text": "Market dashboard · latest readings"},
    {"k": "tiles", "cols": 4, "items": [
        {"value": "$4,176", "label": "Drewry WCI composite, per 40ft", "delta": "▼ 3% w/w", "dir": "down", "asof": "19 Nov", "src": ["drewry"]},
        {"value": "$4,989", "label": "Far East → Med spot (Xeneta), per 40ft", "delta": "▲ 6.8% w/w", "dir": "up", "asof": "19 Nov", "src": ["xeneta20"]},
        {"value": "$4,436", "label": "Drewry Shanghai → Genoa, per 40ft", "delta": "▲ 6% w/w", "dir": "up", "asof": "19 Nov", "src": ["drewry"]},
        {"value": "$838", "label": "VLSFO per tonne, Global 20 Ports average", "delta": "▼ $25.50", "dir": "down", "asof": "20 Nov", "src": ["sb_prices"]},
        {"value": "$3.45/kg", "label": "WorldACD global air rate", "delta": "▲ 2% w/w · +31% y/y", "dir": "up", "asof": "week 45", "src": ["st_wcd45"]},
        {"value": "115 / 148", "label": "Hormuz transits out / in, a week", "delta": "was 139 / 169", "dir": "flat", "asof": "UKMTO, 20 Nov", "src": ["gc_hormuz20"]},
        {"value": "57", "label": "Suez container transits, week to 15 Nov", "delta": "▲ 73% y/y", "dir": "flat", "asof": "Drewry", "src": ["drewry_redsea"]},
        {"value": "54+", "label": "EGP per USD in bank trading", "delta": "CBE quote 53.39 on 12 Nov", "dir": "up", "asof": "22 Nov", "src": ["zw_egp", "eam_db"]},
    ]},
]}

# ------------------------------------------------------------------ geopolitics & policy
p_geo = {"section": "Geopolitics & trade policy", "title": "Geopolitics & trade policy", "label": "Shenzhen · the January cliff", "blocks": [
    {"k": "grid", "cols": "1.15fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "Washington & Beijing", "head": "A summit, a declaration, no trade deal we could verify",
         "deck": "We promised to report what came out of APEC in Shenzhen. On trade, nothing we could read on a primary or reliable page.",
         "text": [
             "EnterpriseAM reports that Presidents Trump, Xi and Putin met in Shenzhen in the first trilateral summit of its kind. The 90-minute talks ended with a joint declaration that “nuclear war cannot be won and must never be fought” and a pledge to raise output of refined petroleum products. Wire coverage of the summit was not reachable from our desk, so this is our only account of it.",
             "We found no change to tariffs, to the US port fees on Chinese ships, or to China's rare-earth waivers. A search of the Federal Register for 13–22 November returned no new Section 301 maritime notice. The last primary US statement is USTR's readout of a 6 November call in which Ambassador Greer and Treasury Secretary Bessent pressed Vice Premier He Lifeng to “fully implement” commitments on farm purchases, rare earths and critical minerals.",
             "Washington did act on technology. A Commerce Department rule effective 19 November requires licences for advanced chips shipped to Indonesia, Malaysia, Singapore, Thailand and Brazil, restricts remote computing for China-linked firms, and warns of “import restrictions” for countries that tolerate evasion. USTR's Greer wrote on 16 November that 19 trading partners, nearly 40% of world GDP, have signed deals with the US.",
         ], "src": ["eam_apec", "fr_api", "ustr_call", "fr_chips", "ustr_wsj"],
         "why": "Until an official notice says otherwise, US-lane and Asia-lane quotes that run past 9 January need a reopener clause. Shipments of servers or GPUs routed via Southeast Asian hubs face end-user checks."},
    ], [
        {"k": "table", "caption": "Policy tracker · as of 22 November", "head": ["Issue", "Status", "Next date"],
         "rows": [
             {"cells": ["US port fees on Chinese ships (Section 301)", "Suspended; no change found", "9 Jan 2027"], "src": ["fr_portfee", "fr_api"]},
             {"cells": ["China's 24% extra tariff on US goods", "Suspended; no change verified", "10 Jan 2027"], "src": ["gc_truce"]},
             {"cells": ["US chip licences: ID, MY, SG, TH, BR", "In force (interim rule)", "19 Nov 2026"], "src": ["fr_chips"]},
             {"cells": ["AGOA: Rwanda and South Africa", "US intends removal", "1 Jan 2027"], "src": ["ustr_agoa"]},
             {"cells": ["IMO Net-Zero Framework", "Vote pencilled", "4 Dec (tbc)"], "src": ["imo_cal"]},
             {"cells": ["EU CBAM in Norway & Iceland", "Agreed", "1 Jan 2027"], "src": ["ec_cbam_no"]},
             {"cells": ["Strait of Hormuz", "Restricted; talks stalled", "No date"], "src": ["gc_hormuz20", "gc_qeshm"]},
         ]},
        {"k": "panel", "kicker": "The Iran war", "title": "Blockade widens, talks stall", "blocks": [
            P("US Central Command said on 18 November that ships taking Iranian cargo by ship-to-ship transfer “may be stopped, boarded, diverted, captured”, even outside Iranian waters. US warplanes struck an IRGC missile site on Qeshm Island on 17 November, a US official told Bloomberg; Iran's Mehr agency reported no casualties. Treasury officials pressed Singapore and Malaysia on sanctions compliance. Qatar is still mediating, and Bloomberg reports neither side willing to compromise.", ["gc_sts", "gc_qeshm", "gc_treasury"]),
        ]},
    ]]},
    {"k": "rule"},
    {"k": "kicker", "text": "Seven weeks to the January cliff · key dates from this issue"},
    {"k": "html", "html": TIMELINE},
    {"k": "p", "text": "Sources: IMO; Container News; Ship & Bunker; EnterpriseAM; European Commission; Federal Register; Reuters via gCaptain. Full references on pages 14–15.", "src": ["imo_cal", "cn_msc_fak", "sb_hapag_mfs", "cn_gemini", "eam_imf", "eam_gs", "eam_rebate", "eam_wage", "ec_cbam_no", "fr_portfee", "gc_truce"], "cls": "srcline"},
]}

# ------------------------------------------------------------------ war, sanctions & carbon
p_war = {"section": "Geopolitics & trade policy", "title": "War, sanctions & carbon", "label": "Geopolitics · continued", "blocks": [
    {"k": "grid", "cols": "1fr 1.15fr", "gap": "9mm", "style": "margin-bottom:3mm", "columns": [[
        {"k": "chart", "type": "vbar", "width_mm": 72, "height_mm": 36, "min": 0, "max": 360, "dp": 0, "kind": "gold",
         "sub": "WTO · new trade-restrictive measures", "title": "Restrictions at a record",
         "rows": [["All of 2025", 300], ["H1 2026", 333]],
         "note": "Import restrictions in force now cover $5.4tn, 21.3% of world imports: the highest since monitoring began in 2009.", "src": ["wto_mon"]},
    ], [
        {"k": "kicker", "text": "The week in four numbers"},
        {"k": "tiles", "cols": 2, "items": [
            {"value": "17", "label": "ships attacked off Bulgaria and Romania since mid-July", "asof": "Diaplous via Reuters", "src": ["gc_gashusky"]},
            {"value": "113", "label": "people and entities added to EU Russia sanctions (12 + 101)", "asof": "16 Nov", "src": ["gc_eusanc"]},
            {"value": "10%", "label": "cap on international credits in CBAM carbon-price deductions", "asof": "Reg. 2026/2498", "src": ["ec_cbam_ded"]},
            {"value": "$5.4tn", "label": "world imports under restrictions (21.3%)", "asof": "WTO, 17 Nov", "src": ["wto_mon"]},
        ]},
    ]]},
    {"k": "flow", "n": 2, "blocks": [
        brief("Black Sea", "A wheat ship bound for Egypt sinks", "The *BETUL 8*, carrying almost 3,000 tonnes of wheat from Tulcea in Romania to Egypt, capsized off Bulgaria on 16 November; crew told Bulgarian media it was hit by two sea drones. All 12 were rescued and no one has been officially blamed. The LPG tanker *GAS HUSKY* sank off Bulgaria the next day.", ["gc_betul", "gc_gashusky"],
              "The Romanian and Bulgarian coastal route, Egypt's safer alternative to Odesa, is now in the line of fire. Expect higher war-risk premiums on Danube and Constanța loadings."),
        brief("Sanctions", "EU targets the shadow fleet's managers", "On 16 November the EU listed 12 people and 101 entities, including ship managers and traders in the UAE, Oman, Seychelles and China, a Dubai network, and Moscow's Balance Insurance; gCaptain reports nearly 50 Russian banks were added as well. ", ["gc_eusanc"],
              "Several listed managers sit in Dubai, a common counterparty hub. Run KYC on UAE ship managers and insurers for any EU-linked cargo."),
        brief("Carbon · EU", "CBAM credit for carbon paid abroad, but not for Egypt", "Commission Regulation 2026/2498 (16 November) lets importers deduct carbon prices effectively paid outside the EU, with international credits capped at 10%. CBAM extends to Norway and Iceland from 1 January 2027, and the EU and UK agreed on 20 November to link their emissions trading systems, paving the way for mutual CBAM exemption.", ["ec_cbam_ded", "ec_cbam_no", "ec_ets_uk"],
              "Egypt has no national carbon price, so its steel, aluminium, fertiliser and cement exporters get no deduction, while UK rivals move towards exemption."),
        brief("Scrap", "Egypt left off the EU's draft scrap list", "EnterpriseAM reports that the Commission's September draft list of non-OECD countries allowed to receive EU metal scrap leaves Egypt out; exports to unlisted countries would be banned from 21 May 2027. Cairo is lobbying to be added.", ["eam_scrap"],
              "The EU supplies about half of Egypt's ferrous scrap, per EnterpriseAM's sources. A ban would reshape bulk imports into Alexandria and Damietta."),
        brief("Customs", "The EU's new customs authority meets", "The EU Customs Authority held its first management board in Lille on 19 November. It will run EU-wide risk analysis and the Customs Data Hub that replaces more than 100 national systems, starting in 2027.", ["ec_euca"],
              "EU-level risk targeting will make HS codes and product data on Egyptian export filings matter more."),
    ]},
]}

# ------------------------------------------------------------------ Egypt desk
p_egypt = {"section": "Egypt desk", "title": "Egypt desk", "label": "IMF · rebates · trade · the pound", "blocks": [
    {"k": "grid", "cols": "1.15fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "The economy", "head": "The IMF deal lands before the deadline",
         "deck": "Staff agreed the final reviews on 18 November. About $2.3bn now needs only the Board's signature before 15 December.",
         "text": [
             "The IMF and Egypt reached staff-level agreement on the eighth and final review of the Extended Fund Facility and the third review of the Resilience and Sustainability Facility. If the Executive Board approves before the programme expires on 15 December, Egypt receives about $1.5bn under the EFF and up to about $0.8bn under the RSF, bringing total disbursements to about $9.6bn.",
             "Goldman Sachs expects the CBE to hold at 20% until late Q1 2027, and sees the pound at 53, 52 and 50 per dollar over three, six and twelve months. In bank trading the dollar rose back above EGP 54 on 22 November; the last CBE quote we could read was 53.39 on 12 November. Net reserves were $57.5bn at end-October.",
             "CAPMAS data show September imports up 29.7% to $10.6bn and exports up 7.4% to $5.3bn; the deficit widened 60.6% to $5.3bn.",
         ], "src": ["eam_imf", "zw_imf", "eam_gs", "zw_egp", "eam_db", "eam_noimf", "zw_deficit"],
         "why": "The IMF deal removes last week's biggest FX risk, but the Fund wants the pound to move with shocks, not be held flat. Keep FX clauses in freight quotes and expect a 53–55 working range."},
    ], [
        {"k": "chart", "type": "hbar", "width_mm": 68, "max": 1.4, "prefix": "$", "suffix": "bn", "dp": 1,
         "sub": "CAPMAS · exports to African Union, Jan–Sep 2026", "title": "Where Egypt sells in Africa",
         "rows": [["Libya", 1.2, "gold"], ["Sudan", 0.9, "gold"], ["Morocco", 0.7, "spot"], ["Algeria", 0.7, "spot"], ["Tunisia", 0.4, "spot"]],
         "note": "Total trade with AU countries $8.2bn (+15.3%); exports $6.1bn (+8.5%). Africa is a 50%-freight-support market.", "src": ["zw_africa"]},
        {"k": "kicker", "text": "Trade & money"},
        {"k": "tiles", "cols": 2, "items": [
            {"value": "$5.3bn", "label": "trade deficit, September (+60.6%)", "asof": "CAPMAS", "src": ["zw_deficit"]},
            {"value": "+29.7%", "label": "imports, September ($10.6bn)", "asof": "CAPMAS", "src": ["zw_deficit"]},
            {"value": "~$2.3bn", "label": "IMF EFF + RSF money pending Board approval", "asof": "before 15 Dec", "src": ["eam_imf"]},
            {"value": "+47.5%", "label": "Suez Canal activity, Jul–Sep vs a year earlier", "asof": "GDP +4.9%", "src": ["zw_gdp"]},
        ]},
    ]]},
    {"k": "rule"},
    {"k": "grid", "cols": "1.1fr 1fr", "gap": "9mm", "columns": [[
        {"k": "box", "kicker": "Export rebates · our promised follow-up", "title": "What we can confirm, and what we can't", "blocks": [
            P("The Finance and Investment ministries briefed exporters on the revamped rebate programme on 15 November as scheduled. We could not read any report of what was said there: every outlet that covered it was unreachable from our desk, so we are not repeating figures we only saw in search snippets.", ["eam_briefing"]),
            P("The rules on record are unchanged: rebates up 35% on average from November shipments; the state pays 50% of sea and land freight to Africa, Latin America, Australia, Southeast Asia and Russia; 25% of air freight to Europe and 50% to the UK for agricultural exports; 25% of domestic transport, cargo insurance and express-vessel invoices. Files must be complete before they are accepted. The FY 2026/27 budget sets aside EGP 48bn.", ["eam_rebate"]),
        ]},
    ], [
        {"k": "kicker", "text": "What the rules mean for your paperwork"},
        {"k": "ticks", "items": [
            "Freight invoice, B/L and insurance certificate in the exporter's name, dated and itemised.",
            "Inland trucking invoice kept separately (a 25% line of its own).",
            "Shipments since 1 November qualify; phase one ends 31 December.",
            "Payment timing has not been published on any page we could read.",
        ], "srcs": [["eam_rebate"], ["eam_rebate"], ["eam_rebate"], ["eam_rebate"]]},
    ]]},
]}

# ------------------------------------------------------------------ Egypt & region
p_region = {"section": "Egypt desk", "title": "Egypt & the region", "label": "Ports · industry · partners · neighbours", "blocks": [
    {"k": "flow", "n": 2, "blocks": [
        brief("Ports", "More ways to move a box between Egyptian ports", "Yang Ming is taking slots on DP World feeders marketed as EG1–EG3, linking Port Said, Damietta, Alexandria and El Dekheila. Sidra Line's revised loop runs Alexandria–Misurata–Rades–Casablanca–Conakry with a 750 TEU ship. The EBRD lent logistics firm Mesco up to EGP 585m for trucks and yard works at Alexandria, Port Said, Damietta and Sokhna.", ["cn_yangming", "cn_sidra", "eam_mesco"],
              "Intra-Egypt feeders make it easier to book a mainline call at Port Said or Damietta with on-carriage to Alexandria on one carrier."),
        brief("Reefer", "A Sokhna–Jebel Ali corridor for Egyptian produce", "Majid Al Futtaim and DP World signed an MoU to move more Egyptian fruit and vegetables to MAF's UAE stores: consolidation in cold stores at Sokhna, DP World feeders to the UAE, then refrigerated moves to Jebel Ali. No investment value, volume or timeline was given.", ["eam_backsuez"],
              "The route runs through Hormuz, where risk is rising. It is an MoU only, so timing is open."),
        brief("Fertiliser", "Pay more for gas, keep exporting", "Seven fertiliser makers agreed to pay $175m upfront under a 45-day deal that began on 16 November, Asharq Business reports via EnterpriseAM. Their gas price rises 50% to $12.75/mmBtu; in return they can export all current output until early January, while gas cuts of 20–40% stay.", ["eam_fert"],
              "Urea and ammonia exporters can plan December liftings, but in smaller parcels, with a policy review in January."),
        brief("CBAM", "Damietta firm becomes the first non-EU verifier", "Damietta-based ISSC is the first verification body outside the EU accredited under CBAM, EnterpriseAM reports, so Egyptian cement, fertiliser, aluminium and steel exporters can have emissions data verified at home. Egypt supplied 44.3% of the EU's non-EU urea imports in 2025.", ["eam_issc"]),
        brief("Partners", "India aims for $12bn; China at $20bn", "Egypt and India set a target of $12bn of trade by 2030, up from $6.5bn, and agreed to explore a free trade agreement and speed up India's industrial zone in SCZone. The investment minister put Egypt–China trade at about $20bn.", ["eam_india", "zw_china"]),
        brief("Libya", "Agreements signed; border raised", "Egypt and Libya's GNU signed agreements and MoUs on gas infrastructure, refining, fisheries, SMEs and labour on 19 November. Libya, Egypt's largest African market at $1.2bn in nine months, raised visas and entry through the border crossing; no trade-facilitation measure was named.", ["zw_libya", "zw_africa"]),
        brief("Red Sea", "Saudi ports in the Houthis' sights", "After the 20 November warning to ships in Saudi Red Sea ports, watch services that call both Jeddah and Sokhna. MSC's new North India–Red Sea loop (Mundra, Port Qasim, Jeddah, King Abdullah Port) starts in late November with 2,500–3,000 TEU ships.", ["gc_houthi", "cn_msc_redsea"],
              "For Saudi-bound cargo, ask for a contingency: Gulf-side ports, or Safaga and Sokhna ferries with trucking."),
        brief("Gulf", "Building around Hormuz", "An ADNOC L&S tanker was attacked in Hormuz on 17 November. A former WEF supply-chain head told EnterpriseAM that Maersk charges “USD 1k a container to cross Hormuz”; we have not seen the carrier's tariff. Saudi road-freight registrations rose 52% to 104,612 in Q3.", ["eam_whosail", "zw_saudi"]),
        brief("Costs at home", "Minimum wage up 21% in January", "The private-sector minimum wage rises 21% to EGP 8,500 a month from 1 January 2027, covering 26.5m workers.", ["eam_wage"],
              "Expect upward pressure on local trucking, warehousing and handling tariffs from January."),
    ]},
    {"k": "p", "text": "Customs watch: we found no new customs decree, ACI/Nafeza change or GOEIC rule dated 16–22 November on any page we could read.", "src": []},
]}

# ------------------------------------------------------------------ toolkit
p_tool = {"section": "The toolkit", "title": "The toolkit", "label": "Practical · Red Sea cargo in December", "blocks": [
    {"k": "box", "kicker": "Rockit explains", "title": "Six questions before you book Red Sea cargo this December", "style": "margin-bottom:4mm", "blocks": [
        P("Ships are returning to Suez while the security picture around Bab el-Mandeb and Saudi Red Sea ports worsens. A booking that looks cheap can carry costs that only show up when routing changes. These six lines cover most of them."),
        {"k": "html", "html": '''<table class="t" style="color:#e7e3d3;margin-top:1mm"><tr><th style="color:#a9b1c2;border-color:#d6d2c2">Ask</th><th style="color:#a9b1c2;border-color:#d6d2c2">Why</th><th style="color:#a9b1c2;border-color:#d6d2c2">What a good answer looks like</th></tr>
<tr><td style="border-color:#2c3b5c"><b>Routing</b></td><td style="border-color:#2c3b5c">Services can switch between Suez and the Cape</td><td style="border-color:#2c3b5c">The service name, its routing today, and transit days both ways</td></tr>
<tr><td style="border-color:#2c3b5c"><b>Diversion clause</b></td><td style="border-color:#2c3b5c">If the ship reroutes, who pays the extra days and fuel?</td><td style="border-color:#2c3b5c">A named surcharge, or a cap, written into the quote</td></tr>
<tr><td style="border-color:#2c3b5c"><b>War-risk</b></td><td style="border-color:#2c3b5c">Premiums can be added mid-voyage</td><td style="border-color:#2c3b5c">The current charge per box and how it is reviewed</td></tr>
<tr><td style="border-color:#2c3b5c"><b>Skipped calls</b></td><td style="border-color:#2c3b5c">Jeddah or Sokhna may be omitted at short notice</td><td style="border-color:#2c3b5c">Where the box would be discharged, and who pays on-carriage</td></tr>
<tr><td style="border-color:#2c3b5c"><b>Surcharges</b></td><td style="border-color:#2c3b5c">December adds peak, fuel, piracy and Suez charges</td><td style="border-color:#2c3b5c">Every line named, with its effective date</td></tr>
<tr><td style="border-color:#2c3b5c"><b>Free time</b></td><td style="border-color:#2c3b5c">Two in three East–West ships arrive late</td><td style="border-color:#2c3b5c">Demurrage and detention days that start from actual, not scheduled, arrival</td></tr></table>'''},
    ]},
    {"k": "grid", "cols": "1fr 1fr 1fr", "gap": "6mm", "columns": [[
        {"k": "kicker", "text": "If you import"},
        {"k": "ticks", "items": [
            "Benchmark Asia quotes against $4,300–4,989 per 40ft spot (Freightos, Drewry, Xeneta), dated 17–19 November.",
            "Maersk's $1,500 per 40ft Med peak surcharge applies from 23 November; check it is in your quote.",
            "Challenge fuel-surcharge increases: bunker prices fell $25.50 a tonne in a week.",
            "Price FX risk: the dollar went back above EGP 54 on 22 November.",
        ]},
    ], [
        {"k": "kicker", "text": "If you export"},
        {"k": "ticks", "items": [
            "Libya, Sudan, Morocco, Algeria and Tunisia are 50%-freight-support markets: keep freight files complete.",
            "Perishables to the Gulf: plan for Hormuz risk; MAF's Sokhna–Jebel Ali corridor is an MoU only.",
            "CBAM goods to the EU: emissions data can now be verified in Damietta.",
            "Air to Europe or the Gulf: rates from the region are 63–83% above last year; book early.",
        ]},
    ], [
        {"k": "kicker", "text": "If you forward"},
        {"k": "ticks", "items": [
            "Get written confirmation of each airline's DAWB terms before tendering.",
            "Keep a 9–10 January reopener in US- and China-lane quotes.",
            "Screen UAE ship managers and insurers against the 16 November EU listings.",
            "Agree a contingency for Saudi Red Sea calls with each carrier.",
        ]},
    ]]},
    {"k": "rule"},
    {"k": "panel", "kicker": "Ask the desk", "title": "Send us a lane", "blocks": [
        P("Tell us origin, destination, commodity, volume and timing, and we will come back with an all-in quote that names every line above, with its routing and validity."),
        P("**inquiry@rockit.com.eg** · +20 2 2690 7601 · rockit-transport.com"),
        P("Offices in Cairo, Alexandria, Ain Sokhna, Port Said and Damietta."),
    ]},
]}

# ------------------------------------------------------------------ calendar & glossary
p_cal = {"section": "Calendar & glossary", "title": "Calendar & glossary", "label": "Dates to diarise · words we use", "blocks": [
    {"k": "grid", "cols": "1.25fr 1fr", "gap": "8mm", "columns": [[
        {"k": "table", "caption": "The next seven weeks", "head": ["Date", "Event", "Why it matters"], "num_cols": [0],
         "rows": [
             {"cells": ["23 Nov", "Maersk Far East–Med PSS applies ($1,500 per 40ft)", "Asia–Egypt cost"], "src": ["cn_asiamed"]},
             {"cells": ["23–27 Nov", "IMO intersessional GHG working group", "Sets up the carbon vote"], "src": ["imo_cal"]},
             {"cells": ["Late Nov", "MSC North India–Red Sea service starts", "India–Jeddah options"], "src": ["cn_msc_redsea"]},
             {"cells": ["30 Nov–3 Dec", "IMO MEPC 85, London", "Global carbon price for shipping"], "src": ["imo_cal"]},
             {"cells": ["1 Dec", "Hapag-Lloyd December FAK; Q1 2027 fuel surcharge published", "Asia–Egypt rates; 2027 contracts"], "src": ["cn_hapag_fak", "sb_hapag_mfs"]},
             {"cells": ["1–14 Dec", "MSC and CMA CGM December FAKs", "Re-quote mid-month"], "src": ["cn_msc_fak", "cn_cma_dec"]},
             {"cells": ["4 Dec", "First Gemini NE1 Suez sailing; NZF session (to be confirmed)", "Suez capacity; carbon"], "src": ["cn_gemini", "imo_cal"]},
             {"cells": ["9 Dec", "EU package on reliance on non-EU suppliers (reported)", "Subsidy and procurement rules"], "src": ["eam_scrap"]},
             {"cells": ["Dec", "MSC Fujairah Shuttle 2 starts", "Gulf routing outside Hormuz"], "src": ["cn_msc_fuj"]},
             {"cells": ["Before 15 Dec", "IMF Board vote; programme expires 15 Dec", "About $2.3bn for Egypt"], "src": ["eam_imf"]},
             {"cells": ["17 Dec", "CBE Monetary Policy Committee", "Rates and the pound"], "src": ["eam_gs"]},
             {"cells": ["20 Dec", "Gemini NE3 Suez sailing", "Suez capacity"], "src": ["cn_gemini"]},
             {"cells": ["31 Dec", "Export rebate programme, phase one ends", "Phase two from July 2027"], "src": ["eam_rebate"]},
             {"cells": ["1 Jan 2027", "Min. wage EGP 8,500; CBAM in Norway & Iceland; Hapag-Lloyd MFS", "Local costs; EU carbon; fuel"], "src": ["eam_wage", "ec_cbam_no", "sb_hapag_mfs"]},
             {"cells": ["Early Jan", "Fertiliser gas-for-exports deal ends", "Urea and ammonia exports"], "src": ["eam_fert"]},
             {"cells": ["9–10 Jan 2027", "US port-fee pause and China's tariff truce end", "Transpacific surcharge risk"], "src": ["fr_portfee", "gc_truce"]},
         ]},
    ], [
        {"k": "kicker", "text": "Glossary"},
        {"k": "html", "html": "".join(f'<div style="padding:1.5mm 0;border-bottom:.5pt solid #e3d8bd;font-size:7.9pt;line-height:1.4"><b style="font:600 7.6pt IBM Plex Mono,monospace;color:#8a6514;letter-spacing:.06em">{k}</b> · {v}</div>' for k, v in [
            ("FAK", "Freight All Kinds: a carrier's published base rate for general cargo, regardless of commodity."),
            ("PSS", "Peak Season Surcharge: an add-on charged in busy periods."),
            ("GFS / MFS", "Global Fuel Surcharge (MSC) / Marine Fuel Surcharge (Hapag-Lloyd from 2027): the fuel component of a sea rate."),
            ("TEU / FEU", "Twenty- and forty-foot equivalent units: one 40ft box is two TEU."),
            ("WCI / FBX", "Drewry World Container Index and Freightos Baltic Index: weekly spot-rate benchmarks."),
            ("Blank sailing", "A scheduled voyage a carrier cancels to cut capacity."),
            ("Gemini", "The Maersk–Hapag-Lloyd network partnership."),
            ("UKMTO / JMIC", "UK Maritime Trade Operations and the Joint Maritime Information Center: naval reporting centres for Gulf and Red Sea shipping."),
            ("STS", "Ship-to-ship transfer of cargo at sea."),
            ("DAWB", "Direct Air Waybill: an air waybill issued in the shipper's name rather than the forwarder's."),
            ("EFF / RSF", "The IMF's Extended Fund Facility and Resilience and Sustainability Facility."),
            ("CBAM", "EU Carbon Border Adjustment Mechanism: a carbon price on imports of steel, aluminium, cement, fertiliser and more."),
            ("NZF", "The IMO Net-Zero Framework: a proposed global carbon price for shipping."),
            ("ACI / ACID", "Egypt's Advance Cargo Information system and the 19-digit ACID number every import needs before shipment."),
        ])},
    ]]},
]}

p_sources = {"section": "Sources", "title": "Sources", "label": "Every figure, footnoted", "sources_page": True, "split": 51, "blocks": [
    P("We read every page below between 16 and 22 November 2026 (a few earlier pages are cited for rules still in force). Where a source reports a claim by a party to a conflict, the text says so. Analysis, marked *Why it matters* or *Rockit's read*, is ours."),
]}

edition = {
    "meta": {"voyage": "002", "date_long": "23 November 2026", "pages_label": "Full edition · 16 pages", "pages": 16,
             "read_window": "16 and 22 November 2026", "title": "The Rockit Manifest · Voyage 002 · Full edition"},
    "sources": {k: {"name": v[0], "title": v[1], "date": v[2], "url": v[3]} for k, v in SOURCES.items()},
    "disclaimer": "The Rockit Manifest is published every Monday by Rockit Transport Services & Logistics (RTSL), Egypt. Figures come from the named public sources on the dates shown and may change. They are not a quotation or offer. Regulatory notes are summaries, not legal advice. © 2026 RTSL.",
    "cover": cover,
    "pages": [p_brief, p_ocean, p_straits, p_costs, p_air, p_logi, p_geo, p_war, p_egypt, p_region, p_tool, p_cal, p_sources],
    "back": {
        "headline": "Rockit Transport Services & Logistics",
        "deck": "A Cairo freight forwarder moving air, ocean and inland cargo for exporters, importers, manufacturers and project shippers.",
        "columns": [
            {"h": "Services", "items": ["Air freight", "Ocean freight: FCL and LCL", "Inland freight: our own fleet", "Customs clearance", "Project logistics", "Supply chain & warehousing"]},
            {"h": "Offices", "items": ["Cairo (HQ)", "Alexandria", "Port Ain El Sokhna", "Port Said", "Damietta Port"]},
            {"h": "Free tools", "items": ["Container tracking", "Vessel schedules", "Load calculator", "Duties & taxes calculator", "Chargeable weight"]},
        ],
        "next": ["IMO MEPC 85: does shipping get a global carbon price?", "December tariffs in force: did Asia–Egypt rates stick?", "Hapag-Lloyd's Suez-based fuel surcharge for 2027", "The Red Sea after the Houthi warning to Saudi ports"],
        "cta_kicker": "Every Monday · rockit-transport.com/insights/categories/newsletter",
        "cta": "Send us a lane at **inquiry@rockit.com.eg** and get an all-in quote that names every line.",
    },
}
out = Path(__file__).with_name("edition.json")
out.write_text(json.dumps(edition, ensure_ascii=False, indent=1))
print("wrote", out, "·", len(SOURCES), "sources defined")
