# BÁO CÁO TIẾN ĐỘ NGHIÊN CỨU: PHÂN TÍCH TÍNH GIẢI THÍCH CỦA MÔ HÌNH ML TRONG PHÁT HIỆN MALWARE

**Sinh viên thực hiện:** Đoàn Quang Phát  
**Học phần:** Phương pháp Nghiên cứu Khoa học trong ATTT  

---

## 1. GIỚI THIỆU (INTRODUCTION)

### 1.1. Đặt vấn đề
Hiện nay, các mô hình Machine Learning (ML) trong phát hiện Malware thường hoạt động như một 'Hộp đen' (Black-box). Dù độ chính xác cao, nhưng việc không biết **tại sao** mô hình đưa ra quyết định dẫn đến hai rủi ro:
1. **Tin tưởng sai chỗ:** Mô hình có thể dựa vào các đặc trưng nhiễu (noise) thay vì hành vi thực của Malware.
2. **Khó khăn trong đối phó:** Không thể xác định được kẻ tấn công đang giả mạo đặc trưng nào để nâng cấp hệ thống phòng thủ.

### 1.2. Mục tiêu nghiên cứu
Sử dụng phương pháp **SHAP (SHapley Additive exPlanations)** để 'mở hộp đen' mô hình XGBoost, từ đó:
*   Xác định mức độ quan trọng của các nhóm đặc trưng (PE Header vs. API Import).
*   Phát hiện hiện tượng **'Structural Mimicry'** (Giả mạo cấu trúc) gây ra lỗi False Positive.
*   Xây dựng một pipeline thực nghiệm khách quan và có khả năng tái lập.

### 1.3. Câu hỏi nghiên cứu (Research Questions)
*   **RQ1:** Giữa đặc trưng tĩnh (PE Header) và đặc trưng hành vi (API Import), nhóm nào đóng vai trò quyết định hơn trong phân loại?
*   **RQ2:** Hiện tượng 'Giả mạo cấu trúc' ảnh hưởng thế nào đến kết quả và làm sao để nhận diện nó qua SHAP?
*   **RQ3:** Quy trình thực nghiệm cần những yếu tố nào để đảm bảo tính khách quan và tái lập (reproducibility)?

---

## 2. PHƯƠNG PHÁP LUẬN & CƠ SỞ LÝ THUYẾT

### 2.1. Phương pháp tiếp cận (Methodology)
Nghiên cứu áp dụng khung **Supervised Learning** cho bài toán **Binary Classification**:
*   **Kiểm soát sai số:** Sử dụng *Stratified Sampling* (chia dữ liệu 80/20 theo tỷ lệ lớp) và *Fixed Random Seed (42)* để loại bỏ yếu tố may rủi.
*   **Phân tích nguyên nhân:** Thay vì chỉ nhìn vào Accuracy, sử dụng giá trị Shapley để tìm các biến nguyên nhân (Causal Variables).

### 2.2. Các khái niệm then chốt (Simplified)
| Khái niệm | Vai trò trong báo cáo |
| :--- | :--- |
| **PE Header** | Metadata của file (timestamp, size...). Đại diện cho 'hình dáng' file. |
| **API Import** | Danh sách hàm hệ thống được gọi. Đại diện cho 'hành vi' dự kiến. |
| **XGBoost** | Thuật toán phân loại mạnh mẽ dựa trên nhiều cây quyết định (Decision Trees). |
| **SHAP** | Phương pháp toán học định lượng đóng góp của mỗi đặc trưng vào kết quả cuối cùng. |

---

## 3. QUY TRÌNH THỰC NGHIỆM (WORKFLOW)

**Luồng dữ liệu tổng quát:**
Raw Data (EMBER) $ightarrow$ Preprocessing $ightarrow$ Model Training $ightarrow$ XAI Analysis $ightarrow$ Insight Extraction

**Chi tiết các bước triển khai:**

1.  **Thu thập & Tiền xử lý:**
    *   Trích xuất 1,000 mẫu từ tập EMBER (500 Benign / 500 Malware) để cân bằng dữ liệu.
    *   Chọn lọc 5 đặc trưng đại diện: 	imestamp, sizeof_code, sizeof_headers, sections_count, pi_calls_count.
2.  **Huấn luyện Mô hình:**
    *   Sử dụng XGBClassifier tạo Baseline.
    *   Chia tập Train/Test theo tỷ lệ 80/20 (Stratified).
3.  **Phân tích Giải thích (XAI):**
    *   Áp dụng TreeExplainer của SHAP để tính toán giá trị đóng góp cho từng mẫu trong tập Test.
4.  **Đánh giá & Biện luận:**
    *   So sánh tổng giá trị SHAP của nhóm PE Header và API Import.
    *   Phân tích các mẫu False Positive để tìm dấu hiệu 'Structural Mimicry'.

---

## 4. KẾT QUẢ VÀ BIỆN LUẬN KHOA HỌC

### 4.1. Kết quả định lượng (Quantitative)
| Chỉ số | Giá trị | Ý nghĩa |
| :--- | :--- | :--- |
| **Accuracy** | **95.50%** | Độ chính xác tổng thể cao. |
| **Precision** | **97.89%** | Rất ít khi nhầm file sạch thành malware (ít FP). |
| **Recall** | **93.00%** | Bỏ sót khoảng 7% malware. |
| **F1-Score** | **95.38%** | Sự cân bằng tốt giữa Precision và Recall. |

### 4.2. Phân tích chuyên sâu (Qualitative)
*   **Kết luận RQ1:** Tổng đóng góp SHAP của **PE Header ($pprox 6.62$)** cao gấp **8.4 lần** so với **API Import ($pprox 0.79$)**. 
    *   $\Rightarrow$ *Insight:* Mô hình đang dựa vào 'vỏ' file nhiều hơn là 'ruột' hành vi.
*   **Kết luận RQ2 (Science of Failure):** Phát hiện hiện tượng **Structural Mimicry**. Mô hình bị đánh lừa bởi các điểm bất thường (outliers) trong cấu trúc file mà không quan tâm đến chức năng thực sự.
    *   $\Rightarrow$ *Hệ quả:* Kẻ tấn công có thể dễ dàng vượt qua mô hình này bằng cách thay đổi Header (Obfuscation) mà không cần thay đổi code độc hại.

---

## 5. TỰ ĐÁNH GIÁ VÀ GIỚI HẠN

1.  **Điểm yếu:** Mô hình phụ thuộc quá nhiều vào các 'Proxy' (đặc trưng đại diện) thay vì bản chất malware.
2.  **Giới hạn dữ liệu:** Tập mẫu 1,000 file là đủ để chứng minh phương pháp nhưng chưa đủ để đại diện cho toàn bộ thế giới Malware.
3.  **Hướng phát triển:** Cần kết hợp thêm phân tích động (Dynamic Analysis) để giảm sự phụ thuộc vào PE Header.

---

## 6. KHẢ NĂNG TÁI LẬP (REPRODUCIBILITY)
Để đảm bảo tính khách quan, toàn bộ thực nghiệm có thể tái lập trong **15 phút**:
*   **Dataset:** ember_1k_real.parquet
*   **Config:** Random Seed = 42.
*   **Hướng dẫn:** Chi tiết tại file REPRODUCIBILITY.md.

---

## 7. TÀI LIỆU THAM KHẢO (IEEE Style)
1. S. M. Lundberg and S.-I. Lee, 'A unified approach to interpreting model predictions,' in *Advances in Neural Information Processing Systems*, 2017.
2. T. Chen and C. Guestrin, 'XGBoost: A scalable tree boosting system,' in *Proc. of the 22nd ACM SIGKDD*, 2016.
3. T. W. Edgar and D. O. Manz, *Research Methods for Cyber Security*, Syngress, 2017.
4. S. Schloegel et al., 'SoK: Prudent Evaluation Practices for Fuzzing,' in *IEEE S&P*, 2024.
5. A. Wheeler et al., 'The Things That Count: Coverage Evaluation Under the Microscope,' in *NDSS*, 2026.
6. S. Mukherjee et al., 'Evading Provenance-Based ML Detectors with Adversarial System Actions,' in *USENIX Security*, 2023.
7. R. Gupta et al., 'A Survey of Adversarial Machine Learning in Network Intrusion Detection,' *TechRxiv*, 2024.
8. Hajizadeh et al., 'DeepRed: A Deep Learning-Powered Command and Control Framework,' in *USENIX Security*, 2025.
9. L. Zhang et al., 'The Range Shrinks, the Threat Remains,' *arXiv:2605.17062*, 2026.
10. S. Kim et al., 'AI-Driven Security Alert Screening,' *arXiv:2605.08316*, 2026.
11. Y. Liu et al., 'Formalizing and Benchmarking Prompt Injection Attacks,' in *USENIX Security*, 2024.
12. C. Chang et al., 'Overcoming the Retrieval Barrier,' in *USENIX Security*, 2026.
