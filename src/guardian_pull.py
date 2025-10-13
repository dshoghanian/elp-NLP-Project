import os, argparse, pathlib, json, time
from urllib.parse import urlencode
import requests
from dotenv import load_dotenv

BASE = "https://content.guardianapis.com/search"

def main():
    load_dotenv()
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="date_from", required=True)
    ap.add_argument("--to", dest="date_to", required=True)
    ap.add_argument("--section", default="football")
    ap.add_argument("--out", default="data/guardian")
    args = ap.parse_args()

    api_key = os.getenv("GUARDIAN_API_KEY")
    assert api_key, "Missing GUARDIAN_API_KEY"

    out_dir = pathlib.Path(args.out); out_dir.mkdir(parents=True, exist_ok=True)
    page = 1
    while True:
        qs = {
            "section": args.section,
            "from-date": args.date_from,
            "to-date": args.date_to,
            "page-size": 200,
            "page": page,
            "api-key": api_key,
        }
        url = f"{BASE}?{urlencode(qs)}"
        r = requests.get(url, timeout=30); r.raise_for_status()
        payload = r.json(); resp = payload.get("response", {})
        results = resp.get("results", [])
        if not results: break
        out_file = out_dir / f"{args.date_from}_{args.date_to}_{page:04d}.jsonl"
        with out_file.open("a", encoding="utf-8") as f:
            for row in results: f.write(json.dumps(row, ensure_ascii=False) + "\n")
        page += 1; time.sleep(1.05)
        if not resp.get("pages") or page > resp["pages"]: break

if __name__ == "__main__":
    main()