# Explainable Malware Detection via XGBoost and SHAP Analysis

**Research Title (Vietnamese):** Khảo sát Định lượng: Khả năng Diễn giải Đặc trưng trong Học máy Phân tích Mã độc

## Project Overview

This project investigates **explainability in machine learning models** for malware detection, using SHAP (SHapley Additive exPlanations) to interpret model decisions on misclassified benign files (false positives). The study analyzes feature importance across PE Header and API Import feature groups on a balanced, verified dataset of 1,000 samples.

### Key Results
- **Model Accuracy:** 95.50% (Precision: 97.89%, Recall: 93.00%, F1-score: 95.38%)
- **Dataset:** 1,000 balanced samples (500 benign, 500 malware) from EMBER
- **Feature Importance:** PE Header features contribute ~8.4× more than API Import features
- **False Positive Analysis:** 2 false positives driven by interpretable feature patterns
- **Reproducibility:** Fixed random seed (42), stratified splitting, verified dataset hash

## Quick Start (Setup & Run)

### Prerequisites
- Python 3.8+
- pip or conda

### Installation & Running

```bash
# 1. Activate virtual environment
.venv\Scripts\activate          # Windows
# OR
source .venv/bin/activate       # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the main pipeline
python src/run_shap_analysis.py

# 4. View results
# - Console output: Accuracy, F1-Score
# - Figure: docs/shap_summary.png
```

**For detailed reproducibility guide, see [REPRODUCIBILITY.md](REPRODUCIBILITY.md)**

## Research Questions

**RQ1:** Which feature group contributes more strongly to malware classification: PE Header features or API Import features?  
# Phát hiện mã độc có khả năng giải thích thông qua XGBoost và phân tích SHAP trên tập dữ liệu EMBER

## 📌 Giới thiệu
Dự án này tập trung vào việc xây dựng một hệ thống phát hiện mã độc sử dụng các đặc trưng tĩnh (static features) từ metadata của tệp PE. Mục tiêu chính không chỉ là đạt được độ chính xác cao mà còn là **khả năng giải thích (Explainability)** — hiểu rõ tại sao mô hình lại phân loại một tệp là mã độc hoặc an toàn.

Chúng tôi sử dụng bộ phân loại **XGBoost** kết hợp với phương pháp **SHAP (SHapley Additive exPlanations)** để bóc tách tầm quan trọng của từng đặc trưng, từ đó cung cấp cái nhìn minh bạch về logic ra quyết định của mô hình.

## 🛠️ Phương pháp luận
- **Tập dữ liệu**: Sử dụng tập dữ liệu EMBER (phiên bản rút gọn 1,000 mẫu, cân bằng 50/50).
- **Đặc trưng**: Tập trung vào 5 đặc trưng then chốt từ PE Header và số lượng API Import.
- **Mô hình**: XGBoost (Extreme Gradient Boosting).
- **Giải thích**: SHAP TreeExplainer để phân tích đóng góp toàn cục và cục bộ.

## 📂 Cấu trúc thư mục
- `src/`: Chứa toàn bộ mã nguồn Python.
    - `experiments/`: Các script huấn luyện và tiền xử lý dữ liệu.
    - `run_shap_analysis.py`: Script chính để thực hiện phân tích SHAP.
    - `generate_variance_plot.py`: Tạo biểu đồ phương sai đặc trưng.
- `figures/`: Chứa các biểu đồ kết quả (Confusion Matrix, SHAP Summary, v.v.).
- `paper/`: Chứa bản thảo bài báo nghiên cứu (định dạng LaTeX).
- `data/`: Chứa tập dữ liệu chuẩn `.parquet`.
- `docs/`: Các tài liệu tham khảo và hướng dẫn.

## 🚀 Hướng dẫn tái lập (Reproducibility)
Để tái lập kết quả của nghiên cứu, vui lòng thực hiện các bước sau:

1. **Cài đặt môi trường**:

**RQ2:** How do SHAP value distributions explain false positive predictions?  
**Answer:** Two false positives are driven primarily by `api_calls_count` and `header_optional_sizeof_code`, demonstrating that SHAP can meaningfully explain misclassifications.

**RQ3:** How can explainability be supported through a verified and reproducible malware detection pipeline?  
**Answer:** Using canonical dataset (SHA256 verified), fixed random seed, stratified splitting, and documented code provides a fully reproducible pipeline.

## Submission Artifacts

| File | Purpose |
|------|---------|
| `paper/final.tex` | IEEE-format research paper (camera-ready) |
| `results/final_results.md` | Experimental results summary |
| `REPRODUCIBILITY.md` | Detailed reproducibility guide |
| `src/run_shap_analysis.py` | Main experiment pipeline |
| `figures/` | SHAP and analysis plots |
| `project-memory/` | Research methodology documentation |

## Background (Motivation)

This work investigates explainability in malware detection models, focusing on interpretability rather than accuracy alone. The research quantitatively evaluates SHAP feature attribution to decode model decision logic for benign files misclassified as malware (false positives).

### Research Context

Vietनamese Project Title: Khảo sát Định lượng: Khả năng Diễn giải Đặc trưng trong Học máy Phân tích Mã độc

**Topic Code:** T15  
**Methodology:** Machine Learning Applications (Reference: Edgar & Manz, Chapter 6)  
**Experiment Scope:** 1,000 PE executables (500 malware, 500 benign) optimized for local memory constraints.

### Introduction
This work combines validated dataset, rigorous experimental design, and SHAP explainability analysis to provide transparent, reproducible malware detection with interpretable results.

## Research Questions & Answers

**RQ1:** How do PE Header features compare to API Import features in malware classification importance?  
**Answer:** PE Header features contribute approximately 8.4× more than API Import features (mean absolute SHAP: 1.6551 vs 0.7904 per feature).

**RQ2:** How do SHAP distributions explain false positive predictions?  
**Answer:** Two false positives are driven primarily by `api_calls_count` and `header_optional_sizeof_code`, demonstrating SHAP's ability to explain misclassifications.

## Experimental Timeline (Completed)

- [x] **Setup Phase:** Environment configuration, repository structure, PE file format understanding, EMBER dataset preparation
- [x] **Model Training:** Static feature extraction via `LIEF`, XGBoost baseline training with stratified split (seed 42)
- [x] **SHAP Analysis:** TreeExplainer integration, feature group impact quantification, SHAP value computation
- [x] **Reporting:** Results synthesis with malware analysis knowledge, model behavior explanation, IEEE-format paper writing

## Experimental Results & Evaluation

All tables and figures follow rigorous scientific reporting standards (no pie charts).

### Feature Set (Extracted Features)
| Feature Group | Count | Description |
| :--- | :--- | :--- |
| **PE Header** | 4 | `header_coff_timestamp`, `header_optional_sizeof_code`, `header_optional_sizeof_headers`, `sections_count` |
| **API Imports** | 1 | `api_calls_count` (total function imports from DLLs) |
| **Total** | 5 | Static features from PE metadata |

### Baseline Model Performance (Verified Results)
| Model | Accuracy | Precision | Recall | F1-Score | False Positive Count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **XGBoost** | 95.50% | 97.89% | 93.00% | 95.38% | 2 out of 100 test samples |

**Test Set Composition:** 200 samples (100 benign, 100 malware) from stratified 80/20 split with seed=42

## Reproducibility Instructions

To reproduce the full experiment:

```bash
# 1. Clone repository
git clone https://github.com/medvedru777/PPNCKH.git
cd PPNCKH

# 2. Set up virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Run the main analysis pipeline (requires canonical dataset at data/raw/ember_1k_real.parquet)
python src/run_shap_analysis.py

# Expected output:
# - Console: Accuracy 95.50%, F1-Score 95.38%
# - File: docs/shap_summary.png
```

**Required:** Dataset file `data/raw/ember_1k_real.parquet` (SHA256: D2FA243475A6AB613F2AF0CF4008180E838F9958FFA3EB688A2747041C4B58C9)