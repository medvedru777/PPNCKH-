"# Phát hiện mã độc có khả năng giải thích thông qua XGBoost và phân tích SHAP trên tập dữ liệu EMBER

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
   ```bash
   pip install -r requirements.txt
   ```
2. **Chuẩn bị dữ liệu**:
   Đảm bảo tệp `ember_1k_balanced.parquet` nằm trong thư mục `data/`.
3. **Chạy phân tích SHAP**:
   ```bash
   python src/run_shap_analysis.py
   ```
4. **Kiểm tra kết quả**:
   Các biểu đồ sẽ được tự động lưu vào thư mục `figures/` và kết quả chi tiết nằm trong `results/`.

## 📊 Kết quả đạt được
- **Độ chính xác (Accuracy)**: 95.50%.
- **Phân tích SHAP**: Nhóm đặc trưng **PE Header** có đóng góp vào quyết định phân loại mạnh hơn gấp **8.4 lần** so với số lượng API Import.
- **Phân tích Dương tính giả**: Phát hiện hiện tượng mô phỏng cấu trúc (structural mimicry) giữa phần mềm an toàn và mã độc.

## 📝 Tác giả
- **Học viên**: medvedru777
- **Môn học**: Seminar Phương pháp Nghiên cứu An toàn Thông tin"