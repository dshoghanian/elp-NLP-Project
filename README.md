# EPL News (Internal)

Private repo for our group. Keep it simple.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run (example)
```bash
python src/guardian_pull.py --from 2024-08-01 --to 2024-08-31 --section football --out data/guardian
```


## Data storage
- Local path: `data/` (committed via `.gitkeep`, contents are gitignored).
- The pull script writes JSONL files here unless you pass a different `--out`.
- You can also point to cloud buckets later (e.g., GCS/S3) if needed.
