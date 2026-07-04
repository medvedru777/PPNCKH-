"# HỒ SƠ CHI TIẾT DỰ ÁN: PHÁT HIỆN MÃ ĐỘC CÓ KHẢ NĂNG GIẢI THÍCH

## 📘 Tổng quan dự án
Nghiên cứu này tập trung vào việc khảo sát khả năng giải thích của các mô hình học máy trong bài toán phát hiện mã độc. Bằng cách sử dụng phương pháp SHAP (SHapley Additive exPlanations), nghiên cứu phân tích các quyết định của mô hình đối với các tệp an toàn bị phân loại nhầm là mã độc (Dương tính giả). Nghiên cứu thực hiện đánh giá định lượng tầm quan trọng của các nhóm đặc trưng PE Header và API Import trên tập dữ liệu chuẩn hóa gồm 1,000 mẫu.

## 📈 Kết quả then chốt
- **Độ chính xác của mô hình**: 95,50% (Precision: 97,89%, Recall: 93,00%, F1-score: 95,38%)
- **Tập dữ liệu**: 1,000 mẫu cân bằng (500 mẫu an toàn, 500 mẫu mã độc) từ tập dữ liệu EMBER.
- **Tầm quan trọng đặc trưng**: Các đặc trưng thuộc nhóm PE Header đóng góp vào quyết định phân loại mạnh hơn khoảng 8,4 lần so với nhóm đặc trưng API Import.
- **Phân tích Dương tính giả**: Phát hiện 2 trường hợp dương tính giả được thúc đẩy bởi các mô hình đặc trưng có thể giải thích được.
- **Tính tái lập**: Sử dụng seed ngẫu nhiên cố định (42), chia tách dữ liệu phân tầng và xác minh hash của tập dữ liệu.

## 🚀 Hướng dẫn khởi động nhanh
### Yêu cầu hệ thống
- Python 3.8+
- pip hoặc conda

### Cài đặt và vận hành
1. **Kích hoạt môi trường ảo**:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
2. **Cài đặt thư viện phụ thuộc**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Chạy pipeline chính**:
   ```bash
   python src/run_shap_analysis.py
   ```
4. **Xem kết quả**:
   - Kết quả Accuracy, F1-Score hiển thị tại Console.
   - Biểu đồ trực quan tại: `docs/shap_summary.png`

*(Chi tiết xem tại file REPRODUCIBILITY.md)*

## ❓ Câu hỏi nghiên cứu và Trả lời
- **RQ1: Nhóm đặc trưng nào đóng góp mạnh hơn vào việc phân loại mã độc: PE Header hay API Import?**
  - *Trả lời*: Nhóm đặc trưng PE Header đóng góp mạnh hơn đáng kể (giá trị SHAP tuyệt đối trung bình: 1,6551 so với 0,7904 của API Import).
- **RQ2: Sự phân phối giá trị SHAP giải thích như thế nào về các dự đoán dương tính giả?**
  - *Trả lời*: Hai trường hợp dương tính giả bị chi phối chủ yếu bởi `api_calls_count` và `header_optional_sizeof_code`, chứng minh rằng SHAP có thể giải thích một cách có ý nghĩa các sai sót của mô hình.
- **RQ3: Khả năng giải thích có thể được hỗ trợ như thế nào thông qua một pipeline phát hiện mã độc được xác minh và có thể tái lập?**
  - *Trả lời*: Bằng cách sử dụng tập dữ liệu chuẩn (xác minh SHA256), cố định seed ngẫu nhiên, chia tách phân tầng và tài liệu hóa mã nguồn chi tiết.

## 📦 Danh mục sản phẩm bàn giao
| Tệp tin | Mục đích |
| :--- | :--- |
| `paper/final_vietnamese_perfected.tex` | Bài báo nghiên cứu định dạng IEEE (Bản tiếng Việt chuẩn) |
| `results/final_results.md` | Tóm tắt kết quả thực nghiệm |
| `REPRODUCIBILITY.md` | Hướng dẫn chi tiết về tính tái lập |
| `src/run_shap_analysis.py` | Pipeline thực nghiệm chính |
| `figures/` | Các biểu đồ phân tích SHAP và hiệu suất |
| `project-memory/` | Tài liệu về phương pháp luận nghiên cứu |

## 💡 Động lực và Bối cảnh
Nghiên cứu này tập trung vào tính minh bạch của mô hình hơn là chỉ chạy đua theo độ chính xác. Mục tiêu là giải mã logic ra quyết định của mô hình đối với các tệp an toàn bị phân loại nhầm, từ đó cải thiện độ tin cậy của hệ thống phát hiện mã độc.

### Bối cảnh nghiên cứu
- **Tên dự án**: Khảo sát Định lượng: Khả năng Diễn giải Đặc trưng trong Học máy Phân tích Mã độc
- **Mã đề tài**: T15
- **Phương pháp luận**: Ứng dụng Học máy (Tham chiếu: Edgar & Manz, Chương 6)
- **Phạm vi thực nghiệm**: 1,000 tệp thực thi PE (500 mã độc, 500 an toàn).

## 📅 Lộ trình thực hiện (Đã hoàn thành)
1. **Giai đoạn Thiết lập**: Cấu hình môi trường, xây dựng cấu trúc repo, nghiên cứu định dạng tệp PE, chuẩn bị dữ liệu EMBER.
2. **Huấn luyện Mô hình**: Trích xuất đặc trưng tĩnh qua LIEF, huấn luyện baseline XGBoost với chia tách phân tầng (seed 42).
3. **Phân tích SHAP**: Tích hợp TreeExplainer, định lượng tác động của nhóm đặc trưng, tính toán giá trị SHAP.
4. **Báo cáo**: Tổng hợp kết quả, giải thích hành vi mô hình, viết bài báo định dạng IEEE.

## 📊 Kết quả và Đánh giá thực nghiệm
### Tập đặc trưng (Extracted Features)
- **Nhóm PE Header (4 đặc trưng)**: `header_coff_timestamp`, `header_optional_sizeof_code`, `header_optional_sizeof_headers`, `sections_count`.
- **Nhóm API Imports (1 đặc trưng)**: `api_calls_count` (Tổng số hàm import từ các DLL).

### Hiệu suất mô hình cơ sở (Kết quả xác minh)
- **Accuracy**: 95,50%
- **Precision**: 97,89%
- **Recall**: 93,00%
- **F1-Score**: 95,38%
- **Số ca Dương tính giả**: 2 trên 100 mẫu kiểm tra.

**Cấu trúc tập kiểm tra**: 200 mẫu (100 an toàn, 100 mã độc) từ chia tách 80/20 với seed=42.
"