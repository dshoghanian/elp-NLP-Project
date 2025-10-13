# EPL News (Internal)

Describe your research question(s): 
Describe the potential data sources:
Why the data is suitable for answering your question:
What methods you plan to use:
Who will benefit from your research:
How?

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

## Repository structure (what everything is)

```
.
├─ src/                    # Project code
│  └─ guardian_pull.py    # Script to fetch Guardian articles
├─ docs/                   # Project docs (your uploaded files live here)
├─ data/                   # Local data storage (ignored by git)
│  └─ .gitkeep             # Placeholder so folder exists in repo
├─ .github/workflows/      # CI configuration
│  └─ ci.yml               # Minimal CI check
├─ .env.example            # Example env vars (copy to .env; never commit secrets)
├─ requirements.txt        # Python dependencies
├─ .gitignore              # Ignore rules (data, env, caches, etc.)
└─ README.md               # This guide
```

### Key files explained
- **src/guardian_pull.py** — Simple CLI to pull Guardian articles.

  **Args:**

  - `--from` (`YYYY-MM-DD`): start date

  - `--to` (`YYYY-MM-DD`): end date

  - `--section` (default `football`): Guardian section

  - `--out` (default `data/guardian`): output folder

  **Env:** `GUARDIAN_API_KEY` must be set in `.env`.

  **Output:** JSONL files in the `--out` directory.

- **docs/** — Place design notes, meeting notes, and shared write-ups here.

- **data/** — Local cache for raw files; kept out of git. Change with `DATA_DIR` in `.env` if you like.

- **.env.example** — Template for environment variables; copy to `.env` and fill in values.

- **requirements.txt** — Minimal deps (`requests`, `python-dotenv`). Add more as needed.

- **.github/workflows/ci.yml** — Tiny CI that installs deps and runs a quick check.

- **.gitignore** — Prevents committing large/binary data and secrets by default.


### Typical workflow
1. Clone → create & activate venv → `cp .env.example .env` → set `GUARDIAN_API_KEY`.

2. Run a small pull:

   ```bash
   python src/guardian_pull.py --from 2024-08-01 --to 2024-08-07 --section football --out data/guardian
   ```

3. Commit code/doc changes in small PRs.
