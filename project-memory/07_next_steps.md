<!-- # Next Steps

1. Install Python (nếu chưa có)
2. Create Python virtual environment (.venv)
3. Install required Python packages (scikit-learn, lightgbm, v.v.)
4. Download EMBER feature dataset
5. Create first notebook
6. Load 1000 samples to test

# Next Steps

1. Install Python packages (scikit-learn, lightgbm, pandas, matplotlib)
2. Install Jupyter extension trong VSCode để chạy file .ipynb
3. Download EMBER feature dataset (hoặc tạo script tải data)
4. Create first notebook và load thử 1000 samples

# Next Steps

1. Install Python
2. Create virtual environment
3. Install ML packages
4. Configure VSCode interpreter
5. Download EMBER feature dataset
6. Create first notebook
7. Load 1000 samples
8. Train baseline LightGBM
9. Generate SHAP plots

# Next Steps

1. Verify EMBER dataset structure
2. Create first notebook
3. Load JSONL feature files
4. Sample 1000 entries
5. Build dataframe
6. Train baseline LightGBM
7. Generate SHAP explanations

## Current Focus

1. Move EMBER dataset into data/raw/
2. Extract .tar.bz2 archive
3. Verify JSONL files exist
4. Load 1000 samples into DataFrame
5. Inspect feature-label structure
6. Prepare flattening pipeline -->

# Next Steps

## Current Research Phase

Phase 3 — Dataset Verification & Baseline Pipeline

---

# Immediate Objectives

The project setup phase is mostly completed.

Current goal:
transition from environment preparation into the first reproducible malware machine learning experiment.

The research prioritizes:

* explainability
* methodological rigor
* reproducibility
* scientific interpretation

NOT:

* leaderboard accuracy
* deep learning complexity
* excessive optimization

---

# Current Project State

## Completed

* selected Topic 15
* understood seminar methodology requirements
* created research-grade project structure
* initialized Python virtual environment (.venv)
* downloaded EMBER 2018 dataset
* extracted EMBER feature files
* created project memory system
* prepared research workflow

## Current Focus

* verify dataset integrity
* build reusable data loading pipeline
* perform dataset exploration
* prepare baseline LightGBM experiment
* integrate SHAP explainability

---

# Step-by-Step Execution Plan

## Step 1 — Verify EMBER Dataset Structure

Target location:

```text
data/processed/ember/ember2018/
```

Verify existence of:

* train_features_*.jsonl
* test_features.jsonl
* metadata files

Tasks:

* confirm JSONL format is readable
* inspect feature-label structure
* verify malware/benign labels exist

Goal:
Ensure dataset is valid before experimentation.

---

## Step 2 — Install Required Python Packages

Required packages:

* pandas
* numpy
* scikit-learn
* lightgbm
* shap
* matplotlib
* tqdm
* pyarrow

Optional:

* lief (PE parsing support)

Command:

```powershell
pip install pandas numpy scikit-learn lightgbm shap matplotlib tqdm pyarrow
```

Optional:

```powershell
pip install lief
```

Goal:
Prepare reproducible ML environment.

---

## Step 3 — Configure VSCode Environment

Tasks:

* install Jupyter extension
* select correct Python interpreter
* verify notebook execution works

Goal:
Ensure notebook-based experimentation workflow is operational.

---

## Step 4 — Create Dataset Exploration Notebook

Create:

```text
notebooks/01_dataset_exploration.ipynb
```

Tasks:

* load dataset samples
* inspect schema
* inspect feature groups
* inspect labels
* inspect sparsity
* inspect missing values

Goal:
Understand statistical properties of EMBER features before modeling.

---

## Step 5 — Implement Data Loader

Create:

```text
src/data_loader.py
```

Responsibilities:

* read JSONL files
* randomly sample ~1000 entries
* balance malware/benign classes
* flatten features
* convert into pandas dataframe

Goal:
Build reusable and reproducible dataset pipeline.

---

## Step 6 — Perform Initial Dataset Analysis

Required analyses:

* label distribution
* feature variance
* entropy behavior
* imported API frequency
* PE header statistics
* sparsity analysis

Expected outputs:

* histograms
* boxplots
* markdown statistical tables

Goal:
Produce scientifically meaningful observations before training.

---

## Step 7 — Train Baseline Model

Model:
LightGBM baseline classifier

Tasks:

* train/test split
* baseline training
* evaluate:

  * accuracy
  * precision
  * recall
  * F1-score
  * confusion matrix

Goal:
Create first interpretable malware classification baseline.

Important:
Model interpretability is more important than maximizing benchmark accuracy.

---

## Step 8 — Integrate SHAP Explainability

Tasks:

* compute SHAP values
* generate SHAP summary plots
* identify dominant features
* compare:

  * PE header features
  * imported API features
* analyze false positives
* analyze false negatives

Goal:
Understand WHY the model makes decisions.

---

## Step 9 — Begin Scientific Interpretation

Discussion topics:

* feature contribution interpretation
* adversarial reasoning
* label noise concerns
* dataset limitations
* threats to validity
* reproducibility constraints

Goal:
Transition from engineering workflow into scientific analysis.

---

# Planned Deliverables

Expected outputs:

* IEEE-style paper
* SHAP visualizations
* dataset analysis
* baseline experiment results
* reproducibility appendix
* validity discussion

---

# Immediate Next Milestone

Successfully:

* load ~1000 balanced EMBER samples
* train first LightGBM baseline
* generate initial SHAP explanations

# Next Steps

## Current Research Phase
Phase 5 — Mô hình hóa sâu và Tích hợp Tính khả diễn giải (SHAP)

---

# Immediate Objectives
Mục tiêu chuẩn bị dữ liệu và huấn luyện mô hình phân loại Baseline đã hoàn thành xuất sắc. 
Hệ thống cần dịch chuyển trọng tâm từ việc xây dựng pipeline kỹ thuật sang phân tích khoa học có hệ thống theo chuẩn mực USENIX Security và IEEE S&P.

---

# Current Project State

## Completed
* Đăng ký và xác định phạm vi Đề tài 15.
* Khởi tạo cấu trúc thư mục chuẩn nghiên cứu (`malware-ml-research`).
* Cấu hình Jupyter Extension và kích hoạt thành công môi trường ảo `.venv` (Python 3.14.3).
* Nạp tập dữ liệu 1000 mẫu cân bằng từ định dạng Parquet.
* Thực hiện bóc tách và phân tích phương sai của hai nhóm đặc trưng mục tiêu (PE Header và API Imports).
* Làm sạch dữ liệu số và huấn luyện thành công mô hình Baseline LightGBM (đạt cấu trúc ma trận nhầm lẫn 2x2 ổn định).

## Current Focus
* Phân tích và đánh giá các chỉ số đo lường học thuật thu được từ Baseline LightGBM.
* Khởi tạo tính toán giá trị SHAP (SHapley Additive exPlanations) trên mô hình đã huấn luyện.
* Trực quan hóa mức độ đóng góp và sự phân cực đặc trưng để giải mã logic của mô hình đối với các mẫu nhận diện nhầm (False Positives).

---

# Step-by-Step Execution Plan

## Step 1 — Đánh giá Thống kê Hiệu năng Baseline
* Phân tích lạnh lùng và khách quan các chỉ số Accuracy, Precision, Recall, F1-Score vừa thu được.
* Khoanh vùng số lượng mẫu bị nhận diện nhầm (FP) và bỏ sót (FN) từ ma trận nhầm lẫn để làm đối tượng nghiên cứu cho SHAP.

## Step 2 — Triển khai Thư viện Giải thích SHAP
* Tích hợp `shap.TreeExplainer` tương thích riêng với cấu trúc cây quyết định của LightGBM.
* Tính toán ma trận giá trị SHAP (SHAP values) trên tập dữ liệu kiểm thử độc lập (`X_test`).

## Step 3 — Tạo Biểu đồ Summary Plot (Định hướng IEEE)
* Xuất biểu đồ mật độ SHAP (SHAP Summary Plot) để hiển thị trực quan top 20 đặc trưng có tầm ảnh hưởng lớn nhất.
* Biện luận khoa học về hướng tác động (phân cực tích cực/tiêu cực) của giá trị đặc trưng đối với quyết định dán nhãn mã độc.

## Step 4 — Thực hiện Nghiên cứu Đối kháng trên Mẫu False Positive
* Lọc riêng các tệp tin an toàn bị nhận diện nhầm (False Positives).
* Sử dụng biểu đồ lực (SHAP Force Plot / Waterfall Plot) trên từng mẫu cụ thể này để chỉ ra trường cấu trúc nào (PE Header hay API Calls) đã đánh lừa thuật toán.

## Step 5 — Biên soạn Thảo luận và Các mối đe dọa đến Tính hợp lệ
* Đánh giá hiện tượng nhiễu nhãn (Label noise) từ dữ liệu gốc.
* Thảo luận về giới hạn thực nghiệm (1000 mẫu đại diện) đối với tính tổng quát hóa của nghiên cứu.

---

# Planned Next Milestone
Xuất bản thành công hệ thống đồ thị SHAP chứng minh cơ chế ra quyết định của thuật toán và hoàn thiện chương Phương pháp luận đánh giá trong bản thảo tiểu luận.