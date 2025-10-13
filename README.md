# EPL News (Internal)


### Research Questions
- **RQ1 – Rumor credibility:** Can we quantify the credibility of Premier League transfer rumors and coaching changes from news text in near-real time?
- **RQ2 – Impact on demand:** Do credible rumors or breaking news measurably shift **match-level demand proxies** (attendance where available, ticket resale activity if accessible, web attention) and **fan sentiment** in the short run?
- **RQ3 – Moderators:** How do club context (recent form, table position), player profile (market value, position), and news tone/stance moderate these effects?

### Potential Data Sources (and Why They Fit)
- **The Guardian Open Platform (news + metadata):** High editorial standards, rich football coverage, consistent structure (dates, sections, headlines), and API access—ideal for extracting tone, stance, and entities at the article level.
- **GDELT GKG (Global Knowledge Graph via BigQuery):** Massive, timestamped global news signal with sentiment/tone—useful for breadth, event timing, and cross-checking spikes beyond a single outlet.
- **FBref / Football-Data.org (fixtures, results, context):** Timeline backbone (who/when/where) to align news with pre/post windows.
- **Transfermarkt (transfer events & statuses):** Ground truth for whether a rumor was confirmed, associated fees, and dates—enables **rumor → outcome** evaluation.
- *(Optional, if available)* **Ticketing/resale or web attention (e.g., Google Trends):** Strengthens the “demand” side; attendance and engagement proxies still enable a reasonable first pass.

> Together these sources cover **text (news)**, **events (fixtures/transfers)**, and **outcomes (confirmation/demand)**—what we need to test credibility and impact.

### Planned Methods
- **Ingestion & cleaning:** API pulls (Guardian), SQL for GDELT; deduplication (URL/domain + text shingling), timezone normalization, article→club mapping.
- **NLP features:**
  - **NER** to tag players/clubs/competitions.
  - **Sentiment / tone** features (lexicon + model-based).
  - **Stance & hedging cues** (e.g., “close to,” “monitoring,” “agreed terms”) to score rumor credibility.
  - **Topic tags** (transfer/contract/injury/managerial).
- **Labeling & joins:** Link articles to fixtures (±k days); link rumors to outcomes via Transfermarkt.
- **Analysis & modeling:**
  - **Classification:** Predict rumor confirmation (logistic regression / tree-based).
  - **Event-study style comparisons:** Pre/post news windows on demand proxies.
  - **Controls/robustness:** Club and season fixed effects; recent form; opponent strength.
- **Evaluation:** Precision/recall for confirmation predictions; effect sizes and confidence intervals for demand shifts.

### Who Will Benefit—and How
- **Clubs & analysts:** Earlier, data-driven read on which rumors are likely real → better scouting focus and communications planning.
- **Media & platforms:** Credibility scoring helps curate high-quality stories and reduce noise, improving audience trust.
- **Fans & communities:** Clearer context around news spikes reduces misinformation and hype fatigue.
- **Researchers & students:** Reusable pipeline for linking text to events and demand analysis—portable beyond football.

> **Limitations & ethics:** Respect source ToS; avoid disallowed scraping; no sharing of proprietary data; credibility scores are probabilistic and reported with uncertainty.

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
