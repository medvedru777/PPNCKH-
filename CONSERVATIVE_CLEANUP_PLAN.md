# CONSERVATIVE CLEANUP PLAN

Read-only planning document only. No repository changes were made.

## Principles

1. Preserve all research evidence.
2. Preserve all notebooks.
3. Preserve project-memory.
4. Preserve processed datasets.
5. Preserve references.
6. Preserve reproducibility.
7. Only mark items as DELETE when they are clearly duplicate, stale, deprecated, or unused by the final paper.
8. Minimize repository movement.

## Canonical Assets

- Canonical dataset: [data/raw/ember_1k_real.parquet](data/raw/ember_1k_real.parquet)
- Canonical scripts: [src/run_shap_analysis.py](src/run_shap_analysis.py), [src/prepare_real_data.py](src/prepare_real_data.py)
- Canonical figures: [docs/shap_summary.png](docs/shap_summary.png), [figures/group_shap_contribution.png](figures/group_shap_contribution.png), [figures/false_positive_top_features.png](figures/false_positive_top_features.png)
- Canonical result files: [results/final_results.md](results/final_results.md), [results/feature_shap_summary.csv](results/feature_shap_summary.csv), [results/group_shap_contributions.csv](results/group_shap_contributions.csv), [results/false_positive_predictions.csv](results/false_positive_predictions.csv), [results/false_positive_shap_values.csv](results/false_positive_shap_values.csv), [results/false_positive_feature_importance.csv](results/false_positive_feature_importance.csv)

## Classification

### ACTIVE

Keep these in place because they are needed for the final paper, reproducibility, or research traceability.

| Path | Why ACTIVE |
|---|---|
| [paper/](paper/) | Final manuscript source and submission artifact. |
| [paper/final.tex](paper/final.tex) | Camera-ready paper source. |
| [README.md](README.md) | Primary project overview and run instructions. |
| [REPRODUCIBILITY.md](REPRODUCIBILITY.md) | Reproducibility guide for the final study. |
| [PROJECT_AUDIT.md](PROJECT_AUDIT.md) | Verified audit of the repository state. |
| [FINAL_SUBMISSION_SNAPSHOT.md](FINAL_SUBMISSION_SNAPSHOT.md) | Submission-state snapshot. |
| [README_UPDATE_VERIFICATION.md](README_UPDATE_VERIFICATION.md) | Verification of README consistency. |
| [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md) | Submission checklist. |
| [SUBMISSION_READINESS_AUDIT.md](SUBMISSION_READINESS_AUDIT.md) | Submission readiness audit. |
| [SUBMISSION_READINESS_REPORT.md](SUBMISSION_READINESS_REPORT.md) | Submission readiness report. |
| [requirements.txt](requirements.txt) | Environment specification needed to rerun the study. |
| [active_venv.md](active_venv.md) | Environment note that may help reproduction. |
| [.gitignore](.gitignore) | Standard repository control file; keep active. |
| [references/](references/) | Supporting literature and methodology notes. |
| [project-memory/](project-memory/) | High-value AI-assisted project memory and research history. |
| [notebooks/](notebooks/) | Research evidence and exploratory analysis notebooks. |
| [data/](data/) | Holds canonical data and processed research inputs. |
| [data/raw/](data/raw/) | Canonical raw-data area, including the verified dataset and source archive. |
| [data/raw/ember_1k_real.parquet](data/raw/ember_1k_real.parquet) | Canonical dataset used in the final paper. |
| [data/raw/ember_dataset_2018_2.tar.bz2](data/raw/ember_dataset_2018_2.tar.bz2) | Source archive preserved for provenance and reconstruction. |
| [data/processed/](data/processed/) | Processed research inputs retained for reproducibility and provenance. |
| [data/processed/ember/](data/processed/ember/) | Intermediate EMBER extraction tree kept as research evidence. |
| [data/processed/ember/ember2018/](data/processed/ember/ember2018/) | Unpacked EMBER feature files used to derive the canonical dataset. |
| [docs/](docs/) | Canonical paper-supporting plot output. |
| [docs/shap_summary.png](docs/shap_summary.png) | Main SHAP summary figure cited by the paper. |
| [figures/](figures/) | Paper figures and related retained visuals. |
| [figures/group_shap_contribution.png](figures/group_shap_contribution.png) | Canonical group-comparison figure. |
| [figures/false_positive_top_features.png](figures/false_positive_top_features.png) | Canonical false-positive analysis figure. |
| [results/](results/) | Precomputed analysis outputs cited by the paper. |
| [results/final_results.md](results/final_results.md) | Human-readable verified results summary. |
| [results/feature_shap_summary.csv](results/feature_shap_summary.csv) | Feature-level SHAP summary. |
| [results/group_shap_contributions.csv](results/group_shap_contributions.csv) | Group-level SHAP comparison artifact. |
| [results/false_positive_predictions.csv](results/false_positive_predictions.csv) | False-positive record list. |
| [results/false_positive_shap_values.csv](results/false_positive_shap_values.csv) | SHAP values for false positives. |
| [results/false_positive_feature_importance.csv](results/false_positive_feature_importance.csv) | False-positive feature importance ranking. |
| [src/run_shap_analysis.py](src/run_shap_analysis.py) | Main verified analysis pipeline. |
| [src/prepare_real_data.py](src/prepare_real_data.py) | Canonical dataset preparation script aligned with the final pipeline. |

### ARCHIVE

Keep these items, but separate them from the final submission core because they are historical, exploratory, or legacy support material.

| Path | Why ARCHIVE |
|---|---|
| [src/experiments/](src/experiments/) | Early experiment code replaced by the final pipeline. |
| [src/prepare_real_ember.py](src/prepare_real_ember.py) | Earlier dataset-preparation script with a stale output path. |
| [src/data_loader.py](src/data_loader.py) | Older utility module not used by the verified final pipeline. |
| [src/unpack_ember.py](src/unpack_ember.py) | One-off extraction utility, useful as provenance but not active. |
| [figures/feature_variance_boxplot.png](figures/feature_variance_boxplot.png) | Extra EDA figure not referenced by the paper. |
| [data/raw/benign/](data/raw/benign/) | Legacy staging area for source material. |
| [data/raw/malware/](data/raw/malware/) | Legacy staging area for source material. |
| [data/raw/unlabeled/](data/raw/unlabeled/) | Legacy staging area for source material. |
| [ember_1k_balanced.parquet](ember_1k_balanced.parquet) | Deprecated root-level dataset copy retained only as historical clutter until removed. |

### DELETE

Delete only items that are clearly duplicate or stale and do not affect the final paper.

| Path | Why DELETE |
|---|---|
| [.venv/](.venv/) | Local virtual environment artifact, not a research asset. |
| [ember_1k_balanced.parquet](ember_1k_balanced.parquet) | Duplicate stale dataset copy at the repository root. |
| [data/raw/ember_1k_balanced.parquet](data/raw/ember_1k_balanced.parquet) | Duplicate stale dataset copy in the raw-data area. |
| [data/processed/ember_1k_balanced.parquet](data/processed/ember_1k_balanced.parquet) | Duplicate stale dataset copy in the processed-data area. |

## Why This Is Conservative

- It preserves the memory files, notebooks, references, processed EMBER tree, and raw source archive.
- It keeps the canonical dataset, scripts, figures, and CSV outputs in place.
- It only deletes duplicated balanced parquet files and the local environment folder.
- It archives old scripts and exploratory artifacts without removing research evidence.

## Proposed Final Repository Structure

The preferred end state is mostly the current structure, with only lightweight archiving of legacy code and obvious duplicate cleanup.

```text
/
  paper/
  README.md
  REPRODUCIBILITY.md
  PROJECT_AUDIT.md
  FINAL_SUBMISSION_SNAPSHOT.md
  README_UPDATE_VERIFICATION.md
  SUBMISSION_CHECKLIST.md
  SUBMISSION_READINESS_AUDIT.md
  SUBMISSION_READINESS_REPORT.md
  references/
  requirements.txt
  active_venv.md
  project-memory/
  notebooks/
  data/
    raw/
      ember_1k_real.parquet
      ember_dataset_2018_2.tar.bz2
      benign/
      malware/
      unlabeled/
    processed/
      ember/
        ember2018/
  docs/
    shap_summary.png
  figures/
    group_shap_contribution.png
    false_positive_top_features.png
    feature_variance_boxplot.png  # retained as archive-only visual if not deleted later
  results/
    final_results.md
    feature_shap_summary.csv
    group_shap_contributions.csv
    false_positive_predictions.csv
    false_positive_shap_values.csv
    false_positive_feature_importance.csv
  src/
    run_shap_analysis.py
    prepare_real_data.py
    prepare_real_ember.py  # archive candidate
    data_loader.py         # archive candidate
    unpack_ember.py        # archive candidate
    experiments/           # archive candidate
  archive/
    src/
      experiments/
      prepare_real_ember.py
      data_loader.py
      unpack_ember.py
    figures/
      feature_variance_boxplot.png
```

## Exact File Moves Required

These are the only moves recommended in this conservative version.

- Move [src/experiments/](src/experiments/) to [archive/src/experiments/](archive/src/experiments/)
- Move [src/prepare_real_ember.py](src/prepare_real_ember.py) to [archive/src/prepare_real_ember.py](archive/src/prepare_real_ember.py)
- Move [src/data_loader.py](src/data_loader.py) to [archive/src/data_loader.py](archive/src/data_loader.py)
- Move [src/unpack_ember.py](src/unpack_ember.py) to [archive/src/unpack_ember.py](archive/src/unpack_ember.py)
- Move [figures/feature_variance_boxplot.png](figures/feature_variance_boxplot.png) to [archive/figures/feature_variance_boxplot.png](archive/figures/feature_variance_boxplot.png)

## Exact Deletions Required

- Delete [.venv/](.venv/)
- Delete [ember_1k_balanced.parquet](ember_1k_balanced.parquet)
- Delete [data/raw/ember_1k_balanced.parquet](data/raw/ember_1k_balanced.parquet)
- Delete [data/processed/ember_1k_balanced.parquet](data/processed/ember_1k_balanced.parquet)

## Final Recommendation

Do the minimum needed to reduce confusion:

1. Keep all research evidence.
2. Keep all notebooks and project-memory.
3. Keep references and processed EMBER assets.
4. Archive only legacy scripts and the one extra EDA figure.
5. Delete only obvious duplicate balanced parquet files and the local virtual environment.