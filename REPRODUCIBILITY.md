"# Reproducibility Appendix: Explainable Malware Detection Pipeline

This document provides the exact sequence of commands to reproduce the experimental results reported in the paper. The entire process, from environment setup to final result generation, is designed to be completed within 15 minutes.

## 1. Environment Setup
Ensure Python 3.10+ is installed. Execute the following commands in PowerShell:

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\\.venv\\Scripts\\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## 2. Experimental Execution
Run the following scripts in order to regenerate the dataset, train the model, and produce all analysis figures.

```powershell
# Step 1: Verify/Prepare the balanced dataset
# (Dataset ember_1k_real.parquet is provided in data/raw/)

# Step 2: Train the XGBoost Baseline and generate performance metrics
python src/experiments/train_parquet.py

# Step 3: Generate Feature Variance Plot (Figure 1)
python src/generate_variance_plot.py

# Step 4: Perform SHAP Analysis and generate Figures 2, 3, and 4
python src/run_shap_analysis.py
```

## 3. Verification of Outputs
After execution, the following artifacts will be generated:
- **Metrics:** Printed to console by `train_parquet.py`.
- **Figures:** Saved in the `figures/` directory:
  - `feature_variance_boxplot.png`
  - `shap_summary.png`
  - `group_shap_contribution.png`
  - `false_positive_top_features.png`

## 4. Hardware & Software Specifications
- **OS:** Windows 10/11 (PowerShell)
- **Python:** 3.10+
- **Key Libraries:** XGBoost 2.0.3, SHAP 0.45.1, Scikit-learn 1.4.2, Pandas 2.2.2"