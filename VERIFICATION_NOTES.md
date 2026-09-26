# colleges-filled.csv — verification notes

## How values were sourced

The session container could not open college websites directly (network egress blocked).
Every value was taken from web-search results **restricted to the college's own domain**
(or the affiliating university's domain). Aggregators were excluded. Nothing was guessed;
anything unconfirmed or conflicting was left empty.

Consequences interns should know:
- `official_website`: the domain was confirmed through search results, but the pages were not opened in a browser.
- `description` / `about`: written in my own words, using only facts found on the college's site.
- `latitude` / `longitude`: left empty everywhere (no confident official source).
- `brochure_url`: left empty everywhere.
- `exams_accepted`: `wbjee` was set only where the college appears in the WBJEEB institute-profile
  list (wbjeeb.in/assets/ALPG/...) or its own site says so. `jee-main` / `jee-advanced` were set
  for JoSAA institutes (IIT Kharagpur, NIT Durgapur, IIEST, IIIT Kalyani, GKCIET) and UEM.
  Empty means "not confirmed", not "no exam".

## NOT FOUND
- `kingston-college-of-advanced-engineering-and-management`. The Kingston group site (keical.edu.in)
  does not mention this college, and engineering.kingston.ac.in is a different college in Tamil Nadu.

## District changed (clearly wrong in input)
- `alipurduar-government-engineering-and-management-college`: JALPAIGURI → ALIPURDUAR (official address: District Alipurduar)
- `seacom-engineering-college`: KOLKATA → HOWRAH (official address: Sankrail, District Howrah)

## Please check
- **NIRF left empty on purpose.** NIRF pages were unreachable and it is unclear whether NIRF 2026
  engineering results are out. Official sites show these **2025** engineering ranks: IIT Kharagpur 5,
  Jadavpur University 18, NIT Durgapur 49. Fill `nirf_rank` once the latest edition is confirmed.
- **NAAC left empty (possibly expired or unclear):**
  - Haldia Institute of Technology: A, 3.31, but the site's approval letter is valid only to 31-12-2025.
  - Heritage Institute of Technology: B++ (2017) lapsed; newer documents mention A with no dates.
  - University of Calcutta: A, 3.2, valid only to 2022.
  - University of Kalyani: A, 3.12, date unclear.
  - DIATM, JGEC, SIT Siliguri, OmDayal, Aliah and others: say "NAAC accredited" but give no grade.
- **Two official-looking domains, so website left empty:**
  - `bengal-institute-of-technology-and-management`: bitm.org.in vs bitms.ac.in
  - `camellia-institute-of-technology-and-management`: citm.org.in vs citm.edu.in
  - `camellia-school-of-engineering-and-technology`: cset.ac.in vs cset.org.in
  - (Filled but double-check: CIET → ciet.ac.in (also ciet.net.in), MCET → mcetbhb.net (also mcet.org.in),
    Dream → dreaminstituteonline.com (also .edu.in), TIEM → tiem.edu.in (also tecb.edu.in).)
- **http only.** These sites were only seen over http, so check whether https works:
  besdiet.org, gcettb.ac.in, paradiseinstituteoftechnology.com, hmcekalyani.org.
- **Rows with almost nothing filled:**
  - `bishnupur-public-institute-of-engineering-b-tech`: site shows only polytechnic/ITI.
  - `paradise-institute-of-technology`: site shows a diploma polytechnic only.
  - `dr-sudhir-chandra-sur-institute-of-technology-and-sports-complex`: site returned no details.
- **Duplicate rows.** `university-college-of-science-and-technology` and
  `university-college-of-science-and-technology-calcutta-university` appear to be the same institution
  (CU, Rajabazar). Both were filled identically.
- **District possibly wrong (left unchanged).** `camellia-institute-of-technology` (Madhyamgram is in
  North 24 Parganas; input says KOLKATA). Several New Town and Salt Lake institutions also carry KOLKATA.
- **Mallabhum Institute of Technology.** The site search returned a Navi Mumbai address (web-vendor
  footer), so address was left empty.
- **college_type for government autonomous colleges** (JGEC, GCECT, KGEC) was set to GOVERNMENT, not
  AUTONOMOUS, because only one value is allowed.
