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

## Data Sources

| Source | Description |
|--------|-------------|
| Premier League Press | Transfer articles from major outlets |
| Reddit | r/soccer and club subreddits |
| Transfermarkt | Net spend and squad values |
| Club Financials | Revenue and operating profit |
| Match Data | Points, wins, points per game |

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

## Network Outputs

- Club-to-Club Transfer Narrative Network
- Ego Graphs for Big Six and Key Outliers
- Press vs Reddit Centrality Comparison
- Influence Diffusion Visualizations

---

## Key Findings

- Strong positive relationship between press narrative centrality and club performance  
- Big Six dominate both the narrative and performance space  
- Narrative hype remains statistically significant even after controlling for spending  
- Presence of over-hyped under-performers and under-hyped over-performers  
- Narrative strength enhances both financial leverage and sporting outcomes  


