# up-colleges-filled.csv — verification notes

## Status: PARTIAL (rows 1–112 researched, rows 113–239 untouched)

The session reached its web-search limit (200 searches) partway through batch 12.
Rows 113–239 (from `institute-of-engineering-and-technology-3`, Jhansi, onward) are unchanged
apart from what was already in the input (district). All 239 rows are present, in the original order,
with slug, name and state unchanged.

## How values were sourced
Same method as the West Bengal file. College sites could not be opened directly (network egress blocked),
so every value comes from web-search results restricted to the college's own domain. Aggregators were excluded,
and anything unconfirmed or conflicting was left empty. latitude, longitude and brochure_url are empty everywhere.

- **exams_accepted = jee-main** is set only where the college is confirmed as an AKTU-affiliated B.Tech college
  (the site says so, or AKTU's own "Know Your College" portal lists it). The UP state counselling portal
  (uptac.admissions.nic.in) runs B.Tech rounds on JEE Main. It is also set for JIIT, which states JEE Main admission.
  IIT/IIIT/MNNIT rows were not reached.
- **NIRF left empty** everywhere, for the same reason as the West Bengal file: the latest edition could not be confirmed.

## NOT FOUND
- `baba-ramdal-surajdev-engineering-college`: only "Baba Ramdal Surajdev Polytechnic College" and a PG college
  exist online under that name. No engineering college site was found.

## District changed
- `jms-group-of-institutions`: Ghaziabad → Hapur (official address is Hapur Bypass Road, Hapur 245101).

## Please check
- **Maya Institute of Pharmacy:** streams set to `pharmacy`, because the institute offers no engineering programme.
  Change it back if your stream list has no `pharmacy` slug.
- **KIET Ghaziabad:** now a deemed-to-be university (November 2025, per kiet.edu), so college_type is DEEMED.
  The NAAC grade was left empty because the site says both A and A+.
- **Likely duplicate rows:**
  - `delhi-technical-campus` / `dtc-college` (both are Delhi Technical Campus, affiliated to GGSIPU, not AKTU)
  - `r-d-engineering-college` / `r-d-engineering-college-and-research-centre` (one site, rdec.ac.in)
  - `greater-noida-institute-of-technology-engineering-institute` (only the GNIOT website was filled)
- **Websites to double-check:**
  - KCNIT (kcnit.ac.in): a hosting-suspended page appeared in the search results.
  - Institute of Engineering and Technology, Ayodhya: the ietrlau.in homepage now serves spam, so the
    university faculty page was used instead.
  - Maharaja Suhel Dev University: website and address left empty (two domains, msdsu.ac.in and msdu.ac.in, and two addresses).
- **http only:** gnitm.org.in, bulandshahr.mit.asia, csauk.ac.in (CAET Etawah page), imsec.ac.in,
  idealinstitute.ac.in, adhunikinstitute.edu.in, miteducation.org.
- **NAAC left empty (lapsed or unclear):**
  - Dayalbagh Educational Institute (A+, 3.4, awarded 2019).
  - Accurate (site says A+ and B++).
  - Galgotias CET, IET Agra, DBRAU.
- **Pincode dropped:** RBCET (site shows 224001, which is not a Bareilly pincode).
