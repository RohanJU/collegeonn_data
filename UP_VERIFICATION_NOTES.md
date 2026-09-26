# up-colleges-filled.csv — verification notes

## Status: COMPLETE (all 239 rows researched)

Rows 1–112 were done in the first session and rows 113–239 in a second session (about 160 of 200 searches used).
All 239 rows are present, in the original order, with slug, name and state unchanged. A final check against
up-colleges-to-fill-2026-09-26.csv passed: same header, row count, slugs, names and states; every pincode has 6 digits
and appears in its address; every year has 4 digits.

## How values were sourced
Same method as the West Bengal file. College sites could not be opened directly (network egress blocked),
so every value comes from web-search results restricted to the college's own domain. Aggregators were excluded,
and anything unconfirmed or conflicting was left empty. latitude, longitude and brochure_url are empty everywhere.

- **exams_accepted = jee-main** is set only where the college is confirmed as an AKTU-affiliated B.Tech college
  (the site says so, or AKTU's own "Know Your College" portal lists it). The UP state counselling portal
  (uptac.admissions.nic.in) runs B.Tech rounds on JEE Main. It is also set for JIIT, which states JEE Main admission.
  It is jee-main for IIIT Lucknow, IIIT Allahabad and MNNIT, and jee-advanced for IIT Kanpur and IIT (BHU).
  Some colleges are affiliated to AKTU only because AKTU's "Know Your College" portal (erp.aktu.ac.in) lists them, and their own site could not be confirmed.
  Their descriptions say this.
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

## Rows 113–239 (second session)

### NOT FOUND (no official site confirmed)
- `faculty-of-engineering-and-technology-3` (Kanpur Nagar): the name is ambiguous. It could be Rama University's
  "Faculty of Engineering & Technology" or CSJMU's UIET, which is already covered by the CSJMU row. The row was left empty.
- `j-p-institute-of-technology` (Lucknow): no official site found. jpiet.in belongs to JP Institute of Engineering &
  Technology, Meerut (row 187), so it was not reused.
- `rishi-ramnaresh-technical-institute` (Mau): only aggregators list it, as a diploma institute. No official site was found.
- `nalanda-institute-of-technology-2` (Saharanpur): search results only showed the Nalanda institutes in Bhubaneswar and Bihar.
- `svs-group-of-institions` (Meerut): the domain svsit.ac.in that an aggregator gave is a Warangal college. The group's own
  site (email domain svs.ac.in) never appeared in results.
- **No website, but AKTU affiliation confirmed from the AKTU portal:** `rishi-institute-of-enginnering-and-technology`,
  `prayag-institute-of-technology-and-management`, `dr-virendra-swarup-memorial-trust-group-of-institution`.

### District changes
- None in rows 113–239.
- **Possible district fix:** `rajarshi-rananjay-sinh-institute-of-management-and-technology` is at Munshiganj, **Amethi**,
  but the input says Sultanpur. District and city were left unchanged because no official address was confirmed.

### Please check
- **Not engineering:** `lucknow-public-college-of-professional-stidies` (LPCPS) and
  `institute-of-professional-studies-and-research-ipsr` (IPSR Unnao) had no engineering programme confirmed. IPSR's
  site describes pharmacy and management, and LPCPS lists general degree courses. streams was left empty for both.
- **Diploma only:** `shri-vishwanath-college-of-technology` is a polytechnic. streams stays engineering, for its diploma courses.
- **Conflicts:**
  - REC Pratapgarh (recp.ac.in): the site shows a Gonda "Utraula Road" address, apparently copied from another REC.
    The address was left empty.
  - SIETM Unnao (sietm.com): the site says it was "established by the Government of Uttar Pradesh in 2009", which
    contradicts it being a private college. college_type and year were left empty.
  - Apollo Institute of Technology (apolloit.ac.in): one page calls it an "Autonomous College". college_type was left empty.
  - MIPS and MPEC Kanpur share mpgi.edu.in. The MPEC year is 1999 per mpgi.edu.in; an aggregator said 2009.
- **Group websites:** these rows use a group or university page, not a college-only site.
  - Landmark Technical Campus (landmarkgroups.co.in)
  - Krishna Institute of Technology (kgikanpur.in)
  - Maharana Pratap Engineering College (mpgi.edu.in)
  - Saroj Institute of Management and Technology (now a page on sarojuniversity.edu.in; affiliation left empty)
  - Axis Institute of Technology and Management (axiscolleges.in)
- **Deemed or university status:**
  - Shobhit (SIET) is DEEMED, with NAAC A and CGPA 3.12, valid five years from 20 Dec 2022.
  - CSJMU (STATE) has NAAC A++. HBTU (STATE) and PSIT have NAAC A+.
  - KMCLU is a STATE university. MUIT is a PRIVATE university.
- **college_type left empty:** IIIT Lucknow (ownership PPP, as its site states) and IIIT Allahabad. The allowed list has
  no "institute of national importance" type.
- **IIT (BHU):** established_year is 1919, when engineering teaching began with Banaras Engineering College.
  It became an IIT in 2012.
- **Possible duplicate:** `modern-college` (Jhansi) uses moderncollege.tech. Other "Modern College Jhansi" sites also exist
  (moderncollegejhansi.com, mgijhansi.com).
- **http only:** hardayal.in, fgiet.ac.in, shantieng.in.
- **Fixed from the first session:** `i-t-s-engineering-college` had a pincode (201308) but no address. The pincode was removed.
