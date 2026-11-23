# Research desk: Egypt and MEA region (Mon 16 to Sun 22 November 2026)

Prepared Sunday 22 November 2026 for The Rockit Manifest, Issue 002 (publishes Monday 23 November).

**Method.** Stories were found with WebSearch, in English and Arabic. Every figure below was then read on a page fetched with plain `curl -sL` through the environment proxy, and the text was extracted with `python3 -I`. Raw files are in `/tmp/claude-0/-home-user/59036caf-5faf-5066-977d-66ff7505f5d6/scratchpad/w2/raw_egypt/`, and the file names are given per item. No figure comes from a search snippet alone. Where a search snippet was the only evidence, the item is marked UNVERIFIED and is listed at the end.

**Sources that worked this week:**
- enterpriseam.com, through the WordPress JSON API of the Egypt edition (`/egypt/wp-json/wp/v2/posts`) and the Infrastructure edition. Extracted text: `eam_eg.txt`, `eam_eg15.txt`, `eam_infra.txt`, `e_rebate.txt`.
- zawya.com, English and Arabic. Many English items are syndicated from Arab Finance and Daily News Egypt. Arabic Zawya currency stories are paywalled after the first paragraph, so only that lead paragraph was read. Extracted text: `zw.txt`; Arabic raw: `zar_*.html`.
- container-news.com and gcaptain.com, through their WordPress JSON APIs. Extracted text: `cn_all.txt`, `wp_gcaptain.com.txt`.

**Sources that did not work this week:** dailynewsegypt.com (it worked last week, now refused by the proxy), all official Egyptian hosts (cbe.org.eg WAF; mof.gov.eg, customs.gov.eg, sczone.eg, sis.gov.eg, cabinet.gov.eg, capmas.gov.eg refused), and every Arabic news site tried (Youm7, Amwal Al Ghad, Masrawy, El Balad, Veto, Al Mal, Banker, Maspero, Nile News, Akhbar El Yom). See the list at the end.

**Context.** The fetched pages still describe a regional war. "The US-Israeli war on Iran that began on 28 February" continues (EnterpriseAM, 17 Nov). This week the Yemen front reached Saudi Red Sea ports (item 10).

---

## 1. Export rebates: the 15 Nov exporter briefing went ahead; the rules on record are unchanged

**Summary.** The Finance and Investment ministries briefed exporters on the revamped export rebate programme on Sunday 15 November, as scheduled. No fetched page reports what was said there. EnterpriseAM, Zawya, Container News and gCaptain carried nothing on the briefing between 15 and 22 November. The Arabic and English outlets that covered it (Youm7, Maspero, El Balad, Banker, Veto, Amwal Al Ghad English) were all refused by the proxy. The programme rules as published remain those approved by the Cabinet on 5 November, re-read this week on a fetched page:
- Average rebate increase of 35%, varying by sector. Freezone exporters are excluded. The new rates apply to shipments from the start of November.
- A freight support line covers:
  - 50% of sea and land freight to Africa, Latin America, Australia, Southeast Asia and Russia
  - 25% of air freight to Europe and 50% to the UK, both for agricultural exports only
  - 25% of domestic transport costs, 25% of cargo insurance policies and 25% of the invoice for shipments on express vessels
- The target-market incentives stay. The US and 11 Southeast Asian countries are added to the list.
- Exporters must submit complete files before they are accepted. This rule change is "meant to stop incomplete files piling up and holding up payouts".
- Phase 1 runs to end-2026. Phase 2 starts July 2027.

**Key figures**
- Average increase: +35%. Freight support: 50% sea/land to new markets; 25%/50% air (agri, Europe/UK); 25% inland transport, 25% insurance, 25% express-vessel invoice.
- FY 2026/27 export-support budget: EGP 48 bn, against EGP 28 bn actually disbursed in FY 2025/26.
- Arrears: the Finance Ministry "is still working through arrears on shipments made before July 2024".

**Date:** Cabinet approval 5 Nov 2026. Briefing 15 Nov 2026 (confirmed as scheduled at 4pm, St. Regis, New Administrative Capital).

**Sources**
- EnterpriseAM Egypt, "The government is raising export rebates by an average of 35% and picking up as much as half the freight bill to new markets", 8 Nov 2026. https://enterpriseam.com/egypt/2026/11/08/the-government-is-raising-export-rebates-by-an-average-of-35-and-picking-up-as-much-as-half-the-freight-bill-to-new-markets/ (raw: `e_rebate.json`, `e_rebate.txt`)
- EnterpriseAM Egypt, "Happening today" section, 15 Nov 2026. https://enterpriseam.com/egypt/2026/11/15/egypts-final-imf-review-moves-to-virtual-talks-with-usd-2-3-bn-at-stake-and-a-15-december-deadline/ (raw: `eam_eg_15.json`, `eam_eg15.txt`)

**Verbatim quotes**
- "Exporters will also have to submit complete files before they're accepted, a rule change meant to stop incomplete files piling up and holding up payouts."
- "The FY 2026/27 budget earmarks EGP 48 bn for export support, up from the EGP 28 bn actually disbursed last fiscal year. Meanwhile, the Finance Ministry is still working through arrears on shipments made before July 2024."
- "Exporters will hear how the revamped export rebate program works in practice this afternoon, when the Finance and Investment ministries brief them at a 4pm press conference at the St. Regis in the New Administrative Capital"

**Why it matters for Egypt shippers (analysis).** Freight is now a refundable cost on shipments to Africa, Latin America, Southeast Asia, Australia and Russia. Each claim needs a complete file, so the forwarder's documents become part of the claim: the B/L, the freight invoice, the insurance certificate and the inland trucking invoice. These should be issued in the exporter's name, dated and itemised. November shipments already qualify. Payment timing under the new rules is not stated on any fetched page.

**Status: PARTIAL.** The programme terms are VERIFIED. The briefing outcome is UNVERIFIED: no fetched page reports it. Search snippets from blocked Arabic outlets report the following, and none of it can be used until a page is read:
- the EGP 48 bn figure "announced" at the briefing
- the Upper Egypt and border-area support rising from 25% to 40%
- the quality-certificate incentive rising from 30% to 60%
- the target-market incentive held at 25%
- a "digital tools" push by Minister Kouchouk

---

## 2. IMF staff-level agreement on the final review: about USD 2.3 bn pending Board approval

**Summary.** On 18 November the IMF and Egypt reached a staff-level agreement on two reviews: the eighth and final review of the 48-month Extended Fund Facility (EFF), and the third review of the Resilience and Sustainability Facility (RSF). This follows talks in Cairo from 25 October to 5 November and virtual meetings from 7 to 15 November. If the Executive Board approves before the programme expires on 15 December, Egypt receives about USD 1.5 bn (SDR 1.113 bn) under the EFF and up to about USD 0.8 bn (SDR 600 mn) under the RSF. Total disbursements under both arrangements would reach about USD 9.6 bn. Mission chief Amine Mati welcomed the CBE's October 100 bp hike and repeated that exchange-rate flexibility should be "the first line of defense". Egypt beat its primary-surplus and tax-revenue targets at end-September. Divestment is close to the target: about USD 1.2 bn booked, against the roughly USD 1.5 bn the Fund wants before the programme ends (EnterpriseAM's math).

**Key figures**
- EFF: SDR 1.113 bn (about USD 1.5 bn). RSF: up to SDR 600 mn (about USD 0.8 bn). Cumulative: SDR 7.112 bn (about USD 9.6 bn).
- Real GDP growth FY 2025/26: 5.1% (IMF).
- Board deadline: before 15 Dec 2026.

**Date:** IMF statement 18 Nov 2026. Reported 19 Nov.

**Sources**
- EnterpriseAM Egypt, "IMF staff and the government reached agreement on the final review, putting up to USD 2.3 bn on the table before the program expires", 19 Nov 2026. https://enterpriseam.com/egypt/2026/11/19/imf-staff-and-the-government-reached-agreement-on-the-final-review-putting-up-to-usd-2-3-bn-on-the-table-before-the-program-expires/ (raw: `eam_eg_full_1.json`, `eam_eg.txt`)
- Zawya / Arab Finance, "IMF, Egypt reach staff-level agreement on 8th and final EFF review", 19 Nov 2026. https://www.zawya.com/en/economy/imf-egypt-reach-staff-level-agreement-on-8th-and-final-eff-review-2392984 (raw: `zw_10.html`)

**Verbatim quotes**
- "exchange-rate flexibility should remain the first line of defense against external shocks, with interventions limited to containing excessive volatility." (Amine Mati, IMF)
- "The agreement follows discussions between Egyptian officials and an IMF mission led by Amine Mati in Cairo from October 25 to November 5, followed by virtual meetings from November 7 to 15"

**Why it matters for Egypt shippers (analysis).** This removes last week's main FX risk: a review slipping past 15 December. A completed review supports FX availability for importers into early 2027. The IMF's stress on a flexible exchange rate means importers should still expect the EGP to move with regional news rather than be held flat. FX clauses in freight quotes stay important.

**Status: VERIFIED.**

---

## 3. CBE and the EGP: no MPC this week; Goldman sees a hold to late 1Q 2027; USD back above EGP 54 on 22 Nov

**Summary.**
- **No CBE meeting or CPI release in the window.** The next MPC meeting is 17 December. The overnight deposit rate stays at 20.0% after the 29 October hike. October CPI (urban headline 12.7%) was released on 10 November and covered last week.
- **Goldman Sachs (22 Nov).** It expects the CBE to hold at 20% until late 1Q 2027, then cut 500 bp over 2027 (to 15%) and 200 bp in 2028 (to 13%). It expects inflation to rebound to about 14% by year-end before easing. Its USD/EGP forecasts are 53 at 3 months, 52 at 6 months and 50 at 12 months. Foreign holdings of local debt are estimated at about USD 20 bn, down from about USD 30 bn at end-September.
- **Exchange rate in the window.** Zawya (Arabic) reported on Sunday 22 November that the dollar rose back above EGP 54, as Qatar continued mediation efforts and new attacks hit tankers in and around Hormuz. No official CBE quote dated 16–22 November could be read (cbe.org.eg returned "Request Rejected"). The last CBE quote read on a fetched page is still EGP 53.39 on 12 November.
- **Reserves.** Net international reserves were USD 57.5 bn at end-October, up USD 151.6 mn from USD 57.35 bn in September (CBE provisional data). EnterpriseAM restated "USD 57.5 bn right now" on 22 November.

**Key figures**
- Policy rate: 20.0% overnight deposit (unchanged). Next MPC: 17 Dec 2026.
- Goldman: hold to late 1Q 2027; 15% by end-2027; 13% in 2028. USD/EGP 53 / 52 / 50 at 3 / 6 / 12 months.
- USD/EGP: above 54 on Sun 22 Nov (Zawya, bank trading). The last verified CBE quote is 53.39 (12 Nov).
- NIR: USD 57.5 bn, end-Oct 2026 (+USD 151.6 mn m-o-m).

**Date:** 22 Nov 2026 (Goldman, EGP move). Reserves data released early November, restated 22 Nov.

**Sources**
- EnterpriseAM Egypt, "Goldman Sachs expects CBE to hold at 20% until late 1Q, then cut by 700 bps through 2028", 22 Nov 2026. https://enterpriseam.com/egypt/2026/11/22/goldman-sachs-expects-cbe-to-hold-at-20-until-late-1q-then-cut-by-700-bps-through-2028/ (raw: `eam_eg.txt`)
- Zawya (Arabic), "مصر: الدولار يعود للارتفاع فوق 54 جنيه مع بداية الأسبوع", 22 Nov 2026. https://www.zawya.com/ar/الأسواق/عملات/مصر-الدولار-يعود-للارتفاع-فوق-54-جنيه-مع-بداية-الأسبوع-2442943 (raw: `zar_1.html`; lead paragraph only, the rest is behind a registration wall)
- EnterpriseAM Egypt, "Data point" section, 8 Nov 2026 (reserves), link in item 1 (raw: `e_rebate.txt`). EnterpriseAM, "Egypt may not need a new IMF facility…", 22 Nov 2026. https://enterpriseam.com/egypt/2026/11/22/egypt-may-not-need-a-new-imf-facility-but-we-still-have-plenty-of-work-to-do-on-the-fiscal-side-of-the-house/ (raw: `eam_eg.txt`)

**Verbatim quotes**
- "Goldman Sachs expects the Central Bank of Egypt (CBE) to hold its overnight deposit rate at 20% until late 1Q 2027 before it resumes cutting"
- "ارتفع سعر الدولار مقابل الجنيه المصري في تعاملات الأحد، ليعود فوق مستوى 54 جنيه" (Zawya: the dollar rose against the Egyptian pound in Sunday trading, back above EGP 54)
- "USD 57.5 bn — that's where the country's net international reserves stood at the end of October 2026, inching up by USD 151.6 mn from USD 57.35 bn in September, according to provisional data from the Central Bank of Egypt."

**Why it matters for Egypt shippers (analysis).** The EGP gave back part of its early-November gains as Gulf tensions rose. Importers paying USD freight should expect a 53–55 band to be the working range for now. With no rate cut expected before late 1Q 2027, EGP financing for imports stays expensive.

**Status: PARTIAL.** The Goldman forecast, the reserves figure and the "above 54" move are VERIFIED. No official CBE rate dated in the window was read.

---

## 4. Trade: September deficit up 60.6% to USD 5.3 bn as imports jump 29.7%

**Summary.** According to CAPMAS data reported by Arab Finance:
- Egypt's trade deficit rose 60.6% y-o-y to USD 5.3 bn in September 2026.
- Imports rose 29.7% to USD 10.6 bn and exports rose 7.4% to USD 5.3 bn. Total trade was USD 15.9 bn (+21.3%).
- In August the deficit was USD 6.4 bn: imports USD 11.1 bn (+27.4%), exports USD 4.7 bn.

**Key figures**
- Sept 2026: deficit USD 5.3 bn (+60.6%); imports USD 10.6 bn (+29.7%); exports USD 5.3 bn (+7.4%).
- Aug 2026: deficit USD 6.4 bn; imports USD 11.1 bn; exports USD 4.7 bn.

**Date:** 19 Nov 2026.

**Source**
- Zawya / Arab Finance, "Egypt's trade deficit widens 60.6% in September 2026", 19 Nov 2026. https://www.zawya.com/en/economy/egypts-trade-deficit-widens-60.6-in-september-2026-2392989 (raw: `zw_1.html`)

**Verbatim quote**
- "Egypt's trade deficit surged by 60.6% year-on-year (YoY) to $5.3 billion in September 2026, driven by a sharp increase in imports, according to data from the Central Agency for Public Mobilization and Statistics (CAPMAS)."

**Why it matters for Egypt shippers (analysis).** Inbound volumes are running about 30% above last year, which supports import freight demand and port and storage use. Imports growing four times faster than exports is the gap the rebate programme (item 1) is meant to close, and it keeps the risk of import-control measures on the table.

**Status: VERIFIED.** Note: the article gives exports and the deficit both as USD 5.3 bn, which is consistent with imports of USD 10.6 bn.

---

## 5. Egypt–Africa trade up 15.3% to USD 8.2 bn in 9M 2026; Libya and Sudan lead

**Summary.** CAPMAS reported Egypt's trade with African Union countries at USD 8.2 bn in January–September 2026, up 15.3%. Exports to AU countries rose 8.5% to USD 6.1 bn and imports rose 41.6% to USD 2.1 bn. Five markets took 64.2% of exports:
- Libya USD 1.2 bn (19.3%)
- Sudan USD 900 mn (15.2%)
- Morocco USD 700 mn (11.3%)
- Algeria USD 700 mn (11.3%)
- Tunisia USD 400 mn (7.2%)

The top export lines were electrical and mechanical machinery (USD 517.8 mn), plastics (USD 478.2 mn) and iron and steel (USD 344.7 mn). Trade with COMESA rose 23.5% to USD 4.9 bn, and with CEN-SAD 17.5% to USD 5.7 bn. Separately, on 19 November Egypt and Libya (GNU PM Dbeibeh in Cairo) signed agreements and MoUs on gas infrastructure, petroleum refining, fisheries, SMEs and labour. Dbeibeh also raised visas, residence permits and "entry through the border crossing".

**Key figures**
- Egypt–AU trade 9M 2026: USD 8.2 bn (+15.3%). Exports USD 6.1 bn (+8.5%). Imports USD 2.1 bn (+41.6%).
- Top destinations: Libya 1.2 bn, Sudan 0.9 bn, Morocco 0.7 bn, Algeria 0.7 bn, Tunisia 0.4 bn.

**Date:** CAPMAS statement Wed 18 Nov (reported 19 Nov). Egypt–Libya signing 19 Nov 2026.

**Sources**
- Zawya / Daily News Egypt, "Egypt's trade with African Union countries rises by $1.1bln to $8.2bln in 9M 2026", 19 Nov 2026. https://www.zawya.com/en/economy/egypts-trade-with-african-union-countries-rises-by-1.1bln-to-8.2bln-in-9m-2026-2377014 (raw: `zw_2.html`)
- Zawya / Arab Finance, "Egypt, Libya sign agreements on gas infrastructure, fisheries and labor", 20 Nov 2026. https://www.zawya.com/en/projects/commodities/egypt-libya-sign-agreements-on-gas-infrastructure-fisheries-and-labor-2416449 (raw: `zw_7.html`)

**Verbatim quotes**
- "Libya topped the list with $1.2bn, representing 19.3% of total exports, followed by Sudan with $900m (15.2%), Morocco with $700m (11.3%), Algeria with $700m (11.3%) and Tunisia with $400m (7.2%)."
- "Dbeibeh raised several issues affecting Libyan citizens, including visas and residence permits, the status of Libyan students in Egypt, and entry through the border crossing."

**Why it matters for Egypt shippers (analysis).** Libya and Sudan alone take more than a third of Egypt's African exports, mostly by road through Salloum and the southern crossings, and Africa is a 50%-freight-support market under item 1. Exporters on these lanes have a new reason to formalise freight paperwork. The Libya agreements contain no named trade-facilitation or border-procedure measure.

**Status: VERIFIED.**

---

## 6. Suez: Gemini returns three more Asia–Europe loops; DHL warns of 6–12 months of transition

**Summary.**
- **Gemini AE1, AE2, AE3.** On 16–17 November Maersk and Hapag-Lloyd said three more Gemini services will move from the Cape to Suez. Maersk names them AE1/AE2/AE3; Hapag-Lloyd and Container News call them NE1/NE2/NE3, with the same vessels. First westbound sailings:
  - AE2/NE1: Mary Maersk from Ningbo, 4 Dec
  - AE3/NE3: Alette Maersk from Shanghai, 20 Dec
  - AE1/NE2: Damietta Express from Shanghai, 14 Jan 2027
  
  By EnterpriseAM's count this takes Gemini's Suez services to nine. Arab Finance recalls that Maersk said in October it expects all its services back on Suez by March 2027.
- **DHL (16 Nov).** About 60% of relevant Asia–Europe headhaul services are now planned through Suez, and the transition could take another 6–12 months. More than 10% of the global fleet (about 3.6 mn TEU) is tied up in port congestion.
- **Xeneta, October (via Container News, 19 Nov).** Global on-time arrivals were 24%, the lowest since July 2022. Far East–Europe on-time arrivals were 7%, with an average delay of 9.0 days.
- **Canal activity.** The Planning Minister told the Cabinet that Suez Canal activity grew 47.5% y-o-y in Q1 FY 2026/27 (July–September). GDP grew 4.9% in the quarter.
- **SCA.** The SCA is exploring local assembly, then manufacture, of Anglo Belgian Corporation engines. ABC already supplies engines for SCA tugs being built at the South Red Sea Shipyard.

**Key figures**
- Gemini Suez switch dates: 4 Dec 2026, 20 Dec 2026, 14 Jan 2027. Gemini services via Suez: nine (EnterpriseAM count).
- DHL: about 60% of Asia–Europe headhaul planned via Suez; 6–12 months to settle; 3.6 mn TEU in congestion.
- Xeneta Oct: 24% global schedule reliability; 7% Far East–Europe; 9.0 days average delay.
- Suez Canal activity: +47.5% in Q1 FY 2026/27. GDP +4.9%.

**Date:** 16–19 Nov 2026.

**Sources**
- gCaptain, "Maersk, Hapag-Lloyd Expand Suez Canal Return With Three More Gemini Services", 16 Nov 2026. https://gcaptain.com/maersk-hapag-lloyd-expand-suez-canal-return-with-three-more-gemini-services/ (raw: `wp_gcaptain.com.json`)
- Container News, "Maersk and Hapag-Lloyd return three more Gemini services to Suez", 17 Nov 2026. https://container-news.com/maersk-and-hapag-lloyd-return-three-more-gemini-services-to-suez/ (raw: `cn.json`)
- Zawya / Arab Finance, "Maersk, Hapag-Lloyd to reroute 3 Gemini services to Suez Canal", 17 Nov 2026. https://www.zawya.com/en/business/maersk-hapag-lloyd-to-reroute-3-gemini-services-to-suez-canal-2306254 (raw: `zw_5.html`)
- EnterpriseAM Egypt, "Back through Suez" section, 17 Nov 2026. https://enterpriseam.com/egypt/2026/11/17/majid-al-futtaim-taps-dp-world-to-move-egyptian-fresh-produce-onto-uae-shelves/ (raw: `eam_eg.txt`)
- gCaptain, "Suez Canal Return Won't Resolve Global Shipping Congestion, DHL Warns", 16 Nov 2026. https://gcaptain.com/suez-canal-return-wont-resolve-global-shipping-congestion-dhl-warns/ (raw: `wp_gcaptain.com.json`)
- Container News, "Red Sea returns are rewriting carrier reliability, not just transit times", 19 Nov 2026. https://container-news.com/red-sea-returns-are-rewriting-carrier-reliability-not-just-transit-times/ (raw: `cn.json`)
- Zawya / Arab Finance, "Egypt's economy grows 4.9% in Q1 FY 2026/27", 19 Nov 2026. https://www.zawya.com/en/economy/egypts-economy-grows-4.9-in-q1-fy-202627-2356705 (raw: `zw_3.html`)
- Zawya / Arab Finance, "SCA, Belgium's ABC explore localizing engine manufacturing in Egypt", 17 Nov 2026. https://www.zawya.com/en/economy/sca-belgiums-abc-explore-localizing-engine-manufacturing-in-egypt-2306251 (raw: `zw_6.html`)

**Verbatim quotes**
- "According to Maersk's November 16 advisory, the transitions will begin with the AE2 service on December 4, followed by AE3 on December 20 and AE1 on January 14, 2027." (gCaptain)
- "Around 60% of relevant Asia-Europe headhaul services are currently planned to operate through Suez, although the return remains uneven across trade lanes, DHL said."
- "Suez Canal activity recorded a sharper upturn, expanding 47.5% compared with Q1 FY 2025/2026." (Arab Finance)

**Why it matters for Egypt shippers (analysis).** More Asia–Europe mainline capacity will pass Port Said and Sokhna from December. But on-time arrivals on Far East–Europe are only 7%, so shorter Suez routings do not yet mean dependable dates. Egyptian importers should keep buffer time in December–January delivery plans and confirm each sailing's routing (Suez or Cape).

**Status: VERIFIED.** No new SCA revenue or transit figures and no new SCA rebate circular were published in the window on any fetched page.

---

## 7. December rates: Hapag-Lloyd and CMA CGM set Asia–Egypt/East Med FAK at USD 6,600–6,800/40'

**Summary.**
- **Hapag-Lloyd** published Far East–Europe FAK rates from 1 December, valid until further notice. The "Türkiye, Egypt, East Mediterranean" zone is USD 5,300 per 20' and USD 6,600 per 40'/40'HC. North Europe is USD 3,000 / USD 4,500. The rates include Marine Fuel Recovery; THC, security and local charges are extra.
- **CMA CGM** set Asia–Med FAK rates for 1–14 December:
  - East Med USD 5,500 / USD 6,800
  - North Africa USD 6,400 / USD 8,800
  
  These include basic freight, bunker, EU ETS and LSS.
- **For comparison (last week's baseline):** MSC's December East Med 40' was USD 6,500.

**Key figures**
- Hapag-Lloyd from 1 Dec: Egypt/East Med USD 5,300 (20') / 6,600 (40').
- CMA CGM 1–14 Dec: East Med USD 5,500 / 6,800. North Africa USD 6,400 / 8,800.

**Date:** 15 and 18 Nov 2026.

**Sources**
- Container News, "Hapag-Lloyd raises Far East–Europe freight rates from December", 15 Nov 2026. https://container-news.com/hapag-lloyd-raises-far-east-europe-freight-rates-from-december/ (raw: `cn2.json`)
- Container News, "CMA CGM announces new Asia–Mediterranean rates and Mozambique surcharge", 18 Nov 2026. https://container-news.com/cma-cgm-announces-new-asia-mediterranean-rates-and-mozambique-surcharge/ (raw: `cn.json`)

**Verbatim quotes**
- "Higher tariffs will apply to Türkiye, Egypt and the Eastern Mediterranean, at US$5,300 per 20-foot container and US$6,600 per 40-foot container."
- "East Mediterranean shipments will be charged US$5,500 for 20-foot containers and US$6,800 for 40-foot equipment."

**Why it matters for Egypt shippers (analysis).** All three big carriers now ask USD 6,500–6,800 per 40' from Asia to Egypt for early December, about USD 2,000 above North Europe. Hapag-Lloyd names Egypt explicitly. FAK is a ceiling for spot cargo. With Suez capacity returning (item 6) and DHL seeing weakness on some Asia–Europe lanes, contract and NAC shippers should negotiate below these levels.

**Status: VERIFIED.** Hapag-Lloyd names Egypt explicitly. Whether CMA CGM's "East Med" includes Egyptian ports is inferred, not stated.

---

## 8. Egyptian ports and feeders: Yang Ming's EG1–EG3, Sidra Line's Alexandria–North Africa loop, EBRD loan for Mesco's port yards

**Summary.**
- **Yang Ming (15 Nov).** Yang Ming is taking slots on two intra-Egypt DP World Shipping Solutions services and on the Egyptian leg of DP World's Egypt–Syria–Lebanon service, marketed as:
  - EG1 (weekly): Port Said – Damietta – Alexandria Old Port – Port Said
  - EG2 (fortnightly): Damietta – El Dekheila – Port Said
  - EG3 (weekly): Port Said – El Dekheila – Damietta – Port Said
- **Sidra Line (22 Nov).** Sidra Line revised its WAF service to Alexandria – Misurata – Rades – Casablanca – Conakry – Alexandria, with one 750 TEU ship.
- **EBRD and Mesco (19 Nov).** The EBRD lent family logistics firm Mesco up to EGP 585 mn (about EUR 10.6 mn) for flatbed trucks, yard works at Alexandria, Port Said, Damietta and Sokhna, electric equipment, and a study of electric-truck routes.

**Key figures**
- Yang Ming: 3 intra-Egypt connections (2 weekly, 1 fortnightly) covering Port Said, Damietta, Alexandria Old Port and El Dekheila.
- Sidra WAF: 750 TEU, Alexandria to Misurata (Libya), Rades (Tunisia), Casablanca and Conakry.
- Mesco: up to EGP 585 mn (EBRD).

**Date:** 15, 19 and 22 Nov 2026. The Yang Ming item is dated Sunday 15 Nov, a day before the window, and was not in Issue 001.

**Sources**
- Container News, "Yang Ming expands Egypt coverage through DP World slot-sharing deal", 15 Nov 2026. https://container-news.com/yang-ming-expands-egypt-coverage-through-dp-world-slot-sharing-deal/ (raw: `cn2.json`)
- Container News, "Sidra Line revises Mediterranean–West Africa service", 22 Nov 2026. https://container-news.com/sidra-line-revises-mediterranean-west-africa-service/ (raw: `cn.json`)
- EnterpriseAM Egypt, "EBRD lends Mesco EGP 585 mn and takes half the risk on EGP 500 mn Tube loan", 19 Nov 2026. https://enterpriseam.com/egypt/2026/11/19/ebrd-lends-mesco-egp-585-mn-and-takes-half-the-risk-on-egp-500-mn-tube-loan/ (raw: `eam_eg.txt`)

**Verbatim quotes**
- "Yang Ming will market the three connections under the EG1, EG2 and EG3 service brands, providing links between Port Said, Damietta and Alexandria."
- "The revised WAF service will introduce calls at Misurata in Libya, Rades in Tunisia and Casablanca in Morocco."
- "a direct loan of up to EGP 585 mn (c. EUR 10.6 mn) to Mesco , a family logistics firm, for flatbed trucks, yard works at Alexandria, Port Said, Damietta, and Sokhna"

**Why it matters for Egypt shippers (analysis).** More intra-Egypt feeder options make it easier to book a mainline call at Port Said or Damietta with on-carriage to Alexandria (or the reverse) on one carrier. A direct Alexandria–Misurata–Casablanca loop serves North Africa exporters, who now qualify for the 50% freight support on Africa-bound sea freight.

**Status: VERIFIED.**

---

## 9. Majid Al Futtaim and DP World plan a Sokhna–Jebel Ali reefer corridor for Egyptian produce

**Summary.** Majid Al Futtaim and DP World signed an MoU to move more Egyptian fresh fruit and vegetables onto MAF's UAE shelves. DP World would run the cold chain end to end: consolidation in temperature-controlled facilities at Sokhna, DP World feeder services to the UAE, then refrigerated moves to Jebel Ali. The partnership also aims to increase container volumes shipped from Egypt to the UAE, and covers sourcing, consolidation, customs clearance and distribution. No investment value, volume target or timeline was given. DP World already runs the USD 85 mn Sokhna Logistics Park (opened October 2025).

**Key figures**
- MAF cumulative investment in Egypt: USD 2.7 bn. 99.8% of its retail products sourced locally.
- DP World Sokhna Logistics Park: USD 85 mn. Cold store in 6th of October City: USD 29 mn (with Elsewedy).

**Date:** 17 Nov 2026.

**Sources**
- EnterpriseAM Egypt, "Majid Al Futtaim taps DP World to move Egyptian fresh produce onto UAE shelves", 17 Nov 2026. https://enterpriseam.com/egypt/2026/11/17/majid-al-futtaim-taps-dp-world-to-move-egyptian-fresh-produce-onto-uae-shelves/ (raw: `eam_eg.txt`)
- Zawya / Arab Finance, "Majid Al Futtaim, DP World to expand Egyptian exports to regional markets", 17 Nov 2026. https://www.zawya.com/en/business/north-africa/majid-al-futtaim-dp-world-to-expand-egyptian-exports-to-regional-markets-2298089 (raw: `zw_11.html`)

**Verbatim quotes**
- "DP World will run the whole cold chain: produce from the retailer's Egyptian suppliers gets consolidated at its temperature-controlled facilities at Sokhna, shipped to the UAE on its feeder services, and moved under refrigeration to Jebel Ali for distribution across Majid Al Futtaim's stores."
- "they haven't put numbers on any of it yet: no investment value, volume target, or timeline."

**Why it matters for Egypt shippers (analysis).** This is a Red Sea routing (Sokhna to Jebel Ali) for Egyptian perishables, but it runs through Hormuz, where war-risk costs are high (item 11). Agri exporters supplying MAF should expect consolidated reefer bookings from Sokhna rather than direct Alexandria sailings. It is an MoU only, so timing is open.

**Status: VERIFIED.**

---

## 10. Red Sea: Houthis tell ships to leave Saudi Red Sea ports; MSC adds an India–Jeddah loop

**Summary.**
- **Houthi warning (20 Nov, Reuters via gCaptain).** The Saudi-led coalition said it struck Yemen's Hodeidah port on Friday 20 November. Houthi military spokesman Yahya Saree then urged shipping companies to evacuate their ships from Saudi Arabia's Red Sea ports immediately, warned airlines away from Saudi airspace, and threatened a power station at Shuqaiq. Context from the same report:
  - The Houthis struck Riyadh's tallest skyscraper the day before.
  - Fighting in Yemen resumed in July. The Houthis have seized Yemen's Red Sea coast.
- **MSC North India–Red Sea service.** MSC is launching a service in late November with 2,500–3,000 TEU ships: Mundra – Port Qasim – Jeddah – King Abdullah Port – Mundra. Frequency and first sailing date are not given.
- **Saudi trade (EnterpriseAM Infrastructure, 19 Nov).** Attacks around Bab al-Mandab cut crude shipments from Yanbu to roughly half their July level in August, and Saudi crude is moving out through Hormuz again.

**Key figures**
- Houthi threat: all Saudi Red Sea ports, 20 Nov 2026.
- MSC service: 2,500–3,000 TEU; Mundra, Port Qasim, Jeddah, King Abdullah Port; starts late Nov 2026.
- Saudi merchandise trade surplus Aug: SAR 15.6 bn (−21% y-o-y). Re-exports −34%.

**Date:** 15, 19 and 20 Nov 2026.

**Sources**
- gCaptain (Reuters), "Houthis Order Ships to Leave Saudi Red Sea Ports After Hodeidah Airstrikes", 20 Nov 2026. https://gcaptain.com/houthis-order-ships-to-leave-saudi-red-sea-ports-after-hodeidah-airstrikes/ (raw: `wp_gcaptain.com.json`)
- Container News, "MSC to launch new North India–Red Sea container service", 15 Nov 2026. https://container-news.com/msc-to-launch-new-north-india-red-sea-container-service/ (raw: `cn2.json`)
- EnterpriseAM Infrastructure, "Saudi crude is flowing out through Hormuz again after Red Sea attacks cut summer export earnings", 19 Nov 2026. https://enterpriseam.com/infrastructure/2026/11/19/saudi-crude-is-flowing-out-through-hormuz-again-after-red-sea-attacks-cut-summer-export-earnings/ (raw: `eam_infra.json`)

**Verbatim quotes**
- "We warn all employees, workers, and those in the vicinity of (Saudi Arabia's Red Sea) ports to evacuate them immediately and stay away. We also urge all shipping companies to immediately evacuate their ships from these ports," (Houthi spokesman Yahya Saree)
- "Attacks around the Bab al-Mandab Strait cut shipments from Yanbu to roughly half their July level in August"

**Why it matters for Egypt shippers (analysis).** This is the most important risk item of the week. Jeddah and King Abdullah Port are transhipment and call points on several services that also serve Sokhna, including Evergreen's OGRD and Gemini's Jeddah calls. A threat against Saudi Red Sea ports could bring war-risk surcharges, skipped calls or delays on Egypt–Saudi Red Sea cargo and on Asia–Sokhna strings. Saudi-bound shippers should consider routing via Saudi Gulf ports or overland from Sokhna/Safaga ferries, and should watch carrier advisories this week. The reports also raise the question of whether the Gemini/Premier Suez returns hold.

**Status: VERIFIED** for the Houthi statement and the MSC plan. **Not verified:** any carrier suspension of Jeddah calls, or any attack on a ship in a Saudi port, after 20 Nov. None was found on fetched pages.

---

## 11. Gulf: Adnoc L&S ship hit in Hormuz; MSC adds a Fujairah shuttle; Hormuz crossing priced at USD 1k a box

**Summary.**
- **Adnoc attack.** An Adnoc Logistics & Services vessel was attacked transiting Hormuz on the evening of Tuesday 17 November: one crew member missing and 11 injured. This came a week after another Adnoc L&S vessel was damaged in UAE waters.
- **Hormuz surcharge.** Ex-WEF supply-chain head Wolfgang Lehmacher, quoted by EnterpriseAM, said "Maersk charges USD 1k a container to cross Hormuz". This is a third-party quote, not a carrier tariff that was read.
- **MSC Fujairah Shuttle 2.** MSC launches Fujairah Shuttle 2 in December: Colombo – Khor Fakkan – Fujairah – Sohar, with 1,700–9,400 TEU ships.
- **Alonso and Cargo Line.** Spain's Alonso Group took a stake in Dubai forwarder Cargo Line.
- **Oman–Uzbekistan.** The two countries signed about USD 5 bn of MoUs covering logistics, free zones and customs cooperation.

**Key figures**
- Adnoc L&S attack: 17 Nov; 1 missing, 11 injured.
- Hormuz crossing: USD 1k per container (Maersk, per Lehmacher quote).
- MSC Fujairah Shuttle 2: December 2026; Colombo, Khor Fakkan, Fujairah, Sohar.
- Fujairah bunker sales: October about 60% below a year earlier (Unicore estimate).

**Date:** 18–21 Nov 2026.

**Sources**
- EnterpriseAM Infrastructure, "Who's still sailing?", 19 Nov 2026. https://enterpriseam.com/infrastructure/2026/11/19/whos-still-sailing/ (raw: `eam_infra.txt`)
- EnterpriseAM Infrastructure, "Spain's Alonso acquires a stake in UAE's Cargo Line", 18 Nov 2026. https://enterpriseam.com/infrastructure/2026/11/18/spains-alonso-acquires-a-stake-in-uaes-cargo-line/ (raw: `eam_infra.txt`)
- Container News, "MSC expands regional network with two new services", 21 Nov 2026. https://container-news.com/msc-expands-regional-network-with-two-new-services/ (raw: `cn.json`)
- EnterpriseAM Infrastructure, "Fujairah has found new fuel for its bunker trade…", 19 Nov 2026. https://enterpriseam.com/infrastructure/2026/11/19/fujairah-has-found-new-fuel-for-its-bunker-trade-but-winning-back-the-ships-that-refuelled-there-could-take-years/ (raw: `eam_infra.txt`)
- EnterpriseAM Infrastructure, "Oman and Uzbekistan sign USD 5 bn MoUs focused on logistics and mining", 19 Nov 2026. https://enterpriseam.com/infrastructure/2026/11/19/oman-and-uzbekistan-sign-usd-5-bn-mous-focused-on-logistics-and-mining/ (raw: `eam_infra.txt`)

**Verbatim quotes**
- "An Adnoc Logistics & Services vessel was attacked while transiting Hormuz on Tuesday evening, leaving one crew member missing and 11 injured."
- "But Gulf costs are now set by war surcharges and queues. Maersk charges USD 1k a container to cross Hormuz. Margins will come from charging for reliability," (Wolfgang Lehmacher)

**Why it matters for Egypt shippers (analysis).** Cargo from Egypt to Jebel Ali and the inner Gulf still carries a Hormuz premium and attack risk. MSC's new shuttle confirms that carriers are building around Hormuz, via Khor Fakkan, Fujairah and Sohar, with trucking onward. Quote Gulf cargo via the east-coast ports, with war-risk costs listed separately.

**Status: VERIFIED.** The USD 1k figure is VERIFIED as a quote, not as a carrier tariff.

---

## 12. Trade partners: India targets USD 12 bn with Egypt and an FTA study; China trade about USD 20 bn

**Summary.**
- **India (17 Nov).** At the first ministerial session of the India–Egypt Joint Trade Committee, the two sides targeted USD 12 bn of bilateral trade by 2030, up from USD 6.5 bn in FY 2025/26. They agreed to explore the terms of a free trade agreement and to speed up India's first dedicated industrial zone in SCZone. India floated UPI links and wider local-currency trade. EnterpriseAM had reported on 8 Nov a first pilot transfer settling trade in EGP and INR.
- **China (17 Nov).** Investment Minister Mohamed Farid said Egypt–China trade is about USD 20 bn, making China Egypt's second-largest trading partner. More than 3,000 Chinese companies operate in Egypt, with investments above USD 10 bn.
- **FDI target.** Farid also set a target of USD 78 bn in cumulative net FDI for FY 2026/27 to FY 2029/30.

**Key figures**
- Egypt–India trade: USD 6.5 bn (FY 2025/26), target USD 12 bn by 2030.
- Egypt–China trade: about USD 20 bn. Chinese investment: more than USD 10 bn.
- FDI target: USD 78 bn over FY 2026/27–2029/30.

**Date:** 17 Nov 2026.

**Sources**
- EnterpriseAM Egypt, "Egypt and India target USD 12 bn in trade by 2030, and agree to explore a free trade agreement", 17 Nov 2026. https://enterpriseam.com/egypt/2026/11/17/egypt-and-india-target-usd-12-bn-in-trade-by-2030-and-agree-to-explore-a-free-trade-agreement/ (raw: `eam_eg.txt`)
- Zawya / Daily News Egypt, "Egypt-China trade reaches $20bln, Chinese investment exceeds $10bln: Farid", 17 Nov 2026. https://www.zawya.com/en/economy/belt-road-initiative-bri/egypt-china-trade-reaches-20bln-chinese-investment-exceeds-10bln-farid-2301600 (raw: `zw_8.html`)
- Zawya / Arab Finance, "Egypt targets $78bln in FDI inflows by FY2029/30: Farid", 17 Nov 2026. https://www.zawya.com/en/economy/egypt-targets-78bln-in-fdi-inflows-by-fy202930-farid-2302036 (raw: `zw_9.html`)

**Verbatim quotes**
- "They agreed to explore the terms of a free trade agreement and to ramp up work on India's first dedicated industrial zone in the Suez Canal Economic Zone (SCZone)."
- "Bilateral trade between Egypt and China has reached approximately $20bn, making China Egypt's second-largest trading partner"

**Why it matters for Egypt shippers (analysis).** India is now reached via Suez on Gemini ME1 and on MSC's India–Red Sea strings. An FTA study and local-currency settlement could cut FX friction on India–Egypt cargo, which is mostly imports today. An FTA is at the "explore" stage only.

**Status: VERIFIED.**

---

## 13. Fertiliser makers pay 50% more for gas to keep exporting until early January

**Summary.** Seven fertiliser producers agreed to pay a combined USD 175 mn upfront (USD 25 mn each) under a 45-day deal that started on 16 November (Asharq Business, cited by EnterpriseAM). Their gas price rises 50% to USD 12.75/mmBtu from USD 8.5. In return they can export all current output until early January and are temporarily exempt from supplying subsidised fertiliser to the Agriculture Ministry. Gas cuts of 20–40% stay in place. By EnterpriseAM's math, gas for a ton of urea costs USD 672–728 at the roughly USD 28/mmBtu the state pays for LNG, against about USD 535/t FOB for November urea. Separately, Bloomberg/Kpler data (via gCaptain, 18 Nov) show at least two US LNG cargoes diverted away from Egypt. One, the Al Qassar, turned west after reaching Port Said.

**Key figures**
- Upfront gas payment: USD 175 mn (7 firms × USD 25 mn). Gas price: USD 12.75/mmBtu (from 8.5). Term: 45 days. Exports allowed until early January.
- Urea: about USD 535/t FOB (November).
- Mopco: about USD 265 mn upgrade financing (USD 165 mn bank syndicate). Europe takes 89% of its exports.

**Date:** 16–18 Nov 2026.

**Sources**
- EnterpriseAM Egypt, "Fertilizer producers pay 50% more for gas and keep exporting, as LNG costs outrun urea prices", 16 Nov 2026. https://enterpriseam.com/egypt/2026/11/16/fertilizer-producers-pay-50-more-for-gas-and-keep-exporting-as-lng-costs-outrun-urea-prices/ (raw: `eam_eg.txt`)
- EnterpriseAM Egypt, 17 Nov 2026, "Mopco plans to expand" section. https://enterpriseam.com/egypt/2026/11/17/egypt-and-india-target-usd-12-bn-in-trade-by-2030-and-agree-to-explore-a-free-trade-agreement/ (raw: `eam_eg.txt`)
- gCaptain (Bloomberg), "More U.S. LNG Cargoes Divert to Europe in Relief for Tight Market", 18 Nov 2026. https://gcaptain.com/more-u-s-lng-cargoes-divert-to-europe-in-relief-for-tight-market/ (raw: `wp_gcaptain.com.json`)

**Verbatim quotes**
- "In return, they can export all of their current output until early January and are temporarily exempt from supplying subsidized fertilizer to the Agriculture Ministry, while gas cuts of 20-40% remain in place."
- "The Al Qassar tanker, carrying US LNG, turned west away from Egypt earlier this week after reaching the country's Port Said, according to ship-tracking data."

**Why it matters for Egypt shippers (analysis).** This updates last week's picture of 33% curtailments. Urea and ammonia exports are cleared to flow at full available output until early January, although production is still cut 20–40%. Bulk shippers and chartering desks can plan December liftings, but should expect smaller parcels and a policy review in January.

**Status: VERIFIED.** The deal terms are attributed to Asharq Business via EnterpriseAM.

---

## 14. CBAM: Damietta's ISSC becomes the first non-EU accredited verifier

**Summary.** Damietta-based Integrated Sustainable Solutions Company (ISSC) is the first verification body outside the EU to be accredited under the EU's Carbon Border Adjustment Mechanism, according to CBAM Guide (via EnterpriseAM). ISSC can verify the emissions data EU importers must report on Egyptian cement, hydrogen and ammonia, fertilisers, aluminium, and iron and steel. Previously exporters had to bring in an EU-based verifier for the required site visits. Egypt supplied 44.3% of the EU's non-EU urea imports in 2025 (Eurostat). CBAM's definitive phase starts in January. The first annual declarations, covering 2026 imports, are due by 30 September 2027.

**Key figures**
- Egypt's share of EU urea imports from outside the bloc, 2025: 44.3%.
- First CBAM declarations due: 30 Sept 2027.

**Date:** 18 Nov 2026.

**Source**
- EnterpriseAM Egypt, "Carbon checks, done at home" section, 18 Nov 2026. https://enterpriseam.com/egypt/2026/11/18/etisalat-business-plans-gpu-rentals-in-egypt-as-chipverse-raises-funds-to-double-capacity/ (raw: `eam_eg.txt`)

**Verbatim quote**
- "Damietta-based Integrated Sustainable Solutions Company (ISSC) has become the first verification body established outside the EU to be accredited under the bloc's Carbon Border Adjustment Mechanism (CBAM)"

**Why it matters for Egypt shippers (analysis).** Steel, aluminium, cement and fertiliser exporters to the EU can now get emissions data verified locally, which should be faster and cheaper than flying in EU verifiers. That eases the paperwork flagged in Issue 001 (GOEIC emissions reports, EU importer CBAM filings).

**Status: VERIFIED** as reported by EnterpriseAM. The original CBAM Guide page was not fetched.

---

## Also noted (verified, shorter)

- **Private-sector minimum wage up 21% to EGP 8.5k a month from 1 Jan 2027**, approved by the National Wages Council on 15 Nov. It covers 26.5 mn private-sector workers. Expect upward pressure on local trucking, warehousing and handling tariffs from January. Source: EnterpriseAM, 16 Nov 2026, https://enterpriseam.com/egypt/2026/11/16/the-headlines-from-this-morning-22/ (raw: `eam_eg.txt`). Quote: "The private-sector minimum wage will rise 21% to EGP 8.5k a month from 1 January 2027".
- **SCZone: Amea Power wind-turbine factory.** Amea Power signed USD 850 mn of contracts with PowerChina and Mingyang. They cover the USD 650 mn Amunet 2 wind farm (Ras Shukeir) and a turbine factory in SCZone (headline: USD 200 mn) that should make 3 GW of turbines a year by end-2029, some for export to Africa. It is the second Chinese-backed turbine plant in SCZone after Sany. Source: EnterpriseAM, 19 Nov 2026, https://enterpriseam.com/egypt/2026/11/19/amea-power-inks-deals-for-usd-650-mn-ras-shukeir-wind-farm-and-usd-200-mn-turbine-factory-with-chinese-partners/ (raw: `eam_eg.txt`). Expect project cargo (blades, nacelles) through Red Sea ports from 2028.
- **GDP +4.9% in Q1 FY 2026/27.** Non-petroleum manufacturing grew 3.9% and petroleum refining 19.6%. Source: Zawya / Arab Finance, 19 Nov 2026 (raw: `zw_3.html`, link in item 6).
- **Unemployment 6.0% in Q3 2026** (from 5.8%). Transport and storage employ 2.992 mn people (8.9% of the employed). Source: Zawya / Arab Finance, "Egypt's unemployment rate rises to 6% in Q3 2026", 19 Nov 2026, https://www.zawya.com/en/economy/egypts-unemployment-rate-rises-to-6-in-q3-2026-2356706 (raw: `zw_4.html`).
- **Saudi logistics registrations.** Saudi road-freight registrations rose 52% y-o-y to 104,612 in Q3 2026. Storage at ports, customs facilities and free zones rose 46% to 9,111. Source: Zawya / Saudi Gazette, 17 Nov 2026, https://www.zawya.com/en/business/saudi-transport-and-storage-registrations-rise-31-to-185554-in-q3-2026-2310742 (raw: `zw_12.html`).

---

## Upcoming events (verified)

| Date | Event | Source (fetched) |
|---|---|---|
| Late Nov 2026 | MSC North India–Red Sea service starts (Mundra, Port Qasim, Jeddah, KAP) | Container News, 15 Nov (`cn2.json`) |
| 1 Dec 2026 | Hapag-Lloyd Far East–Europe FAK (Egypt/East Med USD 6,600/40') | Container News, 15 Nov (`cn2.json`) |
| 1–14 Dec 2026 | CMA CGM Asia–Med FAK (East Med USD 6,800/40'; North Africa USD 8,800/40') | Container News, 18 Nov (`cn.json`) |
| 4 Dec 2026 | First Gemini AE2/NE1 Suez sailing (Mary Maersk, Ningbo) | gCaptain, 16 Nov; Container News, 17 Nov |
| Dec 2026 | Misr Life Insurance 15% EGX float; MSC Fujairah Shuttle 2 starts | EnterpriseAM, 18 Nov; Container News, 21 Nov |
| Before 15 Dec 2026 | IMF Executive Board vote on final EFF and RSF reviews (about USD 2.3 bn); EFF expires 15 Dec | EnterpriseAM, 19 Nov; Zawya, 19 Nov |
| 17 Dec 2026 | CBE MPC meeting (last of 2026) | EnterpriseAM, 22 Nov |
| 20 Dec 2026 | First Gemini AE3/NE3 Suez sailing (Alette Maersk, Shanghai) | gCaptain, 16 Nov |
| 31 Dec 2026 | End of phase 1 of the export rebate programme | EnterpriseAM, 8 Nov (`e_rebate.txt`) |
| 1 Jan 2027 | Private-sector minimum wage EGP 8.5k; CBAM definitive phase begins | EnterpriseAM, 16 and 18 Nov |
| Early Jan 2027 | End of 45-day fertiliser gas/export arrangement | EnterpriseAM, 16 Nov |
| 14 Jan 2027 | First Gemini AE1/NE2 Suez sailing (Damietta Express, Shanghai) | gCaptain, 16 Nov |

---

## Not verified / dropped

**Not verified (seen in search results only; the pages could not be fetched, so do not publish):**
- **Export rebate briefing details (15 Nov).** Youm7, Maspero, El Balad, Banker, Veto, Alouroba, Youlyou, Estsmar Arabe, Nile News and Amwal Al Ghad English were all refused by the proxy. The snippets mention Upper Egypt and border support rising from 25% to 40%, the quality-certificate incentive from 30% to 60%, the target-market incentive held at 25%, and a "digital tools" push. Payment timing and eligibility under the new rules are still unverified.
- **Official CBE USD/EGP rate for 16–22 Nov.** The snippets give 53.66/53.80 on 18 Nov (Al Bawaba) and 53.74/53.88 on 19 Nov (Banker). Both hosts and cbe.org.eg were blocked.
- **Customs (ACI/Nafeza/GOEIC/fees).** No customs decree, Nafeza change, fee change or GOEIC rule dated 16–22 Nov was found on any fetched page. Search results only showed older items:
  - Decree 262/2026 (June)
  - Importers Register Decree 271/2026 (in force 22 Jul)
  - paperless customs from 29 Oct
  
  A customs-law amendment package that "the House discusses in November" appeared in a search summary only. Its status is unverified.
- **SCA rebates or new circulars, and any SCA revenue or transit statement for 16–22 Nov:** none found. The "1,490 vessels in October" figure is now confirmed second-hand in EnterpriseAM (17 Nov: "transits up 32% to 1,490 vessels, Suez Canal Authority Chairman Osama Rabie said earlier this month"). It can be used with that attribution.
- **SCZone own announcements (Waleid Gamal El-Dien, Sokhna contracts):** sczone.eg and all Arabic outlets were blocked. Only third-party SCZone items (Amea, the India zone) are verified.
- **Carrier suspensions of Jeddah or Saudi Red Sea calls after the 20 Nov Houthi warning, and war-risk premium figures (0.75% of hull value):** search snippets only, older or unfetched.

**Dropped (verified but not material, or already covered in Issue 001):**
- Remittances (USD 38.2 bn, 9M), October CPI 12.7%, PMI 47.2 and the CBE hike were all covered in Issue 001, with no new data this week.
- EGX listings (Misr Life, MNT-Halan), real estate, AI data centres (Project Atlas), and the EBRD loans to NBE and Tube were dropped as not freight-relevant.

**Hosts refused this week:** dailynewsegypt.com, youm7.com, amwalalghad.com, en.amwalalghad.com, sis.gov.eg, cabinet.gov.eg, mof.gov.eg, customs.gov.eg, sczone.eg, capmas.gov.eg, alborsaanews.com, arabfinance.com (direct), gate.ahram.org.eg, masrawy.com, elwatannews.com, almasryalyoum.com, shorouknews.com, businesstodayegypt.com, banker.news, albawabhnews.com, almalnews.com, akhbarelyom.com, vetogate.com, elbalad.news, maspero.eg, nile.eg, reuters.com, arabnews.com, thenationalnews.com, lloydslist.com, maritime-executive.com. english.ahram.org.eg and egypttoday.com returned 403 Cloudflare, and cbe.org.eg returned "Request Rejected" (WAF).
