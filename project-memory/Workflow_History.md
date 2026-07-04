Set-Content -Path "project-memory\Workflow_History.md" -Value @"
# Nhật ký Nghiên Cứu (Project Memory) — Đề tài T15

## Giai đoạn 1: Khảo sát công cụ LIEF và Dữ liệu thô
* **Mục tiêu:** Trích xuất đặc trưng tĩnh từ các tệp PE thô sử dụng thư viện `lief`.
* **Vấn đề gặp phải (đã ghi):** Khó khăn trong việc thu thập và xử lý đủ lượng tệp PE thô để xây pipeline trích xuất.

## Giai đoạn 2: Chuyển hướng sang EMBER (parquet)
* **Mục tiêu:** Dùng định dạng Parquet / EMBER feature vectors để tăng tốc xử lý và tránh thiếu hụt raw PE.
* **Vấn đề đã xác thực:** Một file parquet cũ xuất hiện tại repository root (`ember_1k_balanced.parquet`) chứa chỉ nhãn 0, gây ra lỗi khi một số script sử dụng file này.

## Giai đoạn 3: Pipeline hiện tại và thực thi (Verified)
* **Scripts chủ đạo đã thực thi:** `src/prepare_real_data.py`, `src/run_shap_analysis.py`.
* **Dữ liệu đầu vào đã chuẩn hóa (verified):** `data/raw/ember_1k_real.parquet` — 1000 mẫu (500 benign, 500 malware).
* **Thực thi:** Đã chạy `src/run_shap_analysis.py` trên `data/raw/ember_1k_real.parquet`, huấn luyện XGBoost và tính SHAP.
* **Kết quả thực nghiệm được xác thực:**
  - Accuracy: 95.50%
  - Precision: 97.89%
  - Recall: 93.00%
  - F1-score: 95.38%
  - Confusion Matrix: [[98, 2], [7, 93]]
* **SHAP:** `docs/shap_summary.png` was produced by the run (verified file present).

## Ghi chú và vấn đề còn tồn tại (verified)
* `src/experiments/train_parquet.py` attempts to read `data/raw/ember_1k_balanced.parquet` (which is not the verified canonical dataset) and therefore fails; this mismatch is a verified source of error.
* Documentation sometimes references `figures/` for SHAP output while actual output was saved to `docs/` — a verified path inconsistency.

"@