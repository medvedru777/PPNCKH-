## Verified Issues and Observations

- Stale dataset file present at repository root: `ember_1k_balanced.parquet` contains 500 rows and only label=0. This file is not the canonical balanced dataset and caused confusion when used by some scripts.

- `src/experiments/train_parquet.py` reads `data/raw/ember_1k_balanced.parquet` and fails because that parquet contains only benign samples (verified run produced an error message about single-label data).

- Model choice discrepancy: project memory documents LightGBM as baseline intent, but executed baseline runs in repository use XGBoost (`src/run_shap_analysis.py` and `src/experiments/train_parquet.py` use XGBoost). This is a documented inconsistency (verified by inspecting source and running scripts).

- File path inconsistencies: SHAP plot saved to `docs/shap_summary.png` while some documentation references `figures/shap_summary.png` (verified by file system and workflow history mismatch).

## Notes
- No fixes were applied in this update; the above items are recorded as verified issues to be addressed separately.

