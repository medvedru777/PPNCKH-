## Experiment Design (Verified and Recorded)

### Verified
- Feature groups under study: **PE Header** and **API Import** (documented in project memory and used in implemented analysis).
- Baseline model run (implemented & verified): **XGBoost** — trained via `src/run_shap_analysis.py` on `data/raw/ember_1k_real.parquet` (see `docs/shap_summary.png` and metrics in progress log).

### Implemented (verified)
- XGBoost baseline training and evaluation (metrics verified: Accuracy 95.50%, Precision 97.89%, Recall 93.00%, F1 95.38%).
- SHAP analysis executed and summary plot generated (`docs/shap_summary.png`).

### Planned (recorded but not verified here)
- LightGBM baseline is listed in earlier memory files as an intended baseline; this has not been verified as executed in the repository.

