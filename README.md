# Premier League Transfer Narrative Analysis (NLP + Network Science)

This project applies Natural Language Processing (NLP) and Network Analytics to study how media and fan transfer narratives relate to club performance and financial spending in the English Premier League (EPL) from 2016–2025.

The project integrates:
- Press transfer coverage  
- Reddit fan discussions  
- Club financials  
- On-pitch performance  
- Network centrality metrics  

to quantify how narrative attention ("hype") interacts with real-world success.

---

## Research Question

Do clubs that dominate transfer narratives also dominate on the pitch and financially—and does narrative hype independently matter beyond money?

---

## Core Methods

- Natural Language Processing (spaCy, TF-IDF, Named Entity Recognition)
- Network graph construction (NetworkX)
- Centrality metrics (PageRank, Eigenvector, Degree)
- Regression modeling and correlation analysis
- Temporal panel data (2016–2025)
- Ego network analysis
- Quadrant risk-return analysis

---

## Data Files

All cleaned and analysis-ready datasets are located in the `data/` directory.

| File | Description |
|------|-------------|
| `club_analysis_panel_2016_2022.csv` | Master regression panel with performance, finance, and narrative variables |
| `club_network_centrality_2016_2022.csv` | Club-level centrality metrics from the press narrative network |
| `club_risk_return_panel_2019_2025.csv` | Risk-return quadrant dataset for narrative vs performance analysis |
| `club_yearly_press_reddit_centrality.csv` | Yearly press vs Reddit centrality comparison |
| `press_footy_centrality.parquet` | High-resolution press network centrality metrics |

---

## Pipeline Overview

Raw Text (Press + Reddit)  
→ Entity Extraction (spaCy NER)  
→ Club Mention Networks  
→ Network Centrality Metrics  
→ Merge With:
- Net Spend  
- Revenue  
- Points per Game (PPG)  
→ Statistical Modeling and Visualization  

---

## Notebook Files

All analysis is fully reproducible using the notebooks in the `notebook/` directory.

| Notebook | Purpose |
|----------|---------|
| `network_analysis.ipynb` | Constructs the press narrative network and computes centrality metrics |
| `press_ego_network_search.ipynb` | Interactive ego network exploration for individual clubs |
| `Final_analysis.ipynb` | Full regression modeling, quadrant analysis, and results visualization |

---

## Key Findings

- Strong positive relationship between press narrative centrality and club performance  
- Big Six dominate both the narrative and performance space  
- Narrative hype remains statistically significant even after controlling for spending  
- Presence of over-hyped under-performers and under-hyped over-performers  
- Narrative strength enhances both financial leverage and sporting outcomes  

---

## Project Structure
premier-league-nlp/
│
├── data/
│ ├── club_analysis_panel_2016_2022.csv
│ ├── club_network_centrality_2016_2022.csv
│ ├── club_risk_return_panel_2019_2025.csv
│ ├── club_yearly_press_reddit_centrality.csv
│ └── press_footy_centrality.parquet
│
├── notebook/
│ ├── network_analysis.ipynb
│ ├── press_ego_network_search.ipynb
│ └── Final_analysis.ipynb
│
└── README.md
