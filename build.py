import csv, json, glob, os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, os.environ.get("SRC", "colleges-to-fill-2026-09-26.csv"))
OUT = os.path.join(BASE, os.environ.get("OUT", "colleges-filled.csv"))
DATA = os.environ.get("DATA", "data")
FILL = ["city","college_type","short_name","description","about","established_year","address",
        "district","pincode","latitude","longitude","ownership","affiliated_to","approvals",
        "naac_grade","naac_score","nirf_rank","nirf_category","official_website","brochure_url",
        "streams","exams_accepted"]
data = {}
for f in sorted(glob.glob(os.path.join(BASE, DATA, "batch*.json"))):
    data.update(json.load(open(f, encoding="utf-8")))
with open(SRC, encoding="utf-8", newline="") as fh:
    rows = list(csv.reader(fh))
header, body = rows[0], rows[1:]
idx = {c: i for i, c in enumerate(header)}
unknown = set(data) - {r[0] for r in body}
assert not unknown, unknown
for r in body:
    d = data.get(r[0], {})
    for k, v in d.items():
        assert k in FILL, (r[0], k)
        if k == "district" and not v: continue
        r[idx[k]] = v.strip()
with open(OUT, "w", encoding="utf-8", newline="") as fh:
    csv.writer(fh, quoting=csv.QUOTE_MINIMAL).writerow(header)
    csv.writer(fh, quoting=csv.QUOTE_MINIMAL).writerows(body)
# report
sel = sys.argv[1:]  # optional slug subset
rs = [r for r in body if not sel or r[0] in sel]
print(f"rows: {len(rs)}")
for c in FILL:
    n = sum(1 for r in rs if r[idx[c]].strip())
    print(f"{c:18s} {n:3d}/{len(rs)}  {100*n/len(rs):5.1f}%")
