# BÁO CÁO CHI TIẾT TIỂU LUẬN PHƯƠNG PHÁP NGHIÊN CỨU KHOA HỌC

**Đề tài:** Khảo sát Định lượng: Khả năng Diễn giải Đặc trưng trong Học máy Phân tích Mã độc  
**Học viên thực hiện:** Đoàn Quang Phúc  
**Học phần:** Phương pháp Nghiên cứu Khoa học trong ATTT  

---

## PHẦN 1: GIỚI THIỆU VÀ ĐẶT VẤN ĐỀ

### 1.1. Lý do chọn đề tài và tính cấp thiết
Trong kỷ nguyên của chiến tranh mạng, mã độc không còn đơn thuần là những đoạn mã gây hỏng dữ liệu mà đã tiến hóa thành những hệ thống phức tạp (Advanced Persistent Threats - APTs). Để đối phó, các hệ thống phát hiện mã độc dựa trên Học máy (Machine Learning - ML) đã được triển khai rộng rãi nhờ khả năng tự động hóa và xử lý dữ liệu lớn. Tuy nhiên, một rào cản chí mạng hiện nay là tính "hộp đen" (Black-box) của các mô hình hiện đại.

Khi một mô hình báo cáo một tệp là "mã độc" với độ chính xác cao, nhưng không thể giải thích **tại sao**, chuyên gia an ninh mạng sẽ đối mặt với hai rủi ro:
1. **Sự tin tưởng mù quáng:** Chấp nhận kết quả mà không biết mô hình đang dựa vào những đặc trưng rác (noise) thay vì đặc trưng thực sự của mã độc.
2. **Khó khăn trong ứng phó:** Không thể xác định được kẻ tấn công đang sử dụng kỹ thuật gì để lừa mô hình, dẫn đến việc không thể cập nhật luật phòng thủ.

Vì vậy, tôi chọn đề tài này để ứng dụng phương pháp SHAP, nhằm bóc tách cơ chế ra quyết định của mô hình, chuyển đổi từ việc đo lường hiệu suất thuần túy sang việc hiểu sâu về bản chất của sự phân loại.

### 1.2. Mục tiêu nghiên cứu chi tiết
*   **Xây dựng Baseline ổn định:** Thiết lập một mô hình phân loại mã độc dựa trên đặc trưng tĩnh của tệp PE với độ ổn định cao và khả năng tái lập tuyệt đối.
*   **Định lượng hóa tầm quan trọng:** Sử dụng giá trị Shapley để đo lường chính xác mức độ đóng góp của từng đặc trưng, từ đó so sánh sức mạnh giữa nhóm PE Header và API Import.
*   **Giải mã quy luật thất bại:** Phân tích sâu các trường hợp False Positives để tìm ra hiện tượng "mô phỏng cấu trúc" (Structural Mimicry).
*   **Chuẩn hóa quy trình khoa học:** Xây dựng một pipeline thực nghiệm minh bạch, đáp ứng đầy đủ các yêu cầu về tính hợp lệ (Validity) trong nghiên cứu khoa học.

### 1.3. Câu hỏi nghiên cứu (Research Questions)
*   **RQ1:** Trong không gian đặc trưng tĩnh, đặc trưng cấu trúc (PE Header) hay đặc trưng hành vi (API Import) đóng vai trò quyết định hơn trong phân loại?
*   **RQ2:** Hiện tượng "mô phỏng cấu trúc" ảnh hưởng thế nào đến tỷ lệ False Positives và làm thế nào để định lượng sự ảnh hưởng này thông qua SHAP?
*   **RQ3:** Làm thế nào để thiết lập một quy trình thực nghiệm đảm bảo tính khách quan, không bị thiên kiến và có thể tái lập tuyệt đối bởi bên thứ ba?

---

## PHẦN 2: CƠ SỞ LÝ THUYẾT VÀ PHƯƠNG PHÁP LUẬN

### 2.1. Ánh xạ chi tiết với Phương pháp luận (Mapping to Chapter 6)
Toàn bộ dự án này được dẫn dắt bởi khung **Machine Learning Research** trong Chương 6 của sách *Research Methods for Cyber Security*. Thay vì tiếp cận theo lối lập trình thuần túy, tôi áp dụng tư duy nghiên cứu khoa học:

*   **Phân loại bài toán:** Nghiên cứu được xác định là **Supervised Learning** (Học có giám sát) áp dụng cho bài toán **Classification** (Phân loại nhị phân). Tôi sử dụng tập dữ liệu đã được gán nhãn (labeled data) để huấn luyện mô hình và đo lường sai số.
*   **Kiểm soát Variance và Bias (Debugging ML):** Để tránh hiện tượng Overfitting (High Variance) và Underfitting (High Bias) - những sai lầm phổ biến trong ML, tôi thực hiện:
    *   **Stratified Sampling:** Chia dữ liệu theo tỷ lệ 80/20, đảm bảo phân phối nhãn trong tập Train và Test là tương đồng. Điều này ngăn chặn việc mô hình bị thiên kiến do mất cân bằng dữ liệu.
    *   **Fixed Random Seed (42):** Loại bỏ sự ngẫu nhiên trong việc chia dữ liệu, đảm bảo rằng kết quả thu được là do bản chất của mô hình và dữ liệu, không phải do may mắn.
*   **Tìm kiếm Causal Variables (Biến số nhân quả):** Thay vì chỉ báo cáo Accuracy, tôi sử dụng SHAP để tìm ra các biến số thực sự gây ra quyết định của mô hình. Điều này biến dự án từ một bài tập lập trình thành một nghiên cứu về cơ chế ra quyết định.

### 2.2. Cơ sở lý thuyết về công nghệ
#### a. Cấu trúc tệp PE (Portable Executable)
Tệp PE là định dạng tiêu chuẩn cho các tệp thực thi trên Windows. Tôi tập trung vào hai vùng dữ liệu:
*   **PE Header:** Chứa metadata như timestamp, kích thước các section. Đây là những đặc trưng tĩnh phản ánh cách file được build và compile.
*   **API Import Table:** Danh sách các hàm mà file gọi từ hệ thống. Đây là proxy cho hành vi dự kiến của file (ví dụ: gọi hàm `CreateRemoteThread` thường liên quan đến mã độc).

#### b. Thuật toán XGBoost (Extreme Gradient Boosting)
XGBoost là một thuật toán ensemble dựa trên Gradient Boosting. Nó hoạt động bằng cách xây dựng một chuỗi các cây quyết định, trong đó mỗi cây sau cố gắng sửa lỗi (residual) của các cây trước đó. Mục tiêu là tối thiểu hóa hàm mất mát (Loss function) thông qua việc tối ưu hóa Gradient Descent.

#### c. Lý thuyết SHAP (SHapley Additive exPlanations)
SHAP dựa trên Lý thuyết trò chơi (Game Theory). Một giá trị SHAP $\phi_i$ cho đặc trưng $i$ được tính bằng trung bình đóng góp biên của đặc trưng đó trên tất cả các tập hợp con có thể có của các đặc trưng khác. Điều này đảm bảo tính công bằng (Fairness) và tính nhất quán (Consistency) trong việc phân phối tầm quan trọng của đặc trưng.

---

## PHẦN 3: QUY TRÌNH TRIỂN KHAI CHI TIẾT

### 3.1. Hệ thống thuật ngữ chuẩn hóa
Để báo cáo đạt tính chuyên nghiệp và tránh mơ hồ, tôi phân định rõ 4 khái niệm:
1.  **Architecture (Kiến trúc):** Cấu hình mô hình XGBoost (Hyperparameters) và không gian đặc trưng 5 chiều (PE Header & API Import).
2.  **Pipeline (Luồng dữ liệu):** Chuỗi thao tác tự động: `Raw Data` $\to$ `Stratified Split` $\to$ `XGBoost Training` $\to$ `SHAP Value Computation` $\to$ `Result Export`.
3.  **Workflow (Luồng làm việc):** Quy trình tư duy thực nghiệm lặp: `Đặt giả thuyết` $\to$ `Triển khai Pipeline` $\to$ `Phân tích kết quả` $\to$ `Điều chỉnh giả thuyết`.
4.  **Process (Quá trình):** Phương pháp luận tổng thể từ việc đọc sách giáo khoa $\to$ Thiết lập thực nghiệm $\to$ Biện luận kết quả.

### 3.2. Chi tiết triển khai kỹ thuật (Implementation)
*   **Bước 1: Xử lý dữ liệu:** Trích xuất 1,000 mẫu từ tập EMBER, cân bằng tuyệt đối 500 Benign / 500 Malware để loại bỏ thiên kiến về lớp (class bias).
*   **Bước 2: Lựa chọn đặc trưng:** Tôi chọn 5 đặc trưng có ý nghĩa nhất về mặt an ninh mạng:
    *   `header_coff_timestamp`: Thời điểm tạo file (phát hiện các file được build hàng loạt).
    *   `header_optional_sizeof_code`: Kích thước vùng thực thi (phát hiện các file bị pack/compress).
    *   `header_optional_sizeof_headers`: Kích thước header (phát hiện cấu trúc bất thường).
    *   `sections_count`: Số lượng section (mã độc thường có số section lạ).
    *   `api_calls_count`: Tổng số hàm API được import (phản ánh độ phức tạp của hành vi).
*   **Bước 3: Huấn luyện mô hình:** Sử dụng `XGBClassifier` với tham số mặc định để tạo Baseline ổn định. Tôi không can thiệp quá sâu vào hyperparameter để giữ cho mô hình ở trạng thái "tự nhiên", giúp kết quả SHAP phản ánh đúng bản chất của dữ liệu.
*   **Bước 4: Giải thích mô hình:** Sử dụng `TreeExplainer` của SHAP để tính toán giá trị đóng góp cho toàn bộ tập test.

---

## PHẦN 4: KẾT QUẢ VÀ BIỆN LUẬN KHOA HỌC

### 4.1. Đánh giá hiệu suất (Quantitative Results)
Kết quả thực nghiệm trên tập kiểm thử (Test Set):

| Chỉ số | Giá trị | Ý nghĩa khoa học |
| :--- | :--- | :--- |
| **Accuracy** | **95.50%** | Tỷ lệ dự đoán đúng tổng thể. |
| **Precision** | **97.89%** | Độ tin cậy khi báo động (Rất ít báo động giả). |
| **Recall** | **93.00%** | Khả năng quét sạch mã độc (Bỏ sót 7%). |
| **F1-Score** | **95.38%** | Sự cân bằng giữa khả năng phát hiện và độ chính xác. |

**Biện luận:** Mô hình thể hiện khả năng phân loại mạnh mẽ. Việc Precision cao hơn Recall cho thấy mô hình có xu hướng "thận trọng". Trong thực tế ATTT, điều này cực kỳ quan trọng vì việc báo nhầm một file hệ thống là mã độc (False Positive) gây ra nhiều phiền toái hơn là việc bỏ sót một mẫu mã độc đơn lẻ.

### 4.2. Phân tích bằng chứng (Evidence)
**a. Kiểm chứng tính hợp lệ (Data Validity):**
*(Hình ảnh minh họa: `feature_variance_boxplot.png`)*
$\to$ Biểu đồ Box-plot xác nhận tất cả các đặc trưng đều có phương sai đáng kể. Điều này chứng minh dữ liệu không bị hằng số (constant), loại bỏ nghi ngờ về việc mô hình học được các đặc trưng rác.

**b. Giải quyết RQ1 (Tầm quan trọng nhóm đặc trưng):**
*(Hình ảnh minh họa: `group_shap_contribution.png`)*
$\to$ Tổng đóng góp SHAP của nhóm **PE Header** ($\approx 6.62$) mạnh gấp **8.4 lần** nhóm **API Import** ($\approx 0.79$). Điều này chứng minh một kết luận quan trọng: đối với phân tích tĩnh trên tập dữ liệu này, cấu trúc metadata của file là tín hiệu phân loại mạnh hơn nhiều so với số lượng hàm API.

### 4.3. Khoa học về sự thất bại (Science of Failure - RQ2)
*(Hình ảnh minh họa: `false_positive_top_// ... existing code ...

**Kết luận về Structural Mimicry:** Đây chính là hiện tượng **Mô phỏng cấu trúc**. Mô hình không thực sự hiểu "hành vi độc hại" mà chỉ đang tương quan các **outliers về cấu trúc** với lớp mã độc. Điều này cho thấy một lỗ hổng: kẻ tấn công có thể lừa mô hình bằng cách thay đổi cấu trúc file (Obfuscation) mà không cần thay đổi chức năng.

---

## PHẦN 5: TỰ ĐÁNH GIÁ TRUNG THỰC VÀ GIỚI HẠN (S.18 Frontiers)

Tuân thủ nguyên tắc đánh giá khách quan, tôi xác định các điểm yếu chí mạng của mô hình:
1.  **Sự lệ thuộc vào Proxy:** Mô hình đang dựa vào các "proxy" cấu trúc thay vì bản chất mã độc. Điều này khiến nó dễ sụp đổ trước các kỹ thuật làm mờ cấu trúc (Packing/Obfuscation).
2.  **Giới hạn dữ liệu:** Tập dữ liệu 1,000 mẫu là đủ để minh chứng phương pháp luận nhưng chưa đủ để khái quát hóa cho mọi họ mã độc trên thế giới.
3.  **Độ chính xác gây hiểu lầm:** Con số 95.5% có vẻ ấn tượng, nhưng phân tích SHAP cho thấy mô hình vẫn có những "điểm mù" về ngữ nghĩa (semantics).

--- 

## PHẦN 6: PHỤ LỤC TÁI LẬP (REPRODUCIBILITY)
Toàn bộ dự án được thiết kế để có thể xác thực trong 15 phút:
*   **Tài liệu:** `REPRODUCIBILITY.md` hướng dẫn chi tiết từng bước cài đặt.
*   **Kiểm soát:** Cố định Random Seed (42), sử dụng đúng tệp `ember_1k_real.parquet`.
*   **Thời gian:** Toàn bộ quá trình từ cài đặt đến ra kết quả cuối cùng diễn ra trong dưới 15 phút.

--- 

## PHẦN 7: TÀI LIỆU THAM KHẢO (IEEE Style)
1. S. M. Lundberg and S.-I. Lee, \"A unified approach to interpreting model predictions,\" in *Advances in Neural Information Processing Systems*, 2017.
2. T. Chen and C. Guestrin, \"XGBoost: A scalable tree boosting system,\" in *Proc. of the 22nd ACM SIGKDD*, 2016.
3. T. W. Edgar and D. O. Manz, *Research Methods for Cyber Security*, Syngress, 2017.
4. S. Schloegel et al., \"SoK: Prudent Evaluation Practices for Fuzzing,\" in *IEEE S&P*, 2024.
5. A. Wheeler et al., \"The Things That Count: Coverage Evaluation Under the Microscope,\" in *NDSS*, 2026.
6. S. Mukherjee et al., \"Evading Provenance-Based ML Detectors with Adversarial System Actions,\" in *USENIX Security*, 2023.
7. R. Gupta et al., \"A Survey of Adversarial Machine Learning in Network Intrusion Detection,\" *TechRxiv*, 2024.
8. Hajizadeh et al., \"DeepRed: A Deep Learning-Powered Command and Control Framework,\" in *USENIX Security*, 2025.
9. L. Zhang et al., \"The Range Shrinks, the Threat Remains,\" *arXiv:2605.17062*, 2026.
10. S. Kim et al., \"AI-Driven Security Alert Screening,\" *arXiv:2605.08316*, 2026.
11. Y. Liu et al., \"Formalizing and Benchmarking Prompt Injection Attacks,\" in *USENIX Security*, 2024.
12. C. Chang et al., \"Overcoming the Retrieval Barrier,\" in *USENIX Security*, 2026."