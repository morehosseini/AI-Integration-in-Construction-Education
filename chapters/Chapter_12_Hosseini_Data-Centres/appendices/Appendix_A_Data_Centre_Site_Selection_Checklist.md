# Appendix 1 — Data Centre Site Selection Checklist (Standards-Anchored, Example Only)

## Disclaimer (read first)
This appendix is a **small, simplified educational example** compiled from selected siting-related material in the standards listed below. It is **not sufficient for real projects** and **must not be used for actual site selection, design, procurement, compliance, or risk decisions**. Real data-centre siting requires project-specific due diligence, qualified professional advice, stakeholder engagement (e.g., utility/network providers), and jurisdictional approvals.

---

## Standards consulted (traceability)
- **ANSI/TIA-942** — *Telecommunications Infrastructure Standard for Data Centers* (Annex on Site Selection / siting considerations).
- **ANSI/BICSI 002** — *Data Center Design and Implementation Best Practices* (Site Selection section; includes **recommended minimum separation distances** in its siting table).
- **EN 50600-2-1** — *Information technology — Data centre facilities and infrastructures — Part 2-1: Building construction* (location/site assessment requirements; largely **process- and risk-assessment-oriented** rather than fixed distances).

> **Note:** Only some sources provide numeric separation distances. Where numeric distances appear, they should be treated as **examples from the cited standard’s guidance** and must still be validated against local conditions, current editions, and project risk appetite.

---

## How to use this appendix
Use this checklist to structure early-stage **screening** and to understand typical **civil/construction engineering** considerations:
1) Screen out obvious “no-go” sites.  
2) Identify **risks requiring mitigation** (design, procurement, operations).  
3) Document assumptions and evidence (maps, records, utilities, route studies).  
4) Escalate to competent specialists (geotech, structural, MEP, security, telecom).

---

## 1) Regional hazard and geotechnical screening

### 1.1 Flood, storm surge, and water-related hazards
- ☐ Site is **outside mapped flood hazard areas** (e.g., 1% AEP / “100-year floodplain” mapping) and has a documented flood study (**TIA-942; EN 50600-2-1**).
- ☐ Finished floor levels for critical spaces are above expected flood levels; no critical infrastructure placed in high-risk basements (**TIA-942**).
- ☐ Avoid locations **downstream of dams / water towers** where failure consequences are unacceptable (**TIA-942**).

### 1.2 Seismic and ground failure hazards
- ☐ Seismic hazard category identified and appropriate performance objectives established (**TIA-942; BICSI 002; EN 50600-2-1**).
- ☐ Liquefaction susceptibility assessed; mitigation feasibility documented (ground improvement, deep foundations) (**EN 50600-2-1** risk assessment framing).
- ☐ Fault proximity, surface rupture zones, and lateral spreading considered (**TIA-942**).

### 1.3 Slope stability and terrain
- ☐ Avoid landslide-prone terrain; slope stability evaluated (including cut/fill and retaining needs) (**TIA-942; EN 50600-2-1**).
- ☐ Prefer gentler terrain for construction logistics and drainage (**BICSI 002** practical siting guidance).

### 1.4 Bushfire/wildfire and extreme weather
- ☐ Bushfire/wildfire exposure assessed; defensible space, access, and emergency response considered (**BICSI 002; EN 50600-2-1**).
- ☐ Extreme wind / cyclone exposure and debris risk assessed (structural and envelope implications) (**BICSI 002; EN 50600-2-1**).
- ☐ Lightning density considered (earthing/bonding, surge protection) (**EN 50600-2-1**).

### 1.5 Altitude and microclimate
- ☐ Elevation considered due to cooling/engine derating effects; both TIA and BICSI guidance reference **~3050 m (10,000 ft)** as a practical upper bound for preferred siting (**TIA-942; BICSI 002**).
- ☐ Heatwaves and humidity regime considered (cooling plant sizing, redundancy strategy) (**EN 50600-2-1**).

---

## 2) Separation distances from man-made hazards (numeric examples where specified)

### 2.1 ANSI/BICSI 002 — recommended minimum separation distances (Site Selection siting table)
The following are **examples** of recommended minimum distances from selected man-made elements **as provided in ANSI/BICSI 002** (Site Selection separation-distance table):

| Hazard / adjacency element | Example minimum separation distance | Standard / reference |
|---|---:|---|
| Airports | ≥ **8 km** | ANSI/BICSI 002 (Site Selection table) |
| Chemical plants / chemical storage | ≥ **8 km** | ANSI/BICSI 002 (Site Selection table) |
| Conventional power plants (coal/gas) | ≥ **8 km** | ANSI/BICSI 002 (Site Selection table) |
| Nuclear power plants | ≥ **80 km** | ANSI/BICSI 002 (Site Selection table) |
| Military installations / munitions storage | ≥ **13 km** | ANSI/BICSI 002 (Site Selection table) |
| Railroads | ≥ **1.6 km** | ANSI/BICSI 002 (Site Selection table) |
| Hazardous-materials transport corridors | ≥ **1.6 km** | ANSI/BICSI 002 (Site Selection table) |
| Landfills / waste storage | ≥ **3.2 km** | ANSI/BICSI 002 (Site Selection table) |
| Water/sewage treatment plants | ≥ **3.2 km** | ANSI/BICSI 002 (Site Selection table) |
| Dams/reservoirs/lakes | ≥ **3.2 km** | ANSI/BICSI 002 (Site Selection table) |
| Embassies / political group properties | ≥ **5 km** | ANSI/BICSI 002 (Site Selection table) |
| Radio/TV transmitters | ≥ **5 km** | ANSI/BICSI 002 (Site Selection table) |

> **Important:** These values are guidance examples. For real projects, confirm the **current** edition of the standard and reconcile with local hazard mapping and risk assessment.

### 2.2 ANSI/TIA-942 — hazard avoidance and proximity considerations (qualitative)
TIA-942 site selection guidance emphasizes **avoiding** proximity to hazards such as:
- Floodplains, fault lines, unstable slopes, and being downstream of dams/water towers.
- Railroads and major highways where chemical spill risk is elevated.
- Airport flight paths and other high-risk adjacencies.

> TIA-942 is frequently used alongside tiering/certification guidance in industry. Treat any numeric siting distances found in those ancillary documents as **tier- and context-dependent** and verify against the latest authoritative text and the project’s required tier level.

---

## 3) Power infrastructure (grid access, redundancy, and constructability)

### 3.1 Utility power availability and resilience
- ☐ Utility can supply initial capacity **and future expansion** (load growth plan documented) (**TIA-942; EN 50600-2-1**).
- ☐ Options for **redundant feeders** (ideally from independent substations) assessed (**TIA-942**).
- ☐ Grid reliability and outage history reviewed (including planned works and fault response times) (**BICSI 002** risk assessment approach).

### 3.2 On-site generation and fuel logistics
- ☐ Space and permitting feasibility for generators, fuel storage, and emissions/noise compliance assessed (**TIA-942; BICSI 002**).
- ☐ Fuel delivery routes and continuity during emergencies assessed (**BICSI 002**).
- ☐ Fire protection implications (bunding, separation, hazardous area controls) considered (engineering good practice; align with AHJ).

### 3.3 Earthing, EMC, and lightning
- ☐ Grounding/earthing strategy feasible given soil resistivity and site conditions (**BICSI 002**).
- ☐ Electromagnetic interference sources reviewed (rail traction power, transmitters, heavy industrial plant) (**BICSI 002**).

---

## 4) Telecommunications connectivity and route diversity

- ☐ Availability of multiple service providers confirmed early (**TIA-942**).
- ☐ **Diverse fibre routes** verified (not just different providers on the same duct/path) (**TIA-942**).
- ☐ Separate building entry points and protected pathways considered (**TIA-942**).
- ☐ Proximity to carrier interconnect facilities / “carrier hotels” considered where latency and diversity are critical (**BICSI 002**).

---

## 5) Water and cooling-related siting considerations

- ☐ Water availability evaluated (where water-based cooling is contemplated); drought constraints and competing demand considered (**EN 50600-2-1** site assessment framing).
- ☐ Discharge constraints and reuse opportunities assessed (regulatory approvals; community acceptance) (**EN 50600-2-1**).
- ☐ Ambient conditions assessed for free-cooling potential and plant sizing strategy (**BICSI 002**).
- ☐ Opportunity for **waste-heat reuse** considered (**EN 50600-2-1** location assessment themes).

---

## 6) Access, construction logistics, and emergency response

### 6.1 Site access and delivery logistics
- ☐ At least two independent access routes considered (**TIA-942; BICSI 002**).
- ☐ Heavy vehicle access, turning radii, crane placement, laydown areas, and staging evaluated (**BICSI 002**).
- ☐ Constraints from bridges, load limits, rail crossings, and seasonal disruptions assessed (**BICSI 002**).

### 6.2 Emergency services proximity (examples from BICSI 002 guidance)
- ☐ Fire and police response proximity assessed (BICSI provides practical proximity guidance).
- ☐ Hospital access considered for workforce safety and incident response.

---

## 7) Security, standoff, and adjacency management

- ☐ Controlled perimeter achievable (setbacks, fencing, controlled entry) (**TIA-942**).
- ☐ External plant (generators, cooling equipment, fuel tanks, provider gear) can be placed in secured zones (**TIA-942**).
- ☐ Exposure to protest/blockade risk assessed (**BICSI 002**).
- ☐ Crime risk and local security context assessed (**TIA-942; BICSI 002**).

---

## 8) Planning, environmental, and community constraints

- ☐ Zoning permits the intended use and critical infrastructure (fuel tanks, noise sources, emissions) (**TIA-942; EN 50600-2-1**).
- ☐ Environmental hazards (legacy contamination; asbestos/lead/PCBs where brownfield) assessed (**TIA-942**).
- ☐ Noise, visual impact, traffic impacts, and community acceptance assessed (**EN 50600-2-1**).
- ☐ Opportunities for renewables and local sustainability alignment considered (**EN 50600-2-1**).

---

## 9) Building form and expandability (civil/structural implications)

- ☐ Building footprint supports data hall planning and future expansion (**TIA-942**).
- ☐ Column grid / clear spans support efficient layouts (TIA notes practicality of large clear spans).
- ☐ Floor loading, vibration criteria, and plant-support structures feasible (engineering due diligence; align with project brief).
- ☐ Envelope resilience (wind-borne debris, fire exposure, smoke) suitable for hazard context (**BICSI 002; EN 50600-2-1** risk framing).

---

## 10) Documentation package (what to record)
- ☐ Hazard maps and studies: flood, seismic, bushfire/wildfire, wind, lightning, contamination.
- ☐ Geotechnical investigation summary and foundation concept.
- ☐ Utility “will-serve” / capacity letters and substation/feed options.
- ☐ Telecom route diversity evidence (drawings, duct/path separation).
- ☐ Permitting pathway and constraints register.
- ☐ Risk register with mitigations and residual risk acceptance.

---

## Notes on limitations
- **EN 50600-2-1** is primarily **risk- and assessment-driven** for location/site selection and does not generally provide fixed separation distances in the same way as the BICSI siting table.
- The numeric distances listed above are **examples** from **ANSI/BICSI 002** guidance and must not be treated as universal rules.
