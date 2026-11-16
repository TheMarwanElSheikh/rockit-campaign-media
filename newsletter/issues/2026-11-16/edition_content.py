#!/usr/bin/env python3
"""Full edition, Voyage 001 (16 Nov 2026). Writes edition.json next to this file.

Every figure here was read on a fetched source page (see AUDIT_EDITION.md). Source ids map to the
`SOURCES` table below; the builder numbers them in order of first citation and prints the list on the last page.
"""
import json
from pathlib import Path

CN = "Container News"
GC = "gCaptain"
EAM = "EnterpriseAM"
ACN = "Air Cargo News"
ST = "STAT Times"
FW = "FreightWaves"

SOURCES = {
    # ---------------- ocean
    "drewry": ("Drewry", "World Container Index – 12 Nov", "12 Nov 2026", "https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry"),
    "freightos10": ("Freightos", "LA/LB strike deadline extended; Dem win increasing trade uncertainty – November 10, 2026 Update", "10 Nov 2026", "https://www.freightos.com/freight-resources/la-lb-strike-deadline-extended-dem-win-increasing-trade-uncertainty-november-10-2026-update/"),
    "xeneta13": ("Xeneta", "Weekly Ocean Container Shipping Market Update – 13.11.26", "13 Nov 2026", "https://www.xeneta.com/news/xeneta-weekly-ocean-container-shipping-market-update-13.11.26"),
    "xeneta_summit": ("Xeneta", "Analysts forecast ocean freight spot rates to fall 30% in 2027 as Red Sea return sees capacity flooding back", "5 Nov 2026", "https://www.xeneta.com/news/xeneta-summit-analysts-forecast-ocean-freight-spot-rates-to-fall-30-in-2027-as-red-sea-return-sees-capacity-flooding-back"),
    "cn_hapag_fak": (CN, "Hapag-Lloyd raises Far East–Europe freight rates from December", "15 Nov 2026", "https://container-news.com/hapag-lloyd-raises-far-east-europe-freight-rates-from-december/"),
    "cn_msc_fak": (CN, "MSC raises December FAK rates to Mediterranean and Black Sea", "12 Nov 2026", "https://container-news.com/msc-raises-december-fak-rates-to-mediterranean-and-black-sea/"),
    "cn_msc_sur": (CN, "MSC extends piracy and Suez surcharges across Mediterranean", "7 Nov 2026", "https://container-news.com/msc-extends-piracy-and-suez-surcharges-across-mediterranean/"),
    "cn_maersk_pss": (CN, "Maersk introduces new Asia–Europe PSS and revises North America charges", "13 Nov 2026", "https://container-news.com/maersk-introduces-new-asia-europe-pss-and-revises-north-america-charges/"),
    "cn_cma_oct": (CN, "CMA CGM raises Asia–Mediterranean rates and announces new surcharges", "20 Oct 2026", "https://container-news.com/cma-cgm-raises-asia-mediterranean-rates-and-announces-new-surcharges/"),
    "sb_evergreen": ("Ship & Bunker", "Evergreen Makes First Suez Canal Transit in Nearly Three Years", "9 Nov 2026", "https://shipandbunker.com/news/world/201712-evergreen-makes-first-suez-canal-transit-in-nearly-three-years"),
    "cn_one": (CN, "ONE returns to Suez Canal as Premier Alliance plans further service shifts", "16 Nov 2026", "https://container-news.com/one-returns-to-suez-canal-as-premier-alliance-plans-further-service-shifts/"),
    "fbx_page": ("Freightos", "Freightos Baltic Index – key events (3 Nov entry)", "accessed 16 Nov 2026", "https://www.freightos.com/enterprise/terminal/freightos-baltic-index-global-container-pricing-index/"),
    "gc_hapag": (GC, "Hapag-Lloyd Profit Surges as Freight Rates Rise, Red Sea Services Return", "13 Nov 2026", "https://gcaptain.com/hapag-lloyd-profit-surges-as-freight-rates-rise-red-sea-services-return/"),
    "cn_summit": (CN, "Summit Shipping announces new China–Red Sea container service", "14 Nov 2026", "https://container-news.com/summit-shipping-announces-new-china-red-sea-container-service/"),
    "cn_msc_redsea": (CN, "MSC to launch new North India–Red Sea container service", "15 Nov 2026", "https://container-news.com/msc-to-launch-new-north-india-red-sea-container-service/"),
    "cn_yangming": (CN, "Yang Ming expands Egypt coverage through DP World slot-sharing deal", "15 Nov 2026", "https://container-news.com/yang-ming-expands-egypt-coverage-through-dp-world-slot-sharing-deal/"),
    "cn_evergreen_sched": (CN, "Evergreen schedules first Suez transits with own vessels", "6 Nov 2026", "https://container-news.com/evergreen-schedules-first-suez-transits-with-own-vessels/"),
    "ls_suez_cong": ("The Loadstar", "Return to Suez transits raises congestion fears at Red Sea ports", "11 Nov 2026", "https://theloadstar.com/return-to-suez-transits-raises-congestion-fears-at-red-sea-ports/"),
    "eam_suez_oct": (EAM, "The US commits USD 125 mn to Egypt under a new aid template… (SCA October revenue item)", "8 Nov 2026", "https://enterpriseam.com/egypt/2026/11/08/the-us-commits-usd-125-mn-to-egypt-under-a-new-aid-template-that-ties-development-money-to-market-access-for-american-companies/"),
    "gc_gulf_oil": (GC, "Gulf Oil Exports Recover as Hormuz Shipping Struggles", "13 Nov 2026", "https://gcaptain.com/gulf-oil-exports-recover-as-hormuz-shipping-struggles/"),
    "gc_ablaze": (GC, "Tanker Ablaze Off UAE as More Attacks Rattle Gulf Shipping", "12 Nov 2026", "https://gcaptain.com/tanker-ablaze-off-uae-as-more-attacks-rattle-gulf-shipping/"),
    "gc_lng_mine": (GC + " / Reuters", "Iran Says Tanker Carrying LNG Hit Mine, Suffered Explosion in Hormuz", "13 Nov 2026", "https://gcaptain.com/iran-says-tanker-carrying-lng-hit-mine-suffered-explosion-in-hormuz/"),
    "gc_mine": (GC + " / Reuters", "Oil Tanker On Fire After Hitting Mine in Hormuz", "14 Nov 2026", "https://gcaptain.com/oil-tanker-on-fire-after-hitting-mine-in-hormuz/"),
    "gc_panama": (GC, "Panama Canal Raises Daily Transit Capacity as Water Conditions Improve", "11 Nov 2026", "https://gcaptain.com/panama-canal-raises-daily-transit-capacity-as-water-conditions-improve/"),
    "gc_la_strike": (GC + " / Bloomberg", "LA Port Strike Threat Deferred Again As Labor Talks Drag On", "7 Nov 2026", "https://gcaptain.com/la-port-strike-threat-deferred-again-as-labor-talks-drag-on/"),
    "gc_la_record": (GC, "Port of Los Angeles Sets October Cargo Record as Strike Threat and Rail Delays Loom", "12 Nov 2026", "https://gcaptain.com/port-of-los-angeles-sets-october-cargo-record-as-strike-threat-and-rail-delays-loom/"),
    "fw_maersk": (FW, "Maersk raises profit outlook as earnings surge, but shares slide on expectations miss", "5 Nov 2026", "https://www.freightwaves.com/?p=585078"),
    "gc_maersk_lng": (GC, "Maersk's 26-Ship LNG Order Adds Nearly Half a Million TEU to Newbuilding Pipeline", "5 Nov 2026", "https://gcaptain.com/maersks-26-ship-lng-order-adds-nearly-half-a-million-teu-to-newbuilding-pipeline/"),
    "gc_cmacgm": (GC, "CMA CGM Net Profit More Than Triples to $2.32 Billion as Freight Rates Surge", "13 Nov 2026", "https://gcaptain.com/cma-cgm-net-profit-more-than-triples-to-2-32-billion-as-freight-rates-surge/"),
    "fw_one": (FW, "ONE lifts profit forecast to $2 billion as earnings surge", "4 Nov 2026", "https://www.freightwaves.com/news/one-lifts-profit-forecast-to-2-billion-as-earnings-surge"),
    "sb_prices": ("Ship & Bunker", "Bunker prices – Global 20 Ports Average (values dated 13 Nov)", "13 Nov 2026", "https://shipandbunker.com/prices"),
    "cn_mabux": (CN, "MABUX: Bunker prices remain volatile in November", "2 Nov 2026", "https://container-news.com/mabux-bunker-prices-remain-volatile-in-november/"),
    # ---------------- air & logistics
    "iata_sep": ("IATA", "Air Cargo Demand Accelerates in September, Up 7.7%", "29 Oct 2026", "https://www.iata.org/en/pressroom/2026-releases/10-29-air-cargo-demand-accelerates-september/"),
    "tac_nov": ("TAC Index", "Air freight rates surge past previous peak season highs as jet fuel prices soar", "5 Nov 2026", "https://www.tacindex.com/air-freight-rates-costs-latest-november-2026/"),
    "acn_rates": (ACN, "Airfreight rates reach 2026 high on peak season demand", "12 Nov 2026", "https://www.aircargonews.net/data/2026/11/airfreight-rates-reach-2026-high-on-peak-season-demand/"),
    "st_wcd": (ST, "Global air cargo tonnages up 6% in Oct despite drop in China-Europe volumes (WorldACD)", "9 Nov 2026", "https://www.stattimes.com/air-cargo/global-air-cargo-tonnages-up-6-in-oct-despite-drop-in-china-europe-volumes-1361242"),
    "acn_xen": (ACN, "Air cargo demand continues to grow but peak surge looking unlikely (Xeneta)", "6 Nov 2026", "https://www.aircargonews.net/data/2026/11/air-cargo-demand-continues-to-grow-but-peak-surge-looking-unlikely/"),
    "st_dhl": (ST, "DHL Group upgrades 2026 outlook as Q3 EBIT hits €1.7bn", "5 Nov 2026", "https://www.stattimes.com/financial/dhl-group-upgrades-2026-outlook-as-q3-ebit-hits-17bn-1361217"),
    "acn_dgf": (ACN, "DHL Forwarding sees airfreight rise but some volumes move to express", "5 Nov 2026", "https://www.aircargonews.net/freight-forwarder/2026/11/dhl-forwarding-sees-airfreight-rise-but-some-volumes-move-to-express/"),
    "st_dsv": (ST, "DSV Q3: Air freight yields up 8% despite 3% volume dip", "22 Oct 2026", "https://www.stattimes.com/air-cargo/dsv-q3-air-freight-yields-up-8-despite-3-volume-dip-1360995"),
    "st_kn": (ST, "Kuehne+Nagel Air Logistics EBIT soars 84% in Q3 2026", "22 Oct 2026", "https://www.stattimes.com/air-cargo/kuehnenagel-air-logistics-ebit-soars-84-in-q3-2026-1361006"),
    "acn_expd": (ACN, "Expeditors sees air cargo volumes and revenues rise in Q3", "3 Nov 2026", "https://www.aircargonews.net/freight-forwarder/2026/11/expeditors-sees-air-cargo-volumes-and-revenues-rise-in-q3/"),
    "acn_scan": (ACN, "Scan Global Logistics targets the top 20 with deal to acquire OIA Global", "29 Oct 2026", "https://www.aircargonews.net/business/2026/10/scan-global-logistics-targets-the-top-20-with-deal-to-acquire-oia-global/"),
    "acn_ait": (ACN, "AIT acquires Connor Anderson", "2 Nov 2026", "https://www.aircargonews.net/business/2026/11/ait-acquires-connor-anderson/"),
    "acn_chr": (ACN, "CH Robinson invests in AI to speed up air cargo quoting", "26 Oct 2026", "https://www.aircargonews.net/freight-forwarder/2026/10/ch-robinson-invests-in-ai-to-speed-up-air-cargo-quoting/"),
    "dcsa_korea": ("DCSA", "From issuance to surrender: KTNET and HMM test eBL Korea on DCSA standards", "5 Nov 2026", "https://dcsa.org/newsroom/ktnet-hmm-ebl-korea"),
    "acn_saf": (ACN, "DHL is first express cargo carrier to use SAF at Paris CDG airport", "9 Nov 2026", "https://www.aircargonews.net/sustainability/2026/11/dhl-is-first-express-cargo-carrier-to-use-saf-at-paris-cdg-airport/"),
    "acn_geiken": (ACN, "DHL Global Forwarding names Geiken as Sub-Saharan Africa CEO", "10 Nov 2026", "https://www.aircargonews.net/people/2026/11/dhl-global-forwarding-names-geiken-as-sub-saharan-africa-ceo/"),
    "ls_shenzhen": ("The Loadstar", "Shenzhen belly cargo ban threatens peak-season squeeze at other gateways", "10 Nov 2026", "https://theloadstar.com/shenzhen-air-cargo-restrictions-ahead-of-apec-threaten-peak-shipments/"),
    # ---------------- geopolitics & policy
    "fr_portfee": ("Federal Register (USTR)", "Notice of Modification of Section 301 Action: China's Targeting of the Maritime, Logistics, and Shipbuilding Sectors for Dominance (91 FR 72608)", "10 Nov 2026", "https://www.federalregister.gov/documents/2026/11/10/2026-22867/notice-of-modification-of-section-301-action-chinas-targeting-of-the-maritime-logistics-and"),
    "fr_excl": ("Federal Register (USTR)", "Notice of Product Exclusion Extensions: China's Acts, Policies, and Practices Related to Technology Transfer… (91 FR 72610)", "10 Nov 2026", "https://www.federalregister.gov/documents/2026/11/10/2026-22925/notice-of-product-exclusion-extensions-chinas-acts-policies-and-practices-related-to-technology"),
    "gc_portfee": (GC, "U.S. Formalizes Two-Month Extension of China Ship Port Fee Suspension", "10 Nov 2026", "https://gcaptain.com/u-s-formalizes-two-month-extension-of-china-ship-port-fee-suspension/"),
    "gc_truce": (GC + " / Reuters", "China Extends US Trade Truce by Two Months", "9 Nov 2026", "https://gcaptain.com/china-extends-us-trade-truce-by-two-months/"),
    "ls_ups": ("The Loadstar", "UPS in court bid to recover tariff payments ruled 'unlawful'", "10 Nov 2026", "https://theloadstar.com/ups-in-court-bid-to-recover-tariff-payments-ruled-unlawful/"),
    "fr_232": ("Federal Register", "Adjusting Imports of Robotics, Industrial Machinery, and Their Parts and Components Into the United States (Proclamation 11077, 91 FR 69199)", "2 Nov 2026", "https://www.federalregister.gov/documents/2026/11/02/2026-22385/adjusting-imports-of-robotics-industrial-machinery-and-their-parts-and-components-into-the-united"),
    "scd_232": ("Supply Chain Dive", "Trump opts for trade talks over tariffs for robotics, industrial machinery", "29 Oct 2026", "https://www.supplychaindive.com/news/trump-opts-for-trade-talks-over-tariffs-for-robotics-industrial-machinery/873166/"),
    "gc_imo_council": (GC, "IMO Warns of Mounting Human Toll as Attacks on Commercial Shipping Continue", "9 Nov 2026", "https://gcaptain.com/imo-warns-of-mounting-human-toll-as-attacks-on-commercial-shipping-continue/"),
    "gc_imo_solas": (GC, "IMO Chief Calls for Strict Enforcement of SOLAS Rules in Strait of Hormuz", "11 Nov 2026", "https://gcaptain.com/imo-chief-calls-for-strict-enforcement-of-solas-rules-in-strait-of-hormuz/"),
    "gc_fge": (GC + " / Bloomberg", "Iran Oil Exports Near Zero But Peace Deal Not Likely, FGE Says", "6 Nov 2026", "https://gcaptain.com/iran-oil-exports-near-zero-but-peace-deal-not-likely-fge-says/"),
    "imo_ghg": ("IMO", "IMO's work to cut GHG emissions from ships", "accessed 16 Nov 2026", "https://www.imo.org/en/mediacentre/hottopics/pages/cutting-ghg-emissions.aspx"),
    "imo_faq": ("IMO", "The IMO Net-Zero Framework – FAQs", "accessed 16 Nov 2026", "https://www.imo.org/en/mediacentre/hottopics/pages/faqs-the-imo-net-zero-framework.aspx"),
    "gc_nzf": (GC, "IMO Uncertainty Puts Shipping's 2030 Fuel Target at Risk", "22 Sep 2026", "https://gcaptain.com/imo-uncertainty-puts-shippings-2030-fuel-target-at-risk/"),
    "ec_cbam_price": ("European Commission, DG TAXUD", "Price of CBAM certificates", "accessed 16 Nov 2026", "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en"),
    "ec_cbam_def": ("European Commission, DG TAXUD", "CBAM definitive regime", "accessed 16 Nov 2026", "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-definitive-regime_en"),
    "gc_ets": (GC, "From Policy to Practice: Shipping's Regulatory Autumn Puts Proof on Trial", "9 Oct 2026", "https://gcaptain.com/from-policy-to-practice-shippings-regulatory-autumn-puts-proof-on-trial/"),
    "gc_russia3": (GC + " / Reuters", "Russia Says It Hit Three Cargo Ships In Black Sea", "8 Nov 2026", "https://gcaptain.com/russia-says-it-hit-three-cargo-ships-in-black-sea/"),
    "gc_rudiesel": (GC + " / Bloomberg", "Russian Diesel Tanker Makes U-Turn After Heading to U.S.", "11 Nov 2026", "https://gcaptain.com/russian-diesel-tanker-makes-u-turn-after-heading-to-u-s/"),
    # ---------------- Egypt & region
    "eam_rebate": (EAM, "The government is raising export rebates by an average of 35% and picking up as much as half the freight bill to new markets", "8 Nov 2026", "https://enterpriseam.com/egypt/2026/11/08/the-government-is-raising-export-rebates-by-an-average-of-35-and-picking-up-as-much-as-half-the-freight-bill-to-new-markets/"),
    "eam_imf": (EAM, "Egypt's final IMF review moves to virtual talks with USD 2.3 bn at stake and a 15 December deadline", "15 Nov 2026", "https://enterpriseam.com/egypt/2026/11/15/egypts-final-imf-review-moves-to-virtual-talks-with-usd-2-3-bn-at-stake-and-a-15-december-deadline/"),
    "eam_cbe": (EAM, "CBE hikes for the first time since March 2024, raising rates 100 bps and moving its inflation target to 4Q 2027", "1 Nov 2026", "https://enterpriseam.com/egypt/2026/11/01/cbe-hikes-for-the-first-time-since-march-2024-raising-rates-100-bps-and-moving-its-inflation-target-to-4q-2027/"),
    "eam_gs": (EAM, "Goldman Sachs calls EGP undervalued by 30%, sees it at 50 per USD", "8 Nov 2026", "https://enterpriseam.com/egypt/2026/11/08/goldman-sachs-calls-egp-undervalued-by-30-sees-it-at-50-per-usd/"),
    "eam_db": (EAM, "Deutsche Bank Research sees EGP at 48-60 depending on the Iran war, expects CBE to hold rates into next year", "16 Nov 2026", "https://enterpriseam.com/egypt/2026/11/16/deutsche-bank-research-sees-egp-at-48-60-depending-on-the-iran-war-expects-cbe-to-hold-rates-into-next-year/"),
    "eam_infl": (EAM, "Egypt's urban inflation slowed to 12.7% in October despite non-food momentum", "10 Nov 2026", "https://enterpriseam.com/egypt/2026/11/10/egypts-urban-inflation-slowed-to-12-7-in-october-despite-non-food-momentum/"),
    "eam_cbam": (EAM, "Egypt asks Brussels for preferential treatment as EU's carbon border levy nears", "3 Nov 2026", "https://enterpriseam.com/egypt/2026/11/03/egypt-asks-brussels-for-preferential-treatment-as-eus-carbon-border-levy-nears/"),
    "eam_pmi": (EAM, "Egypt's PMI holds at 47.2 in October, but output and new orders fall at their fastest pace in four months", "5 Nov 2026", "https://enterpriseam.com/egypt/2026/11/05/egypts-pmi-holds-at-47-2-in-october-but-output-and-new-orders-fall-at-their-fastest-pace-in-four-months/"),
    "eam_remit": (EAM, "Remittances hit a record USD 38.2 bn in the first nine months of 2026", "11 Nov 2026", "https://enterpriseam.com/egypt/2026/11/11/remittances-hit-a-record-usd-38-2-bn-in-the-first-nine-months-of-2026/"),
    "eam_sczone": (EAM, "SCZone brings in Telecom Egypt to end network downtime for factories and terminals across its ports and zones", "9 Nov 2026", "https://enterpriseam.com/egypt/2026/11/09/sczone-brings-in-telecom-egypt-to-end-network-downtime-for-factories-and-terminals-across-its-ports-and-zones/"),
    "eam_gas": (EAM, "Gov't deepens industrial gas rationing, raising curtailments on fertilizer and methanol plants to 33% and notifying Ezz Steel of a 30% cut", "9 Nov 2026", "https://enterpriseam.com/egypt/2026/11/09/govt-deepens-industrial-gas-rationing-raising-curtailments-on-fertilizer-and-methanol-plants-to-33-and-notifying-ezz-steel-of-a-30-cut/"),
    "eam_dpw": (EAM + " Infrastructure", "Boxes by truck, fuel by?", "16 Nov 2026", "https://enterpriseam.com/infrastructure/2026/11/16/boxes-by-truck-fuel-by/"),
    "eam_adports": (EAM + " Infrastructure", "AD Ports' 3Q net income jumps 64% to a record AED 975 mn as freight rates offset lower UAE port volumes", "12 Nov 2026", "https://enterpriseam.com/infrastructure/2026/11/12/ad-ports-3q-net-income-jumps-64-to-a-record-aed-975-mn-as-freight-rates-offset-lower-uae-port-volumes/"),
    "eam_gccrail": (EAM + " Infrastructure", "GCC states sign the legal framework for a 2.1k-km regional railway…", "10 Nov 2026", "https://enterpriseam.com/infrastructure/2026/11/10/gcc-states-sign-the-legal-framework-for-a-2-1k-km-regional-railway-but-each-country-still-funds-its-own-section/"),
    "eam_dpw_africa": (EAM + " Infrastructure", "DP World starts a weekly China-Africa line + DHL renews its A300 maintenance deal with Joramco", "3 Nov 2026", "https://enterpriseam.com/infrastructure/2026/11/03/dp-world-starts-a-weekly-china-africa-line-dhl-renews-its-a300-maintenance-deal-with-joramco/"),
    "eam_sudan": (EAM, "Sudan scraps import ban on 44 goods, zeroes duties on eight food staples", "29 Oct 2026", "https://enterpriseam.com/egypt/2026/10/29/sudan-scraps-import-ban-on-44-goods-zeroes-duties-on-eight-food-staples/"),
    "dne_koper": ("Daily News Egypt", "Seaport integration, labour migration pact sought by Egypt with Slovenia", "4 Nov 2026", "https://dailynewsegypt.com/2026/11/04/seaport-integration-labour-migration-pact-sought-by-egypt-with-slovenia/"),
    "dne_sinai": ("Daily News Egypt", "Egypt advances construction of 341km railway linking Bir al-Abd, Arish and Taba", "2 Nov 2026", "https://dailynewsegypt.com/2026/11/02/egypt-advances-construction-of-341km-railway-linking-bir-al-abd-arish-and-taba/"),
    "eam_iraq": (EAM, "Iraq, Egypt and Jordan discuss new Red Sea, Med outlets for Iraqi crude", "3 Nov 2026", "https://enterpriseam.com/egypt/2026/11/03/iraq-egypt-and-jordan-discuss-new-red-sea-med-outlets-for-iraqi-crude/"),
    "dne_farid": ("Daily News Egypt", "Egypt's investment minister holds talks in Washington to boost US trade, African market access", "10 Nov 2026", "https://dailynewsegypt.com/2026/11/10/egypts-investment-minister-holds-talks-in-washington-to-boost-us-trade-african-market-access/"),
    "eam_privlabel": (EAM, "Private Label Egypt returns this November to bring together local manufacturers and brands", "15 Nov 2026", "https://enterpriseam.com/egypt/2026/11/15/private-label-egypt-returns-this-november-to-bring-together-local-manufacturers-and-brands/"),
}

P = lambda text, src=None, cls="": {"k": "p", "text": text, "src": src, "cls": cls}


def brief(tag, head, text, src, why_=None):
    b = {"k": "brief", "tag": tag, "head": head, "text": text if isinstance(text, list) else [text], "src": src}
    if why_:
        b["why"] = why_
    return b


def _timeline():
    W, H = 680, 150
    x0, x1, axis = 20, 655, 76
    days = 56  # 16 Nov -> 10 Jan
    # (day offset, date, label, level): level 1/2 above the axis, -1/-2 below
    ev = [(0, "16 Nov", "Shenzhen belly-cargo ban", -1), (2.5, "18–19 Nov", "APEC leaders, Shenzhen", 1), (14, "30 Nov", "IMO MEPC 85 opens", -1),
          (29, "15 Dec", "Egypt IMF programme expires", 1), (31, "17 Dec", "CBE rate decision", -2), (45, "31 Dec", "Rebate phase one ends", 2),
          (49, "4 Jan", "CBAM Q4 price", -1), (54.5, "9–10 Jan", "US port-fee pause & China truce end", 1)]
    ly = {1: 44, 2: 14, -1: 102, -2: 130}
    g = ('<linearGradient id="tlg" x1="0" y1="0" x2="1" y2="1">' + "".join(f'<stop offset="{o}%" stop-color="{c}"/>' for c, o in
         [("#A88329", 0), ("#C09934", 17), ("#DEC163", 33), ("#F7E590", 50), ("#DEC161", 67), ("#C29B36", 83), ("#A88228", 100)]) + "</linearGradient>")
    out = [f'<defs>{g}</defs>', f'<line x1="{x0}" y1="{axis}" x2="{x1}" y2="{axis}" stroke="#1b2333" stroke-width="1.4"/>']
    for m, lab in ((0, "NOV"), (15, "DEC"), (46, "JAN")):
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
    "kicker": "Cover story · Two straits",
    "headline": "Suez reopens. Hormuz doesn't. Your freight bill sits in between.",
    "deck": "Container lines are coming back through the canal and spot rates are easing. The Gulf war keeps fuel, air cargo and Gulf-bound freight expensive. Sixteen pages on what both mean for cargo that touches Egypt.",
    "standfirst": "Evergreen and ONE sent ships through the Suez Canal this month for the first time in nearly three years, and the canal earned $724m in October, its best month since the Red Sea crisis began. In the Strait of Hormuz, traffic is still about 65% below pre-war levels, and at least 10 ships were hit in the first ten days of November.",
    "src": ["sb_evergreen", "cn_one", "eam_suez_oct", "gc_gulf_oil", "gc_mine"],
    "contents": [
        {"p": "02", "sec": "The briefing", "what": "60 seconds · market dashboard"},
        {"p": "03", "sec": "Ocean freight", "what": "spot vs December tariffs"},
        {"p": "04", "sec": "Suez & Hormuz", "what": "two straits, service by service"},
        {"p": "05", "sec": "Carriers & costs", "what": "Q3 results · fuel · 2027"},
        {"p": "06", "sec": "Air cargo", "what": "a peak season priced like one"},
        {"p": "07", "sec": "The logistics business", "what": "forwarders · deals · tech"},
        {"p": "08", "sec": "Geopolitics & trade policy", "what": "the 9 January cliff"},
        {"p": "09", "sec": "War, sanctions & carbon", "what": "IMO · CBAM · ETS"},
        {"p": "10", "sec": "Egypt desk", "what": "rebates · the money tiles"},
        {"p": "11", "sec": "Egypt & the region", "what": "industry · Gulf · Africa"},
        {"p": "12", "sec": "The toolkit", "what": "reading a December quote"},
        {"p": "13", "sec": "Calendar & glossary", "what": "dates to diarise"},
        {"p": "14", "sec": "Sources", "what": "every figure, footnoted (pp. 14–15)"},
        {"p": "16", "sec": "About Rockit", "what": "services · offices · tools"},
    ],
    "status_asof": "as reported 9–16 Nov 2026",
    "status": [
        {"name": "Suez Canal", "state": "open", "label": "Reopening", "note": "Evergreen back 8 Nov, ONE 15 Nov; October transits +32% to 1.5k, revenue $724m (+94%).", "src": ["eam_suez_oct", "cn_one"]},
        {"name": "Red Sea · Bab al-Mandab", "state": "partial", "label": "Half capacity", "note": "467,297 TEU/week committed in October, 50% of pre-crisis; IMO still condemns Houthi attacks.", "src": ["xeneta_summit", "gc_imo_council"]},
        {"name": "Strait of Hormuz", "state": "restricted", "label": "Restricted", "note": "Traffic ~65% below pre-war; 181 incidents logged since 1 March (JMIC).", "src": ["gc_gulf_oil", "gc_ablaze"]},
        {"name": "Cape of Good Hope", "state": "partial", "label": "Still in use", "note": "Most Asia–North Europe loops still route via the Cape (Hapag-Lloyd).", "src": ["gc_hapag"]},
        {"name": "Panama Canal", "state": "open", "label": "Normal", "note": "34 daily slots and the 50ft Neopanamax draft restored (9 Nov advisory).", "src": ["gc_panama"]},
    ],
    "numbers": [
        {"value": "$724m", "label": "Suez Canal revenue, October (+94%)", "src": ["eam_suez_oct"]},
        {"value": "−65%", "label": "Hormuz traffic vs pre-war", "src": ["gc_gulf_oil"]},
        {"value": "$4,305", "label": "Drewry WCI per 40ft (−2%)", "src": ["drewry"]},
        {"value": "+22.8%", "label": "Global air rates, year on year", "src": ["tac_nov"]},
        {"value": "53.39", "label": "EGP per USD, CBE, 12 Nov", "src": ["eam_db"]},
    ],
}

# ------------------------------------------------------------------ page 2: briefing
p2 = {"section": "The briefing", "title": "The briefing", "label": "If you read one page, read this", "blocks": [
    {"k": "grid", "cols": "1.22fr 1fr", "gap": "8mm", "columns": [[
        {"k": "kicker", "text": "From the desk"},
        P("This is the full edition of *The Rockit Manifest*, the weekly review we publish every Monday for exporters, importers, manufacturers and fellow forwarders who move cargo through Egypt.", cls="drop"),
        P("Every figure is footnoted to the page we read it on. Where we could not verify a claim, we left it out; where a claim comes from one side of a conflict, we say so. The analysis lines marked *Why it matters* are ours, and they are kept apart from the reporting. — **The Rockit desk, Cairo**"),
        {"k": "kicker", "text": "The week in 60 seconds"},
        {"k": "ticks", "items": [
            "**Ocean:** spot rates are easing (Drewry WCI −2% to $4,305 per 40ft), but December tariffs to Egypt and the East Med go up: Hapag-Lloyd $6,600, MSC $6,500 per 40ft.",
            "**Suez:** Evergreen (8 Nov) and ONE (15 Nov) are back through the canal, and three more Premier Alliance services will follow.",
            "**Hormuz:** traffic is still about 65% below pre-war; at least 10 ships were hit on 1–10 November.",
            "**Air:** global air rates are 22.8% above last year; Africa-origin spot rates hit $3.11/kg, up 60%.",
            "**Logistics:** forwarders' air profits surged in Q3: Kuehne+Nagel air EBIT +84%; DHL lifted its 2026 guidance above €7bn.",
            "**Trade policy:** the US pause on port fees for Chinese ships and China's tariff truce now both end on 9–10 January 2027.",
            "**Egypt:** the state now pays up to 50% of export freight to new markets, and rebates rise 35% on average from November shipments.",
            "**Money:** CBE deposit rate 20.0%; the pound at 53.39 per dollar after a record 56.35 in October; urban inflation 12.7%.",
        ], "srcs": [["drewry", "cn_hapag_fak", "cn_msc_fak"], ["sb_evergreen", "cn_one"], ["gc_gulf_oil", "gc_mine"], ["tac_nov", "st_wcd"],
                    ["st_kn", "st_dhl"], ["fr_portfee", "gc_truce"], ["eam_rebate"], ["eam_cbe", "eam_db", "eam_rebate", "eam_infl"]]},
    ], [
        {"k": "box", "kicker": "Rockit's read", "title": "Three moves for this week", "blocks": [
            {"k": "ticks", "items": [
                "**Importing from Asia?** Book December cargo against index-linked or negotiated rates, not the $6,500–6,600 tariff, and ask for an all-in quote that lists every surcharge.",
                "**Exporting?** Check whether your markets are on the 50% freight-support list, and build complete rebate files from the first shipment: incomplete files are now refused.",
                "**Shipping to the Gulf or by air?** Confirm the routing (Gulf bypass ports or Saudi Red Sea ports) and lock air space before the late-November peak.",
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
        {"value": "$4,305", "label": "Drewry WCI composite, per 40ft", "delta": "▼ 2% w/w", "dir": "down", "asof": "12 Nov", "src": ["drewry"]},
        {"value": "$4,666", "label": "Far East → Med spot (Xeneta), per 40ft", "delta": "▼ 0.9% w/w", "dir": "down", "asof": "13 Nov", "src": ["xeneta13"]},
        {"value": "$6,600", "label": "Hapag-Lloyd FAK, Far East → Egypt/E. Med, 40ft", "delta": "▲ from 1 Dec", "dir": "up", "asof": "announced 15 Nov", "src": ["cn_hapag_fak"]},
        {"value": "$863.50", "label": "VLSFO per tonne, Global 20 Ports average", "delta": "▲ $17.50", "dir": "up", "asof": "13 Nov", "src": ["sb_prices"]},
        {"value": "+22.8%", "label": "Baltic Air Freight Index (BAI00), year on year", "delta": "▲ 5.3% in 4 weeks", "dir": "up", "asof": "to 2 Nov", "src": ["tac_nov"]},
        {"value": "+7.7%", "label": "Global air cargo demand (CTK), September", "delta": "capacity +2.7%", "dir": "flat", "asof": "IATA, 29 Oct", "src": ["iata_sep"]},
        {"value": "−65%", "label": "Strait of Hormuz traffic vs pre-war", "delta": "8 incidents in latest week", "dir": "flat", "asof": "UKMTO, 13 Nov", "src": ["gc_gulf_oil"]},
        {"value": "$724m", "label": "Suez Canal revenue, October", "delta": "▲ 94% y/y", "dir": "flat", "asof": "SCA, 8 Nov", "src": ["eam_suez_oct"]},
        {"value": "53.39", "label": "EGP per USD (CBE quote)", "delta": "record 56.35 in Oct", "dir": "flat", "asof": "12 Nov", "src": ["eam_db", "eam_rebate"]},
        {"value": "20.0%", "label": "CBE overnight deposit rate", "delta": "▲ 100bp on 29 Oct", "dir": "up", "asof": "next MPC 17 Dec", "src": ["eam_cbe"]},
        {"value": "12.7%", "label": "Egypt urban inflation, October", "delta": "▼ from 13.9%", "dir": "down", "asof": "CAPMAS, 10 Nov", "src": ["eam_infl"]},
        {"value": "$96.33", "label": "Brent crude per barrel", "delta": "Oct peak $136 (IEA)", "dir": "flat", "asof": "13 Nov", "src": ["sb_prices", "gc_gulf_oil"]},
    ]},
]}

# ------------------------------------------------------------------ page 3: ocean freight
p3 = {"section": "Ocean freight", "title": "Ocean freight", "label": "Rates · December tariffs · surcharges", "blocks": [
    {"k": "grid", "cols": "1.18fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "Lead · Asia → Mediterranean", "head": "The index says down. The tariff says up.",
         "deck": "Three independent indices put Asia–Med spot between $4,168 and $4,666 a box. December's published tariffs to Egypt start at $6,500.",
         "text": [
             "Spot container rates eased again last week. Drewry's World Container Index fell 2% to $4,305 per 40ft on 12 November. Shanghai–Rotterdam slipped 3% to $3,504, while Shanghai–Genoa, Drewry's closest proxy for Egypt's Mediterranean ports, held at $4,168. Freightos put Asia–Mediterranean at $4,300 (−1%), and Xeneta's Far East–Med average was $4,666 (−0.9%) on 13 November.",
             "Carriers are pricing December differently. Hapag-Lloyd's Far East–Europe tariff from 1 December sets Türkiye, Egypt and the Eastern Mediterranean at $5,300 per 20ft and $6,600 per 40ft. MSC's December rate lifts East Med 40ft boxes by $800 to $6,500, valid to 14 December at the latest. From 15 November MSC also adds a combined $91 per TEU piracy-risk and Suez Canal surcharge on Asian cargo to the remaining Mediterranean, North African and Black Sea ports.",
             "Drewry counts eight blank sailings on Asia–Europe/Med next week, up from five, and still expects those rates to “increase slightly in the coming weeks”. Xeneta's chief analyst Peter Sand is less convinced: “gravity always wins”.",
         ], "src": ["drewry", "freightos10", "xeneta13", "cn_hapag_fak", "cn_msc_fak", "cn_msc_sur"],
         "why": "A published tariff is a carrier's opening position, not the market. With the gap at roughly $1,800–2,400 per 40ft, Asia–Egypt importers have room to negotiate below December's tariffs, but only with an all-in quote that names every surcharge."},
    ], [
        {"k": "chart", "type": "hbar", "width_mm": 66, "max": 7400, "prefix": "$",
         "sub": "US$ per 40ft · Asia → Egypt / East Med", "title": "Spot vs December tariff",
         "legend": [["spot", "Spot index (market average)"], ["gold", "Published tariff (FAK)"]],
         "rows": [["Drewry · Shanghai → Genoa · 12 Nov", 4168, "spot"], ["Freightos FBX13 · Asia → Med · 10 Nov", 4300, "spot"],
                  ["Xeneta · Far East → Med · 13 Nov", 4666, "spot"], ["MSC FAK · Far East → E. Med · 1 Dec", 6500, "gold"],
                  ["Hapag-Lloyd FAK · → Egypt/E. Med · 1 Dec", 6600, "gold"]],
         "note": "Spot = weekly market averages. FAK = published base tariff, port to port, before local charges and some surcharges.",
         "src": ["drewry", "freightos10", "xeneta13", "cn_msc_fak", "cn_hapag_fak"]},
        {"k": "panel", "kicker": "Transpacific", "title": "US rates slide as GRIs fail", "blocks": [
            P("Shanghai–New York fell 3% to $9,020 and Shanghai–Los Angeles 2% to $7,416, Drewry's lowest readings since August and September. Freightos says “significant carrier GRIs failed to materialize”, leaving Asia–US East Coast at about $9,700.", ["drewry", "freightos10"]),
        ]},
    ]]},
    {"k": "table", "caption": "December rate actions · as announced", "head": ["Carrier", "Trade", "Charge", "Amount", "Effective"], "num_cols": [3],
     "rows": [
         {"cells": ["Hapag-Lloyd", "Far East → Egypt, Türkiye, East Med", "FAK", "$5,300 / $6,600 (20' / 40')", "1 Dec"], "src": ["cn_hapag_fak"]},
         {"cells": ["Hapag-Lloyd", "Far East → Black Sea (highest)", "FAK", "$5,450 / $6,800", "1 Dec"], "src": ["cn_hapag_fak"]},
         {"cells": ["MSC", "Far East → East Med", "FAK", "$5,100 / $6,500 (+$800 on 40')", "1–14 Dec"], "src": ["cn_msc_fak"]},
         {"cells": ["MSC", "Far East → Algeria / Libya / Tunisia", "FAK", "$8,200 / $8,000 / $8,000 (40')", "1–14 Dec"], "src": ["cn_msc_fak"]},
         {"cells": ["MSC", "Asia → remaining Med, N. Africa, Black Sea ports", "Piracy risk + Suez surcharge", "$55 + $36 = $91 per TEU", "15 Nov"], "src": ["cn_msc_sur"]},
         {"cells": ["Maersk", "Far East → North Europe", "Peak season surcharge", "$500 / $1,000", "1 Dec"], "src": ["cn_maersk_pss"]},
         {"cells": ["CMA CGM", "North Europe → North Africa", "Surcharge", "€150 per TEU", "7 Nov"], "src": ["cn_cma_oct"]},
     ], "note": "Tariff figures as reported by Container News. Hapag-Lloyd's FAK includes Marine Fuel Recovery; security surcharges, THC and local charges may apply on top. Confirm with the carrier that your Egyptian port of discharge falls in the zone quoted."},
]}

# ------------------------------------------------------------------ page 4: lanes & carriers
p4 = {"section": "Suez & Hormuz", "title": "Suez & Hormuz", "label": "Two straits · services · security", "blocks": [
    {"k": "grid", "cols": "1.2fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "Suez Canal", "head": "The canal's comeback, service by service",
         "deck": "Every major alliance now has at least one service through Suez again. Most North Europe loops are still on the Cape.",
         "text": [
             "Evergreen's 16,556 TEU *Ever Eon* transited northbound on 8 November, the carrier's first Suez passage since it suspended Red Sea routings in December 2023. A week later, on 15 November, ONE's 8,110 TEU *ONE Continuity* crossed southbound on the Premier Alliance FE1 loop. Suez Canal Authority chairman Ossama Rabiee said three more Premier Alliance services will switch from the Cape to the canal; Freightos expects Yang Ming in December and full alliance returns by Q1 2027.",
             "Maersk and Hapag-Lloyd moved their joint ME1 India–Europe service to Suez in early November. Hapag-Lloyd now routes five Far East–South Europe services, one Far East–North Europe service and two India–Europe services through the canal; its other North Europe services still sail via the Cape.",
             "The money is following. Canal revenue reached $724m in October, up 94% year on year and the highest since the Red Sea crisis began, on transits up 32% to 1.5k. Xeneta counts 467,297 TEU of weekly capacity committed to the Red Sea in October: half the pre-crisis level, and roughly double the end-of-August figure.",
         ], "src": ["sb_evergreen", "cn_one", "fbx_page", "gc_hapag", "eam_suez_oct", "xeneta_summit"],
         "why": "The services recovering first are the ones that pass Egypt: Asia–South Europe and India–Europe. Check each booking's routing (Suez or Cape) rather than assume it."},
    ], [
        {"k": "box", "kicker": "New calls at Egyptian ports", "title": "Sokhna, Port Said, Damietta, Alexandria", "blocks": [
            {"k": "ticks", "items": [
                "**Summit Shipping CRS:** weekly China–Red Sea loop with eight 2,000 TEU ships: Shanghai, Ningbo, Nansha, Jeddah, Aqaba, **Sokhna**. Start date not announced.",
                "**Evergreen OGRD:** four ad hoc China sailings calling Jeddah, **Sokhna** and Aqaba.",
                "**Yang Ming EG1–EG3:** slots on DP World feeders linking **Port Said, Damietta and Alexandria**.",
                "**MSC North India–Red Sea:** Mundra, Port Qasim, Jeddah, King Abdullah Port, with 2,500–3,000 TEU ships from late November.",
            ], "srcs": [["cn_summit"], ["cn_evergreen_sched"], ["cn_yangming"], ["cn_msc_redsea"]]},
            P("Flexport, quoted by The Loadstar, warns that ships arriving via Suez and the Cape together could push North Europe arriving capacity to 131% of normal in week 47.", ["ls_suez_cong"]),
        ]},
    ]]},
    {"k": "rule"},
    {"k": "h", "text": "The other strait: Hormuz"},
    {"k": "flow", "n": 2, "blocks": [
        P("UKMTO's latest weekly count, reported on 13 November, was 139 outbound and 169 inbound Hormuz transits, with traffic about 65% below pre-conflict levels and eight incidents, seven of them tanker attacks. The Joint Maritime Information Center has logged 181 incidents since 1 March and about 211 ships waiting at anchor east of the strait.", ["gc_gulf_oil", "gc_ablaze"]),
        {"k": "tiles", "cols": 2, "items": [
            {"value": "139 / 169", "label": "outbound / inbound transits in UKMTO's latest week", "asof": "reported 13 Nov", "src": ["gc_gulf_oil"]},
            {"value": "~211", "label": "commercial ships at anchor east of Hormuz (JMIC)", "asof": "12 Nov", "src": ["gc_ablaze"]},
            {"value": "18.4m b/d", "label": "Gulf oil exports ex-Oman in October, 26% below pre-war (IEA)", "asof": "October", "src": ["gc_gulf_oil"]},
            {"value": "~34/day", "label": "US-assisted transits (NCAGS, 96-hour window)", "asof": "JMIC, 12 Nov", "src": ["gc_ablaze"]},
        ]},
        P("On 11 November the tanker *Dominica Prosperity* was hit about 14nm north-west of Ras Al Khaimah; all 22 crew were evacuated. Iranian state media said an LNG tanker (13 Nov) and an oil tanker (14 Nov) struck mines on “unauthorized” routes. Reuters could not immediately verify the second claim. Washington Institute data cited by Reuters count at least 10 ships hit on 1–10 November, after 37 attacks in October.", ["gc_ablaze", "gc_lng_mine", "gc_mine"]),
        {"k": "html", "html": '<div class="why"><b>Why it matters</b>Cargo for Jebel Ali or Dammam still carries war-risk exposure and anchorage delays. For now, Egypt–Gulf trade is better served via Saudi Red Sea ports or Gulf bypass ports with a trucking leg (see page 11).</div>'},
    ]},
]}

# ------------------------------------------------------------------ page 5: carriers & costs
p5c = {"section": "Carriers & costs", "title": "Carriers & costs", "label": "Q3 results · fuel · outlook · other gateways", "blocks": [
        {"k": "table", "caption": "Carrier results · Q3 2026", "head": ["Carrier", "Q3", "Outlook"],
         "rows": [
             {"cells": ["Maersk", "Revenue $18.1bn (+27%); EBIT $3.27bn, below the $3.61bn estimate", "FY underlying EBITDA $14.0–14.5bn; 26 × 18,600 TEU LNG ships ordered"], "src": ["fw_maersk", "gc_maersk_lng"]},
             {"cells": ["Hapag-Lloyd", "Net profit $999m (vs $172m); $1,808/TEU (+28%)", "FY EBITDA $4.6–5.0bn; Q4 “better than expected”"], "src": ["gc_hapag"]},
             {"cells": ["CMA CGM", "Net profit $2.32bn (vs $760m); revenue $18.4bn (+31.1%)", "6.5m TEU carried (+5.5%)"], "src": ["gc_cmacgm"]},
             {"cells": ["ONE", "Jul–Sep net profit $1.318bn; revenue $6.27bn", "FY net forecast raised to $2bn"], "src": ["fw_one"]},
         ], "note": "Maersk shares fell as much as 11.6% on the day; its guidance implies Q4 slightly below Q3."},
    {"k": "grid", "cols": "1fr 1fr", "gap": "8mm", "columns": [[
        brief("Fuel", "Bunkers stay expensive", "Ship & Bunker's Global 20 Ports average put VLSFO at $863.50 per tonne on 13 November (Singapore $882.50, Fujairah $856.50, Rotterdam $743.50) and MGO at $1,426.50. MABUX says its VLSFO index rose $70.81 in October to $913.07.", ["sb_prices", "cn_mabux"],
              "Suez routings burn less fuel than the Cape. Fuel recovery charges should follow, slowly."),
        brief("Outlook", "2027: the capacity wave", "Xeneta forecasts global spot rates 30% lower in 2027 and long-term rates 5% lower, against Q3 2026. It expects fleet growth of 6.8% against demand growth of 2.5–4%, and says the Suez return has already released 599k TEU of capacity.", ["xeneta_summit"],
              "Avoid locking Q4 2026 price levels into long 2027 contracts. Shorter or index-linked terms keep the upside.")
    ], [
        {"k": "brief", "tag": "Panama", "head": "34 slots a day, 50ft draft restored", "text": ["The Panama Canal Authority raised daily transit capacity from 33 to 34 slots and restored the 15.24m (50ft) Neopanamax draft, citing improved lake levels."], "src": ["gc_panama"]},
        {"k": "brief", "tag": "US West Coast", "head": "Watchmen strike deadline moves to 20 November", "text": ["Talks between the PMA and ILWU Local 26 now run to 20 November; Local 26 works terminals handling about 85% of Long Beach cargo. Los Angeles handled a record 1,026,872 TEU in October."], "src": ["gc_la_strike", "gc_la_record"]},
        {"k": "chart", "type": "hbar", "width_mm": 76, "max": 1000, "prefix": "$", "dp": 2,
         "sub": "Ship & Bunker · VLSFO, US$ per tonne · 13 Nov", "title": "What a tonne of fuel costs",
         "rows": [["Singapore", 882.5, "spot"], ["Global 20 Ports average", 863.5, "gold"], ["Fujairah", 856.5, "spot"], ["Rotterdam", 743.5, "spot"]],
         "note": "MGO averaged $1,426.50 per tonne; Brent was $96.33 a barrel.", "src": ["sb_prices"]},
    ]]},
    {"k": "panel", "kicker": "Rockit explains · in one paragraph", "title": "Why spot and tariff diverge in a reopening", "blocks": [
        P("When ships return to a shorter route, the same fleet can make more voyages, so effective capacity rises before demand does. Spot rates, set by cargo chasing space week by week, react first. Tariffs and surcharges, set by carriers trying to protect revenue, react last. Xeneta estimates the Suez return has already released 599k TEU of capacity and forecasts spot rates 30% lower in 2027. The gap between index and tariff is the negotiating room.", ["xeneta_summit"]),
    ]},
]}

# ------------------------------------------------------------------ page 5: air & logistics
p5 = {"section": "Air cargo", "title": "Air cargo", "label": "Peak season · rates · capacity", "blocks": [
    {"k": "grid", "cols": "1.2fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "Air freight", "head": "A peak season priced like one",
         "deck": "Rates are at their 2026 high, fuel has doubled, and Gulf capacity is still 18% short of pre-war.",
         "text": [
             "The Baltic Air Freight Index rose 5.3% in the four weeks to 2 November, leaving it 22.8% above last year and above the highest points of the previous two peak seasons, TAC Index says. In the week to 9 November it rose another 6.6% to its highest level of 2026, with “chunky gains” from Europe on routes including to the UAE.",
             "IATA's September data show demand (CTK) up 7.7% against capacity up 2.7%, lifting the global load factor to 47.9%. Middle Eastern carriers had the weakest demand growth, +3.8%, while adding 7.0% capacity; Europe–Middle East traffic fell 18.0%. Jet fuel was 103.4% above a year earlier.",
             "WorldACD's October figures put Africa-origin spot rates at $3.11/kg, up 60% year on year, as tight capacity and fuel surcharges met the start of the perishables export season. Capacity to and from Arabian Gulf markets was still 18% below its pre-war level. Xeneta sees few signs of a further Christmas surge and expects some cargo to shift back to ocean from Q2 2027.",
         ], "src": ["tac_nov", "acn_rates", "iata_sep", "st_wcd", "acn_xen"],
         "why": "Egyptian perishables and urgent-parts shippers should book capacity now and budget for fuel surcharges well above last year. Express heavyweight services are a fallback when general cargo space runs out."},
    ], [
        {"k": "chart", "type": "vbar", "width_mm": 76, "height_mm": 38, "min": 0, "max": 13, "suffix": "%", "dp": 1,
         "sub": "IATA · September 2026 · demand (CTK) y/y", "title": "Who flew more cargo",
         "rows": [["N. Am.", 11.8], ["Asia-Pac", 8.6], ["Global", 7.7], ["Lat. Am.", 6.7], ["Africa", 4.7], ["Europe", 4.5], ["Mid. East", 3.8]],
         "note": "Middle East carriers grew capacity 7.0% against demand 3.8%; African carriers' capacity fell 1.2%.", "src": ["iata_sep"]},
        {"k": "box", "kicker": "This week", "title": "Shenzhen: no belly cargo, 16–20 Nov", "blocks": [
            P("For the APEC leaders' meeting on 18–19 November, international passenger flights at Shenzhen airport may not carry belly cargo from midnight on 16 November until 6pm on 20 November, local time. Dangerous-goods trucks are also barred from city roads.", ["ls_shenzhen"]),
            P("**Rockit's read:** route South China air exports via Guangzhou or Hong Kong this week, and expect knock-on pressure there."),
        ]},
    ]]},
    {"k": "rule"},
    {"k": "grid", "cols": "1fr 1fr", "gap": "9mm", "columns": [[
        {"k": "chart", "type": "hbar", "width_mm": 78, "max": 40, "prefix": "+", "suffix": "%", "dp": 1,
         "sub": "TAC Index · Baltic Air Freight Index · year on year to 2 Nov", "title": "Air rates by origin",
         "rows": [["London Heathrow (BAI40)", 34.4, "spot"], ["Hong Kong (BAI30)", 28.0, "spot"], ["Frankfurt (BAI20)", 25.7, "spot"],
                  ["Global (BAI00)", 22.8, "gold"], ["Chicago (BAI50)", 17.9, "spot"], ["Shanghai (BAI80)", 14.4, "spot"]],
         "note": "TAC also reports rates from India up about 80% year on year.", "src": ["tac_nov"]},
    ], [
        {"k": "chart", "type": "hbar", "width_mm": 78, "max": 12, "prefix": "+", "suffix": "%",
         "sub": "WorldACD · chargeable weight by origin · October y/y", "title": "Africa and MESA lead tonnage growth",
         "rows": [["Africa", 10, "gold"], ["Middle East & South Asia", 10, "spot"], ["Asia Pacific", 7, "spot"],
                  ["Worldwide", 6, "spot"], ["North America", 5, "spot"], ["Europe", 4, "spot"]],
         "note": "Capacity to and from Arabian Gulf markets was still 18% below pre-war levels in week 44.", "src": ["st_wcd"]},
    ]]},
]}

# ------------------------------------------------------------------ page 6: the logistics business
p6l = {"section": "The logistics business", "title": "The logistics business", "label": "Forwarders · deals · e-commerce · technology", "blocks": [
    {"k": "box", "kicker": "Rockit's read", "title": "What the forwarder results mean for you", "style": "margin-bottom:4mm", "blocks": [
        P("The big forwarders are earning more from air freight by choosing which cargo to carry: tech and hyperscaler freight gets space first, and DSV says it is trading volume for yield. Smaller shippers should hold block-space or allocation agreements, or work through a forwarder that does. Consolidation among mid-tier forwarders also means agency networks will change; check who your partner's partner is."),
    ]},
    {"k": "table", "caption": "Forwarders' Q3 2026 · the air boom shows up in profits", "head": ["Company", "Group result", "Air freight", "Note"],
     "rows": [
         {"cells": ["DHL Group", "EBIT €1.7bn (+16.2%); 2026 guidance raised to more than €7.0bn", "Forwarding air volumes 497,000t (+12%)", "Express earned about €100m extra from tight air capacity"], "src": ["st_dhl", "acn_dgf"]},
         {"cells": ["Kuehne+Nagel", "EBIT CHF 435m (+53%)", "Air EBIT CHF 169m (+84%); volumes +10%", "Driven by hyperscaler and semiconductor customers"], "src": ["st_kn"]},
         {"cells": ["DSV", "EBIT before special items DKK 6.61bn (+19.5%)", "Volumes −3%; gross profit per tonne +8%", "Schenker integration: about 9,000 jobs cut; road EBIT −35.1%"], "src": ["st_dsv"]},
         {"cells": ["Expeditors", "Operating income $445.4m (+55%)", "Air tonnage +13% (September +19%)", "Led by South Asia exports and hyperscalers"], "src": ["acn_expd"]},
     ], "note": "DSV and Kuehne+Nagel reported on 21–22 October; DHL and Expeditors on 3–5 November."},
    {"k": "flow", "n": 2, "blocks": [
        brief("E-commerce", "Europe's de minimis ends, parcels drop", "Since the EU's €3 duty on parcels under €150 began on 1 July, Asia–Europe e-commerce air volumes fell 61% year on year in Q3 (Xeneta). WorldACD reports a further €2-per-item EU handling fee from 1 November, expected to cut volumes further.", ["acn_xen", "st_wcd"]),
        brief("Deals", "Mid-tier forwarders consolidate", "Denmark's Scan Global Logistics agreed to buy OIA Global (1,200 staff, 30+ countries), aiming for the global top 20; closing is expected in Q1 2027. AIT Worldwide completed its purchase of Australia's Connor Anderson.", ["acn_scan", "acn_ait"]),
        brief("Technology", "Quotes in minutes, B/Ls on screen", "CH Robinson says AI agents cut air quotes from a day, and ocean quotes from two to three days, to two to three minutes. DCSA reports Korea's eBL platform completed full-lifecycle tests with HMM, with live shipments targeted within 2026.", ["acn_chr", "dcsa_korea"]),
        brief("Sustainability", "DHL Express flies SAF out of Paris, including to Casablanca", "DHL Express signed a one-year deal with TotalEnergies for 5m litres of sustainable aviation fuel on flights from Paris CDG to Leipzig, Casablanca, Milan and London, cutting about 11,800t of CO₂e a year. SAF was 10% of fuel on DHL's own fleet in 2025.", ["acn_saf"],
              "European buyers that report Scope 3 emissions may start asking Egyptian exporters for lower-carbon transport options."),
        brief("Carriers in logistics", "Maersk's logistics arm outgrows its ships", "Maersk's Logistics & Services revenue rose 13% in Q3 and its EBIT margin improved to 5.8%, while ocean volumes slipped about 1%, FreightWaves reports.", ["fw_maersk"]),
        brief("People", "DHL names a Sub-Saharan Africa forwarding chief", "DHL Global Forwarding appointed Sascha Geiken CEO for Sub-Saharan Africa (excluding South Africa) on 10 November.", ["acn_geiken"]),
    ]},
]}

# ------------------------------------------------------------------ page 6: geopolitics & policy
p6 = {"section": "Geopolitics & trade policy", "title": "Geopolitics & trade policy", "label": "The 9 January cliff", "blocks": [
    {"k": "grid", "cols": "1.15fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "Washington & Beijing", "head": "Every deadline now lands on 9 January",
         "deck": "Both sides of the US–China truce, and the US port fees on Chinese ships, expire within a day of each other.",
         "text": [
             "The US Trade Representative suspended its Section 301 port fees on Chinese-built and Chinese-operated ships for two more months, to 11:59pm ET on 9 January 2027 (91 FR 72608, published 10 November). The same day it extended all 178 remaining product exclusions in the main Section 301 China tariff case to the same date.",
             "China mirrored the move. Its 24% additional tariff on US goods stays suspended for two more months (a 10% tariff remains), and its port fees on US-linked ships and critical-mineral export waivers run to 10 January. Reuters reported that Xi and Trump were expected to meet at the APEC summit in Shenzhen on 18–19 November.",
             "The tariffs struck down in February stay in the news. After the Supreme Court ruled the IEEPA tariffs unlawful, UPS has gone to the Court of International Trade to force refunds on finally liquidated entries; The Loadstar reports UPS has received about $500m and still owes customers $270m. China's commerce ministry noted that Washington intends to use Section 301 tariffs to replace the IEEPA duties. On Section 232, the White House chose 180 days of talks rather than tariffs on robotics and industrial machinery.",
         ], "src": ["fr_portfee", "fr_excl", "gc_portfee", "gc_truce", "ls_ups", "fr_232", "scd_232"],
         "why": "US-lane quotes that run past 9 January need a surcharge clause. Egyptian exporters who shipped DDP to the US should check who was importer of record: refund rights follow that name."},
    ], [
        {"k": "table", "caption": "Policy tracker", "head": ["Issue", "Status", "Next date"],
         "rows": [
             {"cells": ["US port fees on Chinese ships (Section 301)", "Suspended", "9 Jan 2027"], "src": ["fr_portfee"]},
             {"cells": ["China's 24% extra tariff on US goods", "Suspended (10% stays)", "10 Jan 2027"], "src": ["gc_truce"]},
             {"cells": ["US Section 232: robotics & machinery", "Talks, no tariff yet", "Report in 180 days"], "src": ["fr_232"]},
             {"cells": ["IMO Net-Zero Framework", "Back on the agenda", "MEPC 85: 30 Nov–3 Dec"], "src": ["imo_ghg"]},
             {"cells": ["EU CBAM (steel, aluminium, cement, fertiliser…)", "Definitive; Q3 price €82.32", "Q4 price 4 Jan 2027"], "src": ["ec_cbam_price"]},
             {"cells": ["EU ETS for shipping", "100% of 2026 emissions", "Incl. methane and N₂O"], "src": ["gc_ets"]},
             {"cells": ["Strait of Hormuz", "Restricted; traffic −65%", "No deal in sight (FGE)"], "src": ["gc_gulf_oil", "gc_fge"]},
         ]},
        {"k": "panel", "kicker": "Energy", "title": "Diesel at $180, Iran's exports near zero", "blocks": [
            P("The IEA says Gulf oil exports excluding Oman were 18.4m barrels a day in October, 26% below pre-war. European diesel is near $180 a barrel, about 77% above pre-war. Iranian crude exports have dwindled to almost nothing under the US naval blockade, and FGE's Fereidun Fesharaki says “we are not close to a resolution”.", ["gc_gulf_oil", "gc_fge"]),
        ]},
    ]]},
    {"k": "rule"},
    {"k": "kicker", "text": "Eight weeks to the January cliff · key dates from this issue"},
    {"k": "html", "html": TIMELINE},
    {"k": "p", "text": "Sources: Federal Register; Reuters via gCaptain; IMO; EnterpriseAM; European Commission. Full references on pages 14–15.", "src": ["fr_portfee", "gc_truce", "imo_ghg", "eam_imf", "eam_cbe", "eam_rebate", "ec_cbam_price", "ls_shenzhen"], "cls": "srcline"},
]}

# ------------------------------------------------------------------ page 9: geopolitics II
p9g = {"section": "Geopolitics & trade policy", "title": "War, sanctions & carbon", "label": "Geopolitics · continued", "blocks": [
    {"k": "grid", "cols": "1fr 1.15fr", "gap": "9mm", "style": "margin-bottom:3mm", "columns": [[
        {"k": "chart", "type": "vbar", "width_mm": 72, "height_mm": 36, "min": 0, "max": 90, "prefix": "€", "dp": 2, "kind": "gold",
         "sub": "European Commission · CBAM certificate price, 2026", "title": "Carbon at the EU border",
         "rows": [["Q1", 75.36], ["Q2", 75.28], ["Q3", 82.32]],
         "note": "Per certificate (one tonne of CO₂e). Q4 price due 4 January 2027.", "src": ["ec_cbam_price"]},
    ], [
        {"k": "kicker", "text": "The war at sea in four numbers"},
        {"k": "tiles", "cols": 2, "items": [
            {"value": "133", "label": "incidents confirmed by the IMO since 28 February", "asof": "as of 10 Nov", "src": ["gc_imo_council"]},
            {"value": "25", "label": "seafarers killed in those incidents", "asof": "IMO Council", "src": ["gc_imo_council"]},
            {"value": "181", "label": "maritime security incidents logged by JMIC since 1 March", "asof": "12 Nov", "src": ["gc_ablaze"]},
            {"value": "37", "label": "attacks on ships in October, the most of the war", "asof": "Washington Institute via Reuters", "src": ["gc_mine"]},
        ]},
    ]]},
    {"k": "flow", "n": 2, "blocks": [
        brief("War at sea", "IMO: 133 incidents, 25 seafarers killed", "The IMO Council (2–6 Nov) condemned Houthi attacks in the Red Sea and Bab al-Mandab and Russian attacks on Ukraine's Black Sea corridor. The IMO counts 133 confirmed incidents and 25 seafarer deaths since the conflict began on 28 February; on 11 November its Secretary-General urged strict SOLAS enforcement in Hormuz.", ["gc_imo_council", "gc_imo_solas"],
              "Keep war-risk and deviation clauses in Red Sea contracts even as carriers return."),
        brief("Black Sea", "Russia claims hits on three cargo ships", "Russia's defence ministry said overnight strikes, reported on 8 November, hit a container ship at Odesa, another at Chornomorsk and a dry-cargo ship south-west of Odesa. Reuters could not verify the claims, and Ukraine did not immediately comment.", ["gc_russia3"],
              "Egypt buys Black Sea wheat; insurance and freight on that corridor stay high."),
        brief("Sanctions", "US and EU rules on Russia diverge", "The tanker *Agioi Fanendes*, carrying about 40,000t of Russian diesel under last month's Putin–Trump supply deal, made a U-turn about 400nm off New York. Bloomberg tracking shows no Russian diesel cargo has yet reached the US.", ["gc_rudiesel"],
              "Screen Russia-linked cargo and tonnage against US, EU and UK lists separately."),
        brief("Carbon · IMO", "Net-Zero Framework returns", "The IMO set MEPC 85 for 30 Nov–3 Dec. gCaptain reported in September that the framework could return for adoption at an extraordinary session on 4 December. If adopted, it enters into force 16 months later for ships over 5,000 GT.", ["imo_ghg", "gc_nzf", "imo_faq"]),
        brief("Carbon · EU", "CBAM certificates get pricier", "The Commission's CBAM certificate price rose to €82.32 for Q3, from €75.28 in Q2. Certificates will be bought on a central platform from February 2027, and the first declarations are due by 30 September 2027. Importers of more than 50t of CBAM goods need declarant status.", ["ec_cbam_price", "ec_cbam_def"]),
        brief("Carbon · shipping", "EU ETS now bills 100%", "Shipping lines surrendered allowances for 70% of verified 2025 emissions on 30 September. For 2026 emissions the share is 100%, and methane and nitrous oxide are now included.", ["gc_ets"],
              "Check ETS surcharges on Egypt–EU legs in 2027 tariffs."),
    ]},
]}

# ------------------------------------------------------------------ page 7: Egypt desk
p7 = {"section": "Egypt desk", "title": "Egypt desk", "label": "Rebates · money · ports · industry", "blocks": [
    {"k": "grid", "cols": "1.15fr 1fr", "gap": "8mm", "columns": [[
        {"k": "lead", "kicker": "Exports", "head": "Cairo will pay half the freight, if the file is complete",
         "deck": "A revamped rebate programme gives freight its own support line, and refuses incomplete files.",
         "text": [
             "The Cabinet approved the revamped export rebate programme on 5 November. Support rises by an average of 35%, and the new rates already apply to shipments from the start of November; free-zone exporters are excluded. For the first time, freight has its own line: the state covers 50% of sea and land freight to Africa, Latin America, Australia, Southeast Asia and Russia, and for agricultural exports 25% of air freight to Europe and 50% to the UK.",
             "The programme also pays 25% of domestic transport, of cargo insurance and of express-vessel invoices. The US and 11 Southeast Asian countries join the target-market list. Exporters must submit complete files before they are accepted. Phase one runs to the end of 2026 and phase two starts in July 2027. The FY 2026/27 budget earmarks EGP 48bn for export support, against EGP 28bn actually paid out last year.",
         ], "src": ["eam_rebate"],
         "why": "Freight invoices, B/Ls and insurance certificates are now part of the exporter's cash flow. Ask your forwarder for claim-ready documents from the first shipment."},
    ], [
        {"k": "chart", "type": "hbar", "width_mm": 68, "max": 100, "suffix": "%",
         "sub": "Share of cost paid by the state · from November", "title": "Half the freight, paid by Cairo",
         "rows": [["Sea & land freight → Africa, Lat. Am., SE Asia, Australia, Russia", 50, "gold"], ["Air freight → UK (agricultural)", 50, "gold"],
                  ["Air freight → Europe (agricultural)", 25, "gold"], ["Domestic transport", 25, "gold"], ["Cargo insurance", 25, "gold"], ["Express-vessel invoices", 25, "gold"]],
         "note": "On top of rebates raised 35% on average. Free-zone exporters excluded.", "src": ["eam_rebate"]},
        {"k": "space", "mm": 2},
        {"k": "kicker", "text": "Trade in one glance · FY 2025/26"},
        {"k": "tiles", "cols": 2, "items": [
            {"value": "$37.3bn", "label": "non-oil exports, up 7.8%", "asof": "FY 2025/26", "src": ["eam_rebate"]},
            {"value": "$64.8bn", "label": "trade deficit, up 27.1%", "asof": "FY 2025/26", "src": ["eam_rebate"]},
            {"value": "$38.2bn", "label": "remittances, Jan–Sep 2026: a record", "asof": "CBE", "src": ["eam_remit"]},
            {"value": "EGP 48bn", "label": "export-support budget, FY 2026/27 (vs EGP 28bn paid last year)", "asof": "budget", "src": ["eam_rebate"]},
        ]},
    ]]},
    {"k": "grid", "cols": "1.1fr 1fr", "gap": "9mm", "columns": [[
        {"k": "chart", "type": "hbar", "width_mm": 72, "max": 64, "dp": 2,
         "sub": "EGP per USD · readings and bank forecasts", "title": "Where the pound stands",
         "rows": [["Record high, October", 56.35, "spot"], ["Close, 5 November", 53.97, "spot"], ["CBE quote, 12 November", 53.39, "spot"],
                  ["Goldman Sachs, 12-month forecast", 50, "gold", "50"], ["Deutsche Bank, if the war ends", 48, "gold", "48"],
                  ["Deutsche Bank, if the war escalates", 60, "gold", "60+"]],
         "note": "Higher = weaker pound. Forecasts are the banks' own scenarios, not ours.", "src": ["eam_rebate", "eam_db", "eam_gs"]},
    ], [
        {"k": "kicker", "text": "Money · your landed cost"},
        {"k": "tiles", "cols": 2, "items": [
            {"value": "20.0%", "label": "CBE deposit rate: +100bp on 29 Oct, the first hike since March 2024", "asof": "next MPC 17 Dec", "src": ["eam_cbe"]},
        {"value": "12.7%", "label": "Urban inflation in October (core 13.1%); third monthly fall", "asof": "CAPMAS", "src": ["eam_infl"]},
        {"value": "$2.3bn", "label": "IMF final reviews to land before the programme ends on 15 Dec", "asof": "talks now virtual", "src": ["eam_imf"]},
        {"value": "47.2", "label": "PMI in October; firms cite shipping delays and slower customs", "asof": "10th month below 50", "src": ["eam_pmi"]},
        ]},
    ]]},
]}

# ------------------------------------------------------------------ page 11: Egypt & region
p11e = {"section": "Egypt desk", "title": "Egypt & the region", "label": "Industry · FX · ports · neighbours", "blocks": [
    {"k": "flow", "n": 2, "blocks": [
        brief("FX outlook", "Banks split on the pound", "Deutsche Bank sees the pound at 48 per dollar if the US–Iran war ends and beyond 60 if it escalates, and expects the CBE to hold rates. It says it has not heard of “significant import delays” from FX shortages. Remittances hit a record $38.2bn in January–September.", ["eam_db", "eam_remit"],
              "Freight is billed in dollars. Watch quote validity and FX clauses."),
        brief("Industry", "Gas rationing deepens", "Gas cuts for fertiliser and methanol plants rose to 33%, and Ezz Steel was notified of a 30% cut, per Asharq Business (disputed by an industry source). Five of 15 November LNG cargoes were deferred, and urea is fetching about $535/t.", ["eam_gas"],
              "Expect lumpier urea, ammonia and methanol export volumes; confirm cargo readiness."),
        brief("SCZone", "Sokhna gets a digital truck yard", "SCZone hired Telecom Egypt to upgrade networks at East Port Said and Sokhna. A Nafeza-run digital truck yard at Sokhna will handle up to 1.1k trucks a day, and Sailun's $804m tyre plant rolled out its first tyre.", ["eam_sczone"]),
        brief("EU", "CBAM bill: about $317m a year", "Egypt is asking Brussels for a phased CBAM timetable. Environment Ministry studies put the cost of non-compliance at about $317m a year, of which steel accounts for $236m. Separately, the EU plans to recognise Egyptian e-signatures, a first outside Europe.", ["eam_cbam", "eam_imf"]),
        brief("Gulf", "Around Hormuz by truck", "DP World has moved more than 1m TEU overland from UAE east-coast ports since March, about 3.5k TEU a day. AD Ports posted record Q3 net income of AED 975m, while UAE container throughput fell 57%. GCC states signed the framework for a 2.1k-km railway.", ["eam_dpw", "eam_adports", "eam_gccrail"],
              "Quote Gulf cargo via Khorfakkan, Fujairah or Sohar plus trucking, or via Saudi Red Sea ports."),
        brief("State finances", "A gate on public FX spending", "The Cabinet approved three months of spending rationalisation: any state spending with a foreign-currency component now needs Finance Ministry approval, coordinated with the CBE.", ["eam_rebate"]),
        brief("Rail", "Sinai freight line gathers pace", "Egypt is accelerating construction of a 341km railway linking Bir al-Abd, Arish and Taba, Daily News Egypt reports.", ["dne_sinai"]),
        brief("Energy routes", "Iraqi crude looks for Red Sea and Med outlets", "Iraqi, Egyptian and Jordanian officials discussed new Red Sea and Mediterranean outlets for Iraqi crude, including the $4.6bn Basra–Haditha pipeline (about 2.3m barrels a day). No terminals or timetable were named.", ["eam_iraq"]),
        brief("United States", "Cairo takes US trade barriers to the USTR", "Investment and Foreign Trade Minister Mohamed Farid met US Trade Representative Jamieson Greer in Washington to review the economic partnership and discuss bilateral trade flows.", ["dne_farid"]),
        brief("Africa & Europe", "New doors open", "Sudan lifted its import ban on 44 of 46 goods and zeroed duties on staples. The PM proposed extending the Alexandria–Koper port partnership to Sokhna and Damietta. DP World starts a weekly China–East Africa link in late November.", ["eam_sudan", "dne_koper", "eam_dpw_africa"]),
    ]},
]}

# ------------------------------------------------------------------ page 8: toolkit
p8 = {"section": "The toolkit", "title": "The toolkit", "label": "Practical · reading a December quote", "blocks": [
    {"k": "box", "kicker": "Rockit explains", "title": "Anatomy of an Asia → Egypt ocean quote", "style": "margin-bottom:4mm", "blocks": [
        P("Spot indices, published tariffs and the number on your invoice are three different things. In December they are far apart, so it pays to know which line is which."),
        {"k": "html", "html": f'''<table class="t" style="color:#e7e3d3;margin-top:1mm"><tr><th style="color:#a9b1c2;border-color:#d6d2c2">Line</th><th style="color:#a9b1c2;border-color:#d6d2c2">What it is</th><th style="color:#a9b1c2;border-color:#d6d2c2">What to ask</th></tr>
<tr><td style="border-color:#2c3b5c"><b>Base freight</b></td><td style="border-color:#2c3b5c">FAK tariff, or a negotiated / index-linked rate</td><td style="border-color:#2c3b5c">Is this tariff, spot or contract? Which index is it linked to?</td></tr>
<tr><td style="border-color:#2c3b5c"><b>Fuel</b></td><td style="border-color:#2c3b5c">BAF or MFR: bunker cost recovery</td><td style="border-color:#2c3b5c">Is fuel included in the base? Which month's fuel price?</td></tr>
<tr><td style="border-color:#2c3b5c"><b>Surcharges</b></td><td style="border-color:#2c3b5c">Peak season (PSS), piracy-risk, Suez Canal, security, EU ETS on EU legs</td><td style="border-color:#2c3b5c">List every surcharge and its effective date</td></tr>
<tr><td style="border-color:#2c3b5c"><b>Routing</b></td><td style="border-color:#2c3b5c">Suez or Cape of Good Hope</td><td style="border-color:#2c3b5c">Which way does this service sail? Transit days?</td></tr>
<tr><td style="border-color:#2c3b5c"><b>Local charges</b></td><td style="border-color:#2c3b5c">THC, documentation, free time at Alexandria, Damietta, Port Said or Sokhna</td><td style="border-color:#2c3b5c">Free days for demurrage and detention?</td></tr>
<tr><td style="border-color:#2c3b5c"><b>Validity</b></td><td style="border-color:#2c3b5c">The date the price stops holding (MSC's December FAK: 14 Dec at the latest)</td><td style="border-color:#2c3b5c">Valid until which date: booking, loading or sailing?</td></tr></table>'''},
    ]},
    {"k": "grid", "cols": "1fr 1fr 1fr", "gap": "6mm", "columns": [[
        {"k": "kicker", "text": "If you import"},
        {"k": "ticks", "items": [
            "Benchmark every Asia quote against $4,168–4,666 per 40ft spot (Drewry, Freightos, Xeneta).",
            "Budget $91 per TEU for MSC's piracy and Suez surcharges from 15 November.",
            "File ACI data early: firms report slower customs procedures in October's PMI.",
            "Price FX risk: the pound moved 3 points in three weeks.",
        ]},
    ], [
        {"k": "kicker", "text": "If you export"},
        {"k": "ticks", "items": [
            "Check if your market is on the 50% freight-support list: Africa, Latin America, SE Asia, Australia, Russia.",
            "Keep freight, insurance and inland invoices claim-ready; incomplete files are refused.",
            "Perishables by air: Africa-origin spot is up 60%; book capacity early.",
            "Steel, aluminium, fertiliser or cement to the EU: prepare emissions data for CBAM.",
        ]},
    ], [
        {"k": "kicker", "text": "If you forward"},
        {"k": "ticks", "items": [
            "Quote December with hard validity, and state the routing on every booking.",
            "Add a 10 January clause to US-lane quotes (port-fee pause ends 9 Jan).",
            "Quote Gulf cargo via bypass ports or Saudi Red Sea gateways.",
            "Screen Russia-linked cargo against US, EU and UK lists separately.",
        ]},
    ]]},
    {"k": "rule"},
        {"k": "panel", "kicker": "Ask the desk", "title": "Send us a lane", "blocks": [
            P("Tell us origin, destination, commodity, volume and timing, and we will come back with an all-in quote that names every line above, with its routing and validity."),
            P("**inquiry@rockit.com.eg** · +20 2 2690 7601 · rockit-transport.com"),
            P("Offices in Cairo, Alexandria, Ain Sokhna, Port Said and Damietta."),
        ]},
]}

# ------------------------------------------------------------------ page 9: calendar & glossary
p9 = {"section": "Calendar & glossary", "title": "Calendar & glossary", "label": "Dates to diarise · words we use", "blocks": [
    {"k": "grid", "cols": "1.25fr 1fr", "gap": "8mm", "columns": [[
        {"k": "table", "caption": "The next eight weeks", "head": ["Date", "Event", "Why it matters"], "num_cols": [0],
         "rows": [
             {"cells": ["16–17 Nov", "WEF Country Strategy Meeting on Egypt, New Administrative Capital", "Investment and trade signals"], "src": ["eam_imf"]},
             {"cells": ["16–20 Nov", "Shenzhen airport: no belly cargo (APEC)", "Re-route South China air"], "src": ["ls_shenzhen"]},
             {"cells": ["18–19 Nov", "APEC leaders' meeting, Shenzhen", "Possible Xi–Trump meeting"], "src": ["ls_shenzhen", "gc_truce"]},
             {"cells": ["19–21 Nov", "Private Label Egypt, Cairo International Convention Center", "Contract manufacturing"], "src": ["eam_privlabel"]},
             {"cells": ["20 Nov", "LA/Long Beach ILWU Local 26 deadline", "Transpacific disruption risk"], "src": ["gc_la_strike"]},
             {"cells": ["Late Nov", "DP World China–Africa Link starts (weekly)", "New East Africa option"], "src": ["eam_dpw_africa"]},
             {"cells": ["30 Nov–3 Dec", "IMO MEPC 85, London", "Global carbon price for shipping"], "src": ["imo_ghg"]},
             {"cells": ["1 Dec", "Hapag-Lloyd and MSC December FAK; Maersk Asia–Europe PSS", "Asia–Egypt base rates"], "src": ["cn_hapag_fak", "cn_msc_fak", "cn_maersk_pss"]},
             {"cells": ["4 Dec", "Extraordinary MEPC session on the Net-Zero Framework (reported)", "Possible adoption"], "src": ["gc_nzf"]},
             {"cells": ["14 Dec", "MSC December FAK validity ends (latest)", "Re-quote mid-month"], "src": ["cn_msc_fak"]},
             {"cells": ["15 Dec", "Egypt's IMF programme expires", "About $2.3bn in reviews"], "src": ["eam_imf"]},
             {"cells": ["17 Dec", "CBE Monetary Policy Committee", "Rates and the pound"], "src": ["eam_cbe"]},
             {"cells": ["31 Dec", "Export rebate programme, phase one ends", "Phase two from July 2027"], "src": ["eam_rebate"]},
             {"cells": ["4 Jan 2027", "CBAM Q4 2026 certificate price published", "EU import costs"], "src": ["ec_cbam_price"]},
             {"cells": ["9–10 Jan 2027", "US port-fee pause and China's tariff truce end", "Transpacific surcharge risk"], "src": ["fr_portfee", "gc_truce"]},
             {"cells": ["Feb 2027", "CBAM certificates go on sale on the central platform", "EU importers start buying"], "src": ["ec_cbam_price"]},
         ]},
    ], [
        {"k": "kicker", "text": "Glossary"},
        {"k": "html", "html": "".join(f'<div style="padding:1.5mm 0;border-bottom:.5pt solid #e3d8bd;font-size:7.9pt;line-height:1.4"><b style="font:600 7.6pt IBM Plex Mono,monospace;color:#8a6514;letter-spacing:.06em">{k}</b> · {v}</div>' for k, v in [
            ("FAK", "Freight All Kinds: a carrier's published base rate for general cargo, regardless of commodity."),
            ("GRI", "General Rate Increase: an announced across-the-board rate rise; not always achieved in the market."),
            ("PSS", "Peak Season Surcharge: an add-on charged in busy periods."),
            ("BAF / MFR", "Bunker Adjustment Factor / Marine Fuel Recovery: the fuel component of a sea freight rate."),
            ("TEU / FEU", "Twenty- and forty-foot equivalent units: one 40ft box is two TEU."),
            ("WCI / FBX", "Drewry World Container Index and Freightos Baltic Index: weekly spot-rate benchmarks."),
            ("CTK / ACTK", "Cargo tonne-kilometres (demand) and available cargo tonne-kilometres (capacity) in air freight."),
            ("BAI00", "Baltic Air Freight Index, global: TAC Index's air rate benchmark."),
            ("Blank sailing", "A scheduled voyage a carrier cancels to cut capacity."),
            ("De minimis", "The value below which parcels enter a country duty-free; the EU removed it on 1 July 2026."),
            ("Section 301", "US trade law used for tariffs and port fees on China."),
            ("CBAM", "EU Carbon Border Adjustment Mechanism: a carbon price on imports of steel, aluminium, cement, fertiliser and more."),
            ("EU ETS", "EU Emissions Trading System, which now covers shipping emissions."),
            ("ACI / ACID", "Egypt's Advance Cargo Information system and the 19-digit ACID number every import needs before shipment."),
        ])},
    ]]},
]}

# ------------------------------------------------------------------ page 10: sources (last page)
p10 = {"section": "Sources", "title": "Sources", "label": "Every figure, footnoted", "sources_page": True, "blocks": [
    P("We read every page below between 9 and 16 November 2026. Where a source reports a claim by a party to a conflict, the text says so. Analysis, marked *Why it matters* or *Rockit's read*, is ours."),
]}

edition = {
    "meta": {"voyage": "001", "date_long": "16 November 2026", "pages_label": "Full edition · 16 pages", "title": "The Rockit Manifest · Voyage 001 · Full edition"},
    "sources": {k: {"name": v[0], "title": v[1], "date": v[2], "url": v[3]} for k, v in SOURCES.items()},
    "disclaimer": "The Rockit Manifest is published every Monday by Rockit Transport Services & Logistics (RTSL), Egypt. Figures come from the named public sources on the dates shown and may change. They are not a quotation or offer. Regulatory notes are summaries, not legal advice. © 2026 RTSL.",
    "cover": cover,
    "pages": [p2, p3, p4, p5c, p5, p6l, p6, p9g, p7, p11e, p8, p9, p10],
    "back": {
        "headline": "Rockit Transport Services & Logistics",
        "deck": "A Cairo freight forwarder moving air, ocean and inland cargo for exporters, importers, manufacturers and project shippers.",
        "columns": [
            {"h": "Services", "items": ["Air freight", "Ocean freight: FCL and LCL", "Inland freight: our own fleet", "Customs clearance", "Project logistics", "Supply chain & warehousing"]},
            {"h": "Offices", "items": ["Cairo (HQ)", "Alexandria", "Port Ain El Sokhna", "Port Said", "Damietta Port"]},
            {"h": "Free tools", "items": ["Container tracking", "Vessel schedules", "Load calculator", "Duties & taxes calculator", "Chargeable weight"]},
        ],
        "next": ["The export-rebate rules in practice, from the ministries' exporter briefing", "APEC in Shenzhen: what came out of US–China talks", "IMO MEPC 85: will shipping get a global carbon price?", "December's first rate moves, Asia → Egypt"],
        "cta_kicker": "Every Monday · rockit-transport.com/insights/categories/newsletter",
        "cta": "Send us a lane at **inquiry@rockit.com.eg** and get an all-in quote that names every line.",
    },
}
out = Path(__file__).with_name("edition.json")
out.write_text(json.dumps(edition, ensure_ascii=False, indent=1))
print("wrote", out)
