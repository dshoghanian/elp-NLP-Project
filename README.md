# EPL News (Internal)



## Clone the repo

Using **HTTPS**:
```bash
git clone https://github.com/<org-or-user>/<repo>.git
cd <repo>
```

Using **SSH** (requires a configured SSH key):
```bash
git clone git@github.com:<org-or-user>/<repo>.git
cd <repo>
```

Then set up your environment:
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
cp .env.example .env
pip install -r requirements.txt
```

To push your first commit (if starting from local):
```bash
git add .
git commit -m "init"
git push -u origin main
```

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
