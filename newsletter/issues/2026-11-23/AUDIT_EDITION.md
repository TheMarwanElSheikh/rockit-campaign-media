# Audit: The Rockit Manifest, Voyage 002 (full edition, 23 November 2026)

**Method.** Four research desks worked in parallel on 22 November 2026: ocean, air & logistics, geopolitics, and Egypt & region.
- Every item was found by search, then read on the fetched page (`curl`, text extracted).
- The notes, with URLs, dates, verbatim quotes and statuses, are in `research/`.
- Search snippets alone were never used.
- The edition cites 96 sources (list on pages 14–15). Source ids map to `SOURCES` in `edition_content.py` and `part_ocean_air.py`.

**Status key:** P = primary source read; T = trade or press report read; R = claim by a party to a conflict, reported as such; S = secondary digest only, attributed in text.

## Claims by page

| Page | Claim | Source id(s) | Status |
|---|---|---|---|
| 1, 3 | Xeneta FE→Med $4,989 (+6.8%), FE→N. Europe $3,438 (−2.3%), Med premium $1,551; Bab el-Mandeb transits 16.6→11.9/day | xeneta20 | P |
| 1, 4 | 57 Suez container transits in week to 15 Nov (+73% y/y); 60% of Asia–Europe capacity on Suez; Cape 126 | drewry_redsea | P |
| 1, 4 | Gemini NE1/NE3/NE2 to Suez; ~4 Dec, ~20 Dec, ~14 Jan sailings; *Damietta Express* 23,700 TEU | cn_gemini, ls_gemini | T |
| 1, 4 | Houthis seized Yemen's Red Sea coast; coalition struck Hodeidah 20 Nov; Saree told ships to leave Saudi ports; threat to Jeddah; Yemeni minister says Hodeidah operational | gc_houthi, sb_oil | T + R |
| 1, 9 | *BETUL 8*, wheat Tulcea→Egypt, capsized 16 Nov after reported sea-drone strike; 12 rescued; unattributed | gc_betul | T + R |
| 1, 6 | WorldACD wk 45 global $3.45/kg (+2% w/w, +31% y/y); MESA +63%; MESA–Europe +66%; Dubai +83%; Saudi −33% | st_wcd45 | T |
| 1, 10 | IMF staff-level agreement 18 Nov; ~$1.5bn EFF + up to ~$0.8bn RSF; total ~$9.6bn; Board before 15 Dec | eam_imf, zw_imf | T |
| 2, 3 | Drewry WCI $4,176 (−3%); Shanghai–Genoa $4,436 (+6%); Rotterdam $3,496; Dec PSS $1,000–1,600 | drewry | P |
| 3 | Freightos FBX13 ~$4,300 (−1%), FBX11 ~$3,400 | freightos17 | P |
| 3 | MSC Dec FAK E. Med $5,100/$6,500 (+$800), W. Med $6,500 (+$1,200), Algeria/Libya-Tunisia/Casablanca $8,200/$8,000/$7,000; GFS $304 (Nov $266); valid to 14 Dec | cn_msc_fak | T |
| 3 | Maersk FE→Med PSS $750/$1,500, PCD 23 Nov, Egypt in scope | cn_asiamed | T |
| 3 | Hapag-Lloyd FAK Egypt/Türkiye/E. Med $5,300/$6,600 from 1 Dec | cn_hapag_fak | T |
| 3 | CMA CGM 1–14 Dec E. Med $5,500/$6,800; N. Africa $6,400/$8,800 (incl. bunker, ETS, LSS); Egypt inclusion not stated (said in text) | cn_cma_dec | T |
| 4 | AE11 Port Said (Estelle Maersk 17 Nov), AE19 Damietta (Ane Maersk 18 Nov), AE12 Port Said East; departures not confirmed (said in text) | cn_gemini_oct, hsn_maersk | T (PARTIAL) |
| 4 | UKMTO 115/148 transits (was 139/169); 6 verified attacks to 18 Nov; Orbital Risk 15 incidents (+50%); 7 strikes on 6 ships near Khasab; JMIC SEVERE | gc_hormuz20 | T |
| 4 | Kpler Hormuz oil ~10m b/d (13.4m start of Nov) | gc_iran_attacks | T |
| 4 | TARA GAS hit 16–17 Nov, 1 missing; NAVIG8 MESSI 17 Nov, 1 missing, 11 injured; strikes 20–21 Nov; Iran mine claim unverified (said in text) | gc_taragas, gc_hormuz20, gc_oman21 | T + R |
| 4, 13 | MSC Fujairah Shuttle 2 from December | cn_msc_fuj | T |
| 5 | VLSFO G20 $838 (−$25.50), Fujairah $800, Singapore $842, Rotterdam $705.50; MGO $1,364; 13 Nov $863.50 | sb_prices | P |
| 5 | Brent ~$92; ~15% down in November | sb_oil | T |
| 5 | Hapag-Lloyd MFS from 1 Jan 2027, Suez-based, quarterly; Q1 rates 1 Dec | sb_hapag_mfs | T |
| 5 | Drewry: on-time 40%→34%; 42 blank sailings of 724 (6%); transpacific 48%, Asia–Europe/Med 33% | drewry_blank | P |
| 5 | ZIM Q3 net $830m (vs $123m), revenue $2.71bn (+53%), $2,480/TEU (+55%), guidance $3.3–3.5bn | cn_zim | T |
| 5 | IMO ISWG 23–27 Nov, MEPC 85 30 Nov–3 Dec, MEPC.ES/2 4 Dec "subject to confirmation"; 9 associations 18 Nov; FMC "cannot be adopted" | imo_cal, gc_imo_assoc, sb_fmc | P + T |
| 5 | MSC carbon surcharge $133/TEU Med (in Why it matters) | cn_msc_fak | T |
| 5 | LA/LB watchmen tentative deal 21 Nov | gc_lalb | T |
| 6 | Freightos via Loadstar: Europe–US $3.27/kg (+12%), highest since Dec 2022; China–N. America $9.25 (+16%) | ls_tatl | T |
| 6 | Aevean: Gulf hubs −12% (~2,200 t/day); foreign freighters −49%; Xeneta 2027 −5–10% conditional | ls_cap | T |
| 6 | Jet fuel $169.82/bbl (−5.1%), week not dated on IATA page (said in tile) | iata_fuel | P (PARTIAL) |
| 6 | Cathay Oct 162,747 t (+7.5%), capacity +0.5%; Korean Air quote | st_cx, ls_kal | T |
| 6 | CH Robinson: Asia–Europe capacity available (as reported) | st_ai_peak | T |
| 6 | DHL GF 747F HKG–Navi Mumbai–Liège, 25–30 t; ~20 freighters in 2027 | acn_dgf_india, fw_dgf | T |
| 6 | Bangkok >1,000 lots; US ground stop 13 Nov, recovered 15–16 Nov | acn_bkk, acn_us_gs | T |
| 6 | IATA after ATConf/7: CORSIA vs EU ETS; weakest pax growth since 2009 | iata_icao | P |
| 7 | DAWB white paper 16 Nov (AfA, NCBFAA; IFCBAA, CIFFA) | acn_dawb | T |
| 7 | EU €2 fee from 1 Nov + €3 duty since 1 Jul; 555m vs 1.51bn items in Q3; €5 per line | eu_cust, ls_bf | P + T |
| 7 | CMA CGM/CEVA Q3 figures; Arvato–Ekol; Logisteed–Neovia; UPS–Smartways; Expeditors; DHL SC; DFDS–Ekol road | ls_cmagap, ls_ekol, acn_ups, ls_expd, st_dhlsc | T |
| 7 | DHL Express photo descriptions; CargoQUALITY | fw_dhlx, acn_cargoai | T |
| 7 | India–Gulf: Khor Fakkan congestion, Sajaa empty-return up to $1,200/40ft; Emirates–Virgin MoU | ls_indgulf, acn_ekvs | T |
| 8 | Trump–Xi–Putin trilateral, 90 min, nuclear-war declaration, refined-products pledge | eam_apec | S |
| 8 | No new Section 301 maritime notice 13–22 Nov | fr_api | P (search) |
| 8 | USTR 6 Nov readout (Greer, Bessent, He Lifeng) | ustr_call | P |
| 8 | BIS rule 19 Nov (91 FR 74970): licences for ID, MY, SG, TH, BR; remote access; "import restrictions" | fr_chips | P |
| 8 | Greer WSJ letter: 19 partners, ~40% of GDP | ustr_wsj | P |
| 8 | AGOA: Rwanda, South Africa from 1 Jan 2027 (intent) | ustr_agoa | P |
| 8 | Port-fee suspension to 9 Jan; China truce to 10 Jan | fr_portfee, gc_truce | P + T |
| 8 | CENTCOM STS advisory 18 Nov; Qeshm strike 17 Nov (US official), Mehr: no casualties; Treasury in SG/MY; Qatar mediating | gc_sts, gc_qeshm, gc_treasury | T + R |
| 9 | WTO: 333 restrictive measures H1 2026 vs 300 in 2025; $5.4tn, 21.3% | wto_mon | P |
| 9 | 17 ships attacked off Bulgaria/Romania since mid-July (Diaplous via Reuters); GAS HUSKY sank 17 Nov | gc_gashusky | T |
| 9 | EU sanctions 16 Nov: 12 + 101; UAE/Oman/Seychelles/China; Balance Insurance; ~50 banks | gc_eusanc | T |
| 9 | CBAM Reg. 2026/2498 (10% credit cap); Norway/Iceland from 1 Jan 2027; EU–UK ETS link 20 Nov | ec_cbam_ded, ec_cbam_no, ec_ets_uk | P |
| 9 | Egypt off EU draft scrap list; ban from 21 May 2027; lobbying; EU ~half of Egypt's ferrous scrap (EnterpriseAM sources) | eam_scrap | S (PARTIAL) |
| 9 | EU Customs Authority first board 19 Nov, Lille; Data Hub replaces 100+ systems | ec_euca | P |
| 10 | Goldman: hold at 20% to late Q1 2027; EGP 53/52/50 | eam_gs | T |
| 10 | Dollar back above EGP 54, 22 Nov (bank trading); last CBE quote read 53.39 (12 Nov) | zw_egp, eam_db | T |
| 10 | NIR $57.5bn end-Oct (+$151.6m) | eam_noimf | T |
| 10 | Sept imports $10.6bn (+29.7%), exports $5.3bn (+7.4%), deficit $5.3bn (+60.6%) | zw_deficit | T |
| 10 | AU trade $8.2bn (+15.3%); exports $6.1bn; Libya 1.2, Sudan 0.9, Morocco 0.7, Algeria 0.7, Tunisia 0.4 | zw_africa | T |
| 10 | Suez Canal activity +47.5% in Q1 FY26/27; GDP +4.9% | zw_gdp | T |
| 10 | Rebate rules (35%; 50% freight; 25% inland/insurance/express; complete files; EGP 48bn); briefing held 15 Nov, content not verified (said in text) | eam_rebate, eam_briefing | T |
| 11 | Yang Ming EG1–EG3; Sidra WAF loop (750 TEU); EBRD–Mesco EGP 585m | cn_yangming, cn_sidra, eam_mesco | T |
| 11 | MAF–DP World Sokhna–Jebel Ali reefer MoU, no numbers | eam_backsuez | T |
| 11 | Fertiliser: $175m upfront, $12.75/mmBtu (from $8.5), 45 days from 16 Nov, exports to early Jan, cuts 20–40% (Asharq via EnterpriseAM) | eam_fert | S |
| 11 | ISSC Damietta first non-EU CBAM verifier; Egypt 44.3% of EU non-EU urea imports (CBAM Guide/Eurostat via EnterpriseAM) | eam_issc | S |
| 11 | India $12bn target by 2030 (from $6.5bn), FTA to explore; China ~$20bn | eam_india, zw_china | T |
| 11 | Egypt–Libya agreements 19 Nov; Dbeibeh raised visas and border | zw_libya | T |
| 11 | MSC North India–Red Sea service late Nov, 2,500–3,000 TEU | cn_msc_redsea | T |
| 11 | ADNOC L&S attack 17 Nov; Lehmacher "USD 1k a container to cross Hormuz" (quote, not a tariff; said in text) | eam_whosail | T (quote) |
| 11 | Saudi road-freight registrations +52% to 104,612 in Q3 | zw_saudi | T |
| 11 | Minimum wage EGP 8,500 from 1 Jan 2027 (+21%), 26.5m workers | eam_wage | T |
| 12–13 | Toolkit, checklists and calendar restate figures above; the Six questions table is Rockit guidance, no figures | as above | — |

## Removed or not used (and why)

- **APEC trade outcome** (truce extension, rare earths, a G20 follow-up): snippets only, on blocked hosts. The edition says no deal could be verified.
- **Export-rebate briefing details** (Upper Egypt support 25→40%, quality certificates 30→60%, "digital tools"): snippets from blocked Arabic outlets. The edition says the content could not be verified.
- **Official CBE quote for 16–22 Nov** (53.66–53.88 in snippets): the CBE site is blocked. The edition uses the last quote read (12 Nov) and Zawya's "above 54".
- **Customs** (ACI/Nafeza/GOEIC/fees): nothing dated in the window on readable pages. The edition says so on page 11.
- **SCA statements and rebates in the window:** none found.
- **TAC/Baltic weekly air index; WorldACD wk 46; IATA October cargo data:** not available on readable hosts, or not yet released.
- **European airport and port strikes:** recycled or blocked claims.
- **EgyptAir Cargo–Unilode and Cardiff items:** blocked hosts; the Unilode deal dates from 2024.
- **CH Robinson–RXO:** outside the window.
- **Drewry "four vessels crossed Hormuz":** vessel type unspecified; conflicts with UKMTO totals.
- **War-risk premium percentages:** not verified.
- **Sea-Intelligence October GLP:** not found.
- **Cut for space after the build** (verified, footnotes removed with the text):
  - Romania's Sulina drone strikes
  - *SPARTA II* fire
  - WTO steel Article XXVIII extension
  - Amea Power SCZone turbine factory
  - JFK AGI dispute
  - SCFI readings

## Brand and build checks

- **Logo:** `brand/rockit-logo.svg`, vector, on white covers and in every footer. The email header and footer use `rockit-logo.png` on white. No dark panel sits behind the logo.
- **Gold:** the `gold-swoosh` gradient on rules and bars. Small gold text on light surfaces uses #8a6514.
- **Overflow check:** `render_edition.js` reported no overflow on all 16 pages after rebalancing. Every page PNG was reviewed visually.
