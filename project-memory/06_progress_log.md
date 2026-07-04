# Progress Log

## 2026-05-27

Completed:
- selected Topic 15
- understood seminar requirements
- understood research workflow
- created project structure (malware-ml-research)
- created research memory system

Pending:
- setup Python environment
- install packages
- download EMBER dataset

# Progress Log

## 2026-05-27

Completed:
- selected Topic 15
- understood seminar requirements
- understood research workflow
- created project structure
- created research memory system
- initialized Python virtual environment (.venv)

Pending:
- install required Python packages (LightGBM, Optuna, etc.)
- download & explore EMBER dataset

# Progress Log

## 2026-05-27

Completed:
- selected Topic 15
- understood seminar requirements
- created project structure
- created research memory system
- defined research questions
- defined methodology
- defined experiment design

Pending:
- setup Python environment
- install packages
- download EMBER dataset

## Dataset Acquisition

Completed:
- created ember dataset folder
- downloaded EMBER 2018 dataset
- extracted feature files

Notes:
- dataset contains feature vectors, not raw malware executables
- research will use only 1000 samples

## 2026-05-27 — Current State

### Environment
- Python virtual environment (.venv) created
- Project structure initialized (research-grade layout)

### Dataset
- EMBER 2018 dataset downloaded (.tar.bz2)
- Dataset NOT yet extracted

### Current Phase
Phase 2: Dataset acquisition & extraction

### Pending Tasks
- Move dataset into /data/raw
- Extract EMBER archive
- Locate JSONL feature files
- Verify dataset structure (label + feature)
- Load sample batch (1000 entries)

### Next Phase
Phase 3: Feature engineering + baseline model (LightGBM)

# Progress Log

## 2026-05-28 — Phase 3 Preparation

### Completed

* verified research topic scope
* finalized research direction (explainability over accuracy)
* completed project structure initialization
* initialized Python virtual environment (.venv)
* downloaded EMBER 2018 dataset
* extracted EMBER feature files
* created research memory system
* reviewed methodology requirements from seminar document
* identified baseline model strategy (LightGBM)
* identified explainability framework (SHAP)

### Current Phase

Phase 3 — Dataset Verification & Baseline Pipeline

### Immediate Tasks

* verify JSONL dataset structure
* install ML dependencies
* create dataset exploration notebook
* implement data loader
* sample 1000 balanced entries
* perform exploratory dataset analysis

### Research Focus

* feature interpretability
* malware vs benign feature contribution
* SHAP analysis
* false positive explanation
* PE header vs API import importance

### Methodological Constraints

* prioritize explainability over benchmark accuracy
* discuss threats to validity
* maintain reproducibility
* avoid purely engineering-oriented evaluation
* use statistically grounded analysis

### Planned Next Milestone

First successful baseline LightGBM training with SHAP-ready feature pipeline.


# 2026-05-29 — Entering Phase 3: Pipeline Construction

### Completed:
- Xác nhận lộ trình kỹ thuật cho Phase 3 [1].
- Xác định danh sách thư viện ML cần thiết (LightGBM, SHAP, LIEF) [3].
- Thống nhất mục tiêu: Ưu tiên tính khả diễn giải hơn là độ chính xác thuần túy [2, 12].

### Immediate Tasks:
- Chạy lệnh cài đặt `pip install` cho các gói ML [3].
- Kiểm tra tính toàn vẹn của các tệp JSONL trong `data/` [5].
- Khởi tạo notebook `01_dataset_exploration.ipynb` để phân tích đặc trưng tĩnh [6].

### Research Note:
- Cần tập trung vào việc so sánh mức độ đóng góp của PE Header và API Calls ngay từ khâu EDA [8, 9].
- Đảm bảo mọi bước xử lý dữ liệu đều phải có `seed` để giảng viên có thể tái lập trong 15 phút [11, 13].

Completed:
- Chọn Đề tài 15 & xác định câu hỏi nghiên cứu khoa học theo Edgar & Manz (2017).
- Khởi tạo cấu trúc thư mục chuẩn nghiên cứu (malware-ml-research).
- Khởi tạo môi trường ảo Python (.venv).
- Tải xuống và giải nén thành công bộ dữ liệu EMBER 2018 vào data/processed/.

Pending:
- Kích hoạt .venv và cài đặt các gói phụ thuộc (LightGBM, SHAP, LIEF, scikit-learn).
- Viết pipeline Data Loader trích xuất 1000 mẫu cân bằng (500 độc hại / 500 an toàn) từ file JSONL gốc.
- Khởi tạo notebook 01_dataset_exploration.ipynb để phân tích đặc trưng tĩnh (EDA).

# Progress Log

## 2026-05-30 — Phase 3 & 4: Progress notes

### Completed (recorded at the time)
- Jupyter Notebook configured with project `.venv`.
- Initial EDA workflows implemented (notebook created). 

### Notes
- Some earlier entries reference a completed LightGBM baseline; see verified updates for actual executed baseline below.

## 2026-06-16 — Verified experimental execution

### Implemented & Verified
- Canonical dataset prepared: `data/raw/ember_1k_real.parquet` (1000 samples, 500/500).
- Executed `src/run_shap_analysis.py` on `data/raw/ember_1k_real.parquet` to train an XGBoost baseline and compute SHAP values.
- Verified metrics from the run:
	- Accuracy: 95.50%
	- Precision: 97.89%
	- Recall: 93.00%
	- F1-score: 95.38%
	- Confusion Matrix: [[98, 2], [7, 93]]
	- SHAP summary plot saved at `docs/shap_summary.png`.

### Outstanding / Pending (recorded)
- Reconcile legacy dataset files (`ember_1k_balanced.parquet` at repo root) and ensure all training scripts reference the canonical dataset.
- Document EDA outputs and schema in `project-memory/04_dataset.md` after final review.