# Final Results

## 1. Dataset

- Dataset chính thức: `data/raw/ember_1k_real.parquet`
- Số lượng mẫu: `1000`
- Phân bố nhãn:
  - `500` benign
  - `500` malware
- Nguồn dữ liệu:
  - Canonical dataset được xác thực trong repository và sử dụng bởi pipeline nghiên cứu.
  - Dữ liệu này được tạo/chuẩn hóa bằng `src/prepare_real_data.py` và lưu tại `data/raw/ember_1k_real.parquet`.
  - Tệp `ember_1k_balanced.parquet` ở thư mục gốc là tệp lỗi thời và không phải dataset chính thức.

## 2. Experimental Setup

- Mô hình sử dụng: `XGBoost` classifier
- Dataset sử dụng: `data/raw/ember_1k_real.parquet`
- Chia train/test:
  - `train_test_split` với `test_size=0.2`
  - `random_state=42`
  - `stratify=y`
- Công cụ explainability: `SHAP` TreeExplainer via `shap.summary_plot`
  - Đầu ra SHAP chính: `docs/shap_summary.png`

## 3. Model Performance

| Metric | Value |
|---|---|
| Accuracy | `95.50%` |
| Precision | `97.89%` |
| Recall | `93.00%` |
| F1-score | `95.38%` |

Confusion Matrix:

- `[[98, 2], [7, 93]]`

## 4. SHAP Analysis

- File `shap_summary.png` là biểu đồ SHAP summary được tạo bởi `src/run_shap_analysis.py`.
- Biểu đồ này phản ánh đóng góp SHAP của tất cả 5 feature trong dataset và cho thấy mức độ quan trọng tương đối của từng feature.
- Top features theo SHAP (theo mean absolute SHAP):
  1. `header_coff_timestamp`
  2. `header_optional_sizeof_code`
  3. `api_calls_count`
  4. `sections_count`
  5. `header_optional_sizeof_headers`

## 5. Feature Group Comparison

| Feature Group | Mean Absolute SHAP | Notes |
|---|---|---|
| PE Header | `6.620401` | Bao gồm `header_coff_timestamp`, `header_optional_sizeof_code`, `sections_count`, `header_optional_sizeof_headers` |
| API Import | `0.790368` | Bao gồm `api_calls_count` |

- Tỷ lệ đóng góp giữa hai nhóm:
  - PE Header / API Import ≈ `8.376`

## 6. False Positive Analysis

- Số lượng false positive: `2`
- Top feature gây false positive theo mean absolute SHAP:

| Rank | Feature | Contribution (mean abs SHAP) |
|---|---|---|
| 1 | `api_calls_count` | `1.290357` |
| 2 | `header_optional_sizeof_code` | `1.253238` |
| 3 | `header_coff_timestamp` | `0.610278` |
| 4 | `header_optional_sizeof_headers` | `0.200722` |
| 5 | `sections_count` | `0.139357` |

## 7. Figures Available

- `shap_summary.png`
- `group_shap_contribution.png`
- `false_positive_top_features.png`
- `feature_variance_boxplot.png`

## 8. Key Findings

- Dataset chính thức là `data/raw/ember_1k_real.parquet` với 1000 mẫu cân bằng 500/500.
- Pipeline xác thực sử dụng `src/run_shap_analysis.py` để huấn luyện XGBoost và tính SHAP.
- Mô hình đạt hiệu năng đã xác thực: Accuracy 95.50%, Precision 97.89%, Recall 93.00%, F1-score 95.38%.
- Confusion matrix đã xác thực: `[[98, 2], [7, 93]]`.
- Feature quan trọng nhất theo SHAP là `header_coff_timestamp`.
- Nhóm PE Header có tổng mean absolute SHAP lớn hơn nhóm API Import khoảng 8.38 lần.
- `api_calls_count` là yếu tố quan trọng nhất trong các false positive.
- Chỉ sử dụng dataset canonical; các file dataset cũ/stale như `ember_1k_balanced.parquet` không nằm trong kết quả chính.
- Biểu đồ SHAP chính thức được lưu tại `docs/shap_summary.png`.
- Repository hiện có 4 figure liên quan đến EDA và explainability.
