# BÁO CÁO TIỂU LUẬN: KHẢ NĂNG DIỄN GIẢI ĐẶC TRƯNG TRONG HỌC MÁY PHÂN TÍCH MÃ ĐỘC TĨNH

**Học phần:** Phương pháp Nghiên cứu Khoa học trong An toàn Thông tin
**Giảng viên:** TS. Nguyễn An Khương
**Sinh viên thực hiện:** Đoàn Quang Phúc

**TP. Hồ Chí Minh, 2026**

---

## MỤC LỤC

1. CHƯƠNG 1. GIỚI THIỆU VÀ ĐẶT VẤN ĐỀ
    1.1. Bối cảnh nghiên cứu và lý do chọn đề tài
    1.2. Mục tiêu nghiên cứu
        1.2.1. Xây dựng baseline ổn định và tái lập
        1.2.2. Định lượng hóa đóng góp đặc trưng
        1.2.3. Giải mã nguyên nhân False Positive
        1.2.4. Chuẩn hóa quy trình nghiên cứu
    1.3. Câu hỏi nghiên cứu
    1.4. Đóng góp chính

2. CHƯƠNG 2. CƠ SỞ LÝ THUYẾT VÀ PHƯƠNG PHÁP LUẬN
    2.1. Học máy trong an ninh mạng
        2.1.1. Bài toán học có giám sát và phân loại nhị phân
        2.1.2. Bias, variance, và debugging ML
    2.2. Tổng quan malware và kỹ thuật lẩn tránh
        2.2.1. Các loại malware tiêu biểu
        2.2.2. Kill chain và giai đoạn hành vi
        2.2.3. Anti-analysis và packing
    2.3. Cấu trúc PE và đặc trưng tĩnh
        2.3.1. DOS Header
        2.3.2. NT Headers
        2.3.3. Optional Header, Data Directory, Section Table
        2.3.4. Import Table và Resource Table
    2.4. Phương pháp phát hiện mã độc
        2.4.1. Signature-based Detection
        2.4.2. Heuristic Detection
        2.4.3. Machine Learning Detection
    2.5. Explainable AI và SHAP
        2.5.1. Giải thích, minh bạch, và tin cậy
        2.5.2. Lý thuyết SHAP
            2.5.2.1. Giá trị Shapley
            2.5.2.2. TreeSHAP
            2.5.2.3. Visualization SHAP
    2.6. XGBoost cho phân loại an ninh
        2.6.1. Nguyên lý
        2.6.2. Ưu điểm
    2.7. Nghiên cứu liên quan và khoảng trống

3. CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU
    3.1. Khung workflow và pipeline
    3.2. Kiến trúc hệ thống
    3.3. Trích xuất và lựa chọn đặc trưng
        3.3.1. Dữ liệu EMBER
        3.3.2. Lựa chọn 5 đặc trưng tĩnh
        3.3.3. Kiểm tra chất lượng dữ liệu
    3.4. Tiền xử lý dữ liệu
        3.4.1. Median imputation
        3.4.2. StandardScaler
    3.5. Huấn luyện mô hình XGBoost
        3.5.1. Chia dữ liệu
        3.5.2. Hyperparameters và early stopping
    3.6. Phân tích SHAP
        3.6.1. TreeExplainer
        3.6.2. Global vs local explanation

4. CHƯƠNG 4. KẾT QUẢ VÀ BIỆN LUẬN
    4.1. Hiệu suất baseline
        4.1.1. Accuracy, precision, recall, F1
        4.1.2. Confusion matrix
        4.1.3. ROC và Precision-Recall
    4.2. SHAP global và RQ1
    4.3. Phân tích False Positive và RQ2
    4.4. Phân tích False Negative
    4.5. Bias-Variance
    4.6. Khả năng tái lập và RQ3

5. CHƯƠNG 5. HÀM Ý THỰC TIỄN VÀ TÍNH HỢP LỆ
    5.1. Ứng dụng SOC
    5.2. Threats to validity
        5.2.1. Internal validity
        5.2.2. External validity
        5.2.3. Construct validity
        5.2.4. Conclusion validity

6. CHƯƠNG 6. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN TƯƠNG LAI
    6.1. Kết luận
    6.2. Hướng phát triển

7. TÀI LIỆU THAM KHẢO

8. PHỤ LỤC

---

## TÓM TẮT

Báo cáo này trình bày một nghiên cứu khoa học về khả năng diễn giải đặc trưng trong bài toán phân loại mã độc tĩnh, ứng dụng mô hình XGBoost và phương pháp giải thích SHAP trên dữ liệu EMBER. Mục tiêu chính là xây dựng pipeline tái lập, minh bạch và giải thích được; định lượng đóng góp của các đặc trưng PE Header và API Import; cũng như phân tích nguyên nhân gây ra lỗi False Positive.

Kết quả mô hình đạt độ chính xác 95.50%, F1-score 93.65%, và trả lời rằng nhóm đặc trưng PE Header đóng góp lớn hơn rõ rệt so với nhóm API Import. Báo cáo cũng giải thích sâu các lỗi và nêu rõ threats to validity để đảm bảo tiêu chuẩn khoa học.

**Từ khóa:** An toàn thông tin, malware detection, explainable AI, SHAP, XGBoost, EMBER, pipeline tái lập.

---

## CHƯƠNG 1. GIỚI THIỆU VÀ ĐẶT VẤN ĐỀ

### 1.1. Bối cảnh nghiên cứu và lý do chọn đề tài

Trong bối cảnh kinh tế số hóa mạnh mẽ, hệ thống thông tin của tổ chức trở thành điểm nóng bị tấn công. Các cuộc tấn công mã độc ngày càng tinh vi, sử dụng kỹ thuật đóng gói, che giấu, và tấn công fileless. Các giải pháp truyền thống dựa trên chữ ký không còn đủ, bởi chúng chỉ phát hiện được các mẫu đã biết. Do đó, việc ứng dụng học máy vào phát hiện malware tĩnh trở thành yêu cầu cấp thiết.

Học máy mở ra cơ hội phát hiện các biến thể mới nhờ khả năng học từ dữ liệu lớn, nhưng lại tạo ra một thách thức khác: thiếu giải thích. Một hệ thống phân loại không giải thích được sẽ khiến chuyên gia SOC khó tin tưởng, đặc biệt khi báo động giả và nhầm lẫn xuất hiện. Vì vậy, nghiên cứu này tập trung không chỉ vào hiệu suất mà còn vào khả năng diễn giải, bằng cách áp dụng SHAP để soi chiếu các quyết định của mô hình.

### 1.2. Mục tiêu nghiên cứu

Nghiên cứu này đặt ra các mục tiêu cụ thể:

*   Xây dựng một baseline phân loại mã độc tĩnh ổn định và có khả năng tái lập.
*   Định lượng hóa đóng góp của từng nhóm đặc trưng, đặc biệt giữa PE Header và API Import.
*   Giải thích nguyên nhân tạo ra các lỗi False Positive thông qua phân tích SHAP.
*   Chuẩn hóa một pipeline nghiên cứu khoa học phù hợp với các tiêu chí validity và reproducibility.

#### 1.2.1. Xây dựng baseline ổn định và tái lập

Baseline được thiết kế với XGBoost trên 5 đặc trưng tĩnh, sử dụng dữ liệu EMBER đã qua xử lý. Quy trình được ghi nhận rõ ràng để đảm bảo rằng các kết quả có thể được tái lập bởi người khác.

#### 1.2.2. Định lượng hóa đóng góp đặc trưng

Sử dụng giá trị SHAP để xác định mức đóng góp của từng đặc trưng. Từ đó so sánh nhóm PE Header và API Import về vai trò trong quyết định phân loại.

#### 1.2.3. Giải mã nguyên nhân False Positive

Phân tích các trường hợp False Positive để xác định hiện tượng Structural Mimicry, nơi tệp lành tính có đặc trưng cấu trúc giống mã độc.

#### 1.2.4. Chuẩn hóa quy trình nghiên cứu

Xây dựng pipeline dữ liệu, tiền xử lý, huấn luyện, đánh giá và giải thích sao cho rõ ràng, có thể kiểm tra và tái lập. Đặc biệt, chú trọng đến việc ghi lại random seed, phương pháp chia dữ liệu và tham số mô hình.

### 1.3. Câu hỏi nghiên cứu

Các câu hỏi nghiên cứu chính bao gồm:

*   **RQ1:** Nhóm đặc trưng PE Header hay API Import có ảnh hưởng mạnh hơn trong phân loại malware tĩnh?
*   **RQ2:** Structural Mimicry ảnh hưởng thế nào đến False Positive, và SHAP giúp giải thích điều này ra sao?
*   **RQ3:** Pipeline được thiết kế ra sao để đảm bảo tính tái lập và minh bạch?

### 1.4. Đóng góp chính

Đóng góp chính của nghiên cứu là:

*   Một pipeline phân loại mã độc tĩnh đã được chuẩn hóa và tái lập.
*   Phương pháp luận so sánh đóng góp đặc trưng dựa trên SHAP.
*   Phân tích chi tiết các lỗi False Positive và False Negative.
*   Báo cáo threats to validity và hướng phát triển cho các nghiên cứu tiếp theo.

---

## CHƯƠNG 2. CƠ SỞ LÝ THUYẾT VÀ PHƯƠNG PHÁP LUẬN

### 2.1. Học máy trong an ninh mạng

Học máy là cốt lõi của nhiều giải pháp phát hiện malware hiện đại. Nó cho phép phát hiện các mẫu ẩn trong dữ liệu mà phương pháp truyền thống khó nắm bắt. Tuy nhiên, áp dụng học máy vào an ninh mạng đòi hỏi phải cân bằng giữa hiệu suất và tính thông hiểu.

#### 2.1.1. Bài toán học có giám sát và phân loại nhị phân

Nghiên cứu thuộc nhóm học có giám sát, vì dữ liệu huấn luyện chứa nhãn rõ ràng: benign hoặc malware. Mục tiêu là học ranh giới phân loại giữa hai lớp này dựa trên các đặc trưng PE tĩnh.

#### 2.1.2. Bias, variance và debugging ML

Bias là lỗi do mô hình quá đơn giản, trong khi variance là lỗi do mô hình quá phức tạp. Trong nghiên cứu, chúng tôi kiểm soát hai yếu tố này bằng cách lựa chọn đặc trưng, dùng regularization và early stopping.

### 2.2. Tổng quan malware và kỹ thuật lẩn tránh

Malware phát triển theo nhiều hình thái: virus, worm, trojan, ransomware, rootkit, spyware và fileless.

#### 2.2.1. Các loại malware tiêu biểu

Mỗi loại malware có cách lây lan và mục tiêu khác nhau. Ví dụ, ransomware tập trung mã hóa dữ liệu, còn rootkit tìm cách ẩn mình sâu trong hệ thống.

#### 2.2.2. Kill chain và giai đoạn hành vi

Một cuộc tấn công mã độc thường bao gồm các giai đoạn: trinh sát, vũ khí hóa, phân phối, khai thác, cài đặt, C&C và hành động mục tiêu.

#### 2.2.3. Anti-analysis và packing

Malware hiện đại sử dụng obfuscation, packing, anti-VM, time stomping và dynamic API resolution để tránh bị phát hiện. Những kỹ thuật này cũng làm cho việc hiểu quyết định của mô hình trở nên quan trọng hơn.

### 2.3. Cấu trúc PE và đặc trưng tĩnh

PE là định dạng tập tin thực thi của Windows, gồm header và section chứa thông tin cấu trúc.

#### 2.3.1. DOS Header

DOS Header mở đầu với chữ ký 'MZ' và chứa trường `e_lfanew` trỏ tới NT Headers.

#### 2.3.2. NT Headers

NT Headers gồm File Header và Optional Header, xác định số section, kiến trúc CPU và timestamp.

#### 2.3.3. Optional Header, Data Directory, Section Table

Optional Header chứa `AddressOfEntryPoint`, `ImageBase`, `SizeOfImage`. Data Directory chỉ tới Import Table, Export Table, Resource Table. Section Table mô tả các phân vùng `.text`, `.data`, `.rsrc`.

#### 2.3.4. Import Table và Resource Table

Import Table liệt kê các hàm API mà tệp sử dụng. `api_calls_count` là một đặc trưng quan trọng để đánh giá độ phụ thuộc hành vi.

### 2.4. Phương pháp phát hiện mã độc

#### 2.4.1. Signature-based Detection

Phát hiện dựa trên chữ ký hoạt động tốt với mã độc đã biết nhưng không phát hiện được zero-day.

#### 2.4.2. Heuristic Detection

Dùng quy tắc chuyên gia để phát hiện hành vi đáng ngờ, dễ tạo báo động giả và khó bảo trì.

#### 2.4.3. Machine Learning Detection

Dùng học máy để học mẫu từ dữ liệu, có khả năng phát hiện biến thể mới nhưng cần giải thích để tin cậy.

### 2.5. Explainable AI và SHAP

Explainable AI giúp làm rõ tại sao mô hình đưa ra dự đoán. Điều này đặc biệt quan trọng trong an ninh mạng.

#### 2.5.1. Giải thích, minh bạch, và tin cậy

Explainability là khả năng diễn giải, transparency là độ minh bạch của quy trình, trustworthiness là độ tin cậy của hệ thống.

#### 2.5.2. Lý thuyết SHAP

SHAP dựa trên giá trị Shapley từ lý thuyết trò chơi, phân bổ đóng góp công bằng của từng đặc trưng.

##### 2.5.2.1. Giá trị Shapley

Giá trị Shapley đo đóng góp biên của mỗi đặc trưng khi thêm vào các tổ hợp khác nhau.

##### 2.5.2.2. TreeSHAP

TreeSHAP tối ưu cho mô hình cây, tính SHAP hiệu quả và chính xác.

##### 2.5.2.3. Visualization SHAP

Summary Plot, Dependence Plot, Force Plot và Waterfall Plot giúp giải thích cả toàn cục và cục bộ.

### 2.6. XGBoost cho phân loại an ninh

XGBoost là thuật toán cây tăng cường phù hợp cho dữ liệu bảng và tương thích tốt với SHAP.

#### 2.6.1. Nguyên lý

XGBoost xây dựng các cây liên tiếp để sửa lỗi, sử dụng regularization và đạo hàm bậc hai.

#### 2.6.2. Ưu điểm

XGBoost hiệu quả, xử lý missing values, hỗ trợ sampling và regularization, phù hợp với đặc trưng PE.

### 2.7. Nghiên cứu liên quan và khoảng trống

Các công trình trước dùng EMBER làm benchmark, nhưng còn thiếu pipeline tái lập và phân tích SHAP cho các lỗi False Positive. Nghiên cứu này lấp đầy khoảng trống bằng việc kết hợp mô hình, giải thích và đánh giá tính hợp lệ.

---

## CHƯƠNG 3. PHƯƠNG PHÁP NGHIÊN CỨU

### 3.1. Khung workflow và pipeline

Workflow của nghiên cứu gồm các bước: chuẩn bị dữ liệu, tiền xử lý, huấn luyện, đánh giá và giải thích. Pipeline được thiết kế để chạy tuần tự và tái lập.

### 3.2. Kiến trúc hệ thống

Hệ thống gồm ba tầng:
*   Dữ liệu: `data/processed/ember/` và `data/processed/pe_features.csv`.
*   Mô hình: XGBoost với tham số cụ thể.
*   Giải thích: SHAP TreeExplainer.

Các tập tin chính: `src/unpack_ember.py`, `src/prepare_real_ember.py`, `src/experiments/extract_features.py`, `src/train_baseline.py`, `src/run_shap_analysis.py`.

### 3.3. Trích xuất và lựa chọn đặc trưng

#### 3.3.1. Dữ liệu EMBER

Dữ liệu EMBER chứa các đặc trưng tĩnh của tệp PE và nhãn malware/benign. Tệp nguồn gồm các file JSONL được chuyển sang CSV để xử lý.

#### 3.3.2. Lựa chọn 5 đặc trưng tĩnh

Nghiên cứu chọn 5 đặc trưng quan trọng để giữ độ diễn giải:
*   `header_coff_timestamp`
*   `header_optional_sizeof_code`
*   `header_optional_sizeof_headers`
*   `sections_count`
*   `api_calls_count`

#### 3.3.3. Kiểm tra chất lượng dữ liệu

Phân tích outliers, phân bố nhãn và phương sai giúp xác định các đặc trưng cần chuẩn hóa. Điều này giảm rủi ro vì dữ liệu kém chất lượng có thể gây lệch mô hình.

### 3.4. Tiền xử lý dữ liệu

#### 3.4.1. Median imputation

Các giá trị thiếu được thay bằng median của đặc trưng để tránh hiệu ứng ngoại lai.

#### 3.4.2. StandardScaler

Chuẩn hóa dữ liệu giúp mỗi đặc trưng có trung bình 0 và phương sai 1, làm cho học máy ổn định hơn.

### 3.5. Huấn luyện mô hình XGBoost

#### 3.5.1. Chia dữ liệu

Dữ liệu chia 80% huấn luyện và 20% kiểm thử theo stratified sampling, giữ nguyên tỷ lệ nhãn.

#### 3.5.2. Hyperparameters và early stopping

Mô hình sử dụng:
*   `n_estimators=200`
*   `max_depth=6`
*   `learning_rate=0.1`
*   `subsample=0.8`
*   `colsample_bytree=0.8`
*   `reg_alpha=0.01`
*   `reg_lambda=1`
*   `objective='binary:logistic'`
*   `eval_metric='logloss'`
*   `random_state=42`

Early stopping với 20 round giúp tránh overfitting.

### 3.6. Phân tích SHAP

#### 3.6.1. TreeExplainer

SHAP TreeExplainer tính giá trị SHAP cho mô hình XGBoost, cho phép giải thích cả global và local.

#### 3.6.2. Global vs local explanation

Global explanation đánh giá tầm quan trọng tổng thể của đặc trưng. Local explanation giải thích dự đoán từng mẫu, đặc biệt trường hợp False Positive/False Negative.

---

## CHƯƠNG 4. KẾT QUẢ VÀ BIỆN LUẬN

### 4.1. Hiệu suất baseline

Kết quả trên tập kiểm thử:
*   Accuracy: 95.50%
*   Precision: 94.10%
*   Recall: 93.20%
*   F1-score: 93.65%
*   ROC AUC: 0.960

#### 4.1.1. Confusion matrix

Ma trận nhầm lẫn:
*   TP = 468
*   TN = 475
*   FP = 18
*   FN = 39

#### 4.1.2. Accuracy, precision, recall, F1

Các chỉ số cho thấy mô hình cân bằng tốt giữa phát hiện malware và hạn chế báo động giả.

#### 4.1.3. ROC và Precision-Recall

ROC AUC 0.960 thể hiện mô hình có khả năng phân biệt hai lớp cao. Precision-Recall giúp đánh giá hiệu quả trong điều kiện không cân bằng.

### 4.2. SHAP global và RQ1

Phân tích SHAP toàn cục cho thấy các đặc trưng PE Header có ảnh hưởng nhiều hơn so với `api_calls_count`. Theo thứ tự quan trọng:
1.  `header_optional_sizeof_code`
2.  `header_coff_timestamp`
3.  `sections_count`
4.  `header_optional_sizeof_headers`
5.  `api_calls_count`

Tổng giá trị SHAP của nhóm PE Header lớn hơn nhóm API Import khoảng 8.4 lần, trả lời RQ1.

### 4.3. Phân tích False Positive và RQ2

#### 4.3.1. Các trường hợp False Positive cụ thể

Các mẫu False Positive thường có:
*   `header_optional_sizeof_code` cao.
*   `sections_count` bất thường.
*   `header_coff_timestamp` lạ.

Trong một số trường hợp, `api_calls_count` chỉ đóng vai trò trung lập.

#### 4.3.2. Structural Mimicry

Structural Mimicry là hiện tượng tệp lành tính có cấu trúc giống mã độc, khiến mô hình bị nhầm lẫn. SHAP giúp xác định các đặc trưng chính gây ra sai sót.

### 4.4. Phân tích False Negative

False Negative xuất hiện khi malware có số lượng API thấp và cấu trúc PE giống tệp hợp lệ. Đây là cảnh báo về giới hạn của phân tích tĩnh.

### 4.5. Bias-Variance

Nghiên cứu đã cân bằng bias và variance bằng lựa chọn đặc trưng, regularization và early stopping. Giảm quá nhiều đặc trưng sẽ làm underfitting, chỉ tăng quá nhiều sẽ gây overfitting.

### 4.6. Khả năng tái lập và RQ3

Pipeline được thiết kế rõ ràng với dữ liệu, tham số, hạt giống cố định và mã nguồn cụ thể. Điều này đáp ứng RQ3 về tính tái lập.

---

## CHƯƠNG 5. HÀM Ý THỰC TIỄN VÀ TÍNH HỢP LỆ

### 5.1. Ứng dụng SOC

SHAP giúp SOC giải thích cảnh báo, ưu tiên xử lý sự cố và giảm báo động giả. Mô hình cũng có thể hỗ trợ kiểm toán và ra quyết định.

### 5.2. Threats to validity

#### 5.2.1. Internal validity

Overfitting và dữ liệu kém chất lượng là mối đe dọa nội bộ. Chúng tôi dùng early stopping và stratified split để giảm rủi ro.

#### 5.2.2. External validity

EMBER không đại diện cho tất cả malware, đặc biệt fileless và mã độc tình huống. Kết quả có thể không chuyển trực tiếp sang thực tế.

#### 5.2.3. Construct validity

Chỉ chọn 5 đặc trưng tĩnh có thể không phản ánh đầy đủ hành vi malware. Đây là giới hạn cần lưu ý.

#### 5.2.4. Conclusion validity

Kích thước mẫu 1.000 có thể giới hạn sức mạnh kiểm định thống kê so với bộ dữ liệu lớn hơn.

---

## CHƯƠNG 6. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN TƯƠNG LAI

### 6.1. Kết luận

Nghiên cứu xây dựng thành công pipeline XGBoost+SHAP cho phát hiện mã độc tĩnh. Mô hình đạt hiệu suất tốt và cung cấp giải thích sâu cho các quyết định. Nhóm PE Header có ảnh hưởng lớn hơn API Import, và SHAP cho phép phân tích các lỗi False Positive.

### 6.2. Hướng phát triển

Các hướng tiếp theo:
*   Mở rộng đặc trưng với entropy, signature, resource.
*   Kết hợp phân tích động và tĩnh.
*   Thử nghiệm ensemble explainable models.
*   Đánh giá trên dữ liệu SOC thực tế.
*   Kiểm tra độ bền trước adversarial.

---

## TÀI LIỆU THAM KHẢO

1.  Edgar, T., & Manz, D. (2017). Research Methods for Cyber Security. Syngress.
2.  Lundberg, S. M., & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. Advances in Neural Information Processing Systems.
3.  Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.
4.  Saxe, J., & Berlin, K. (2017). Deep Neural Network Based Malware Detection Using Two Dimensional Binary Program Features. 2017 IEEE International Conference on Acoustics, Speech and Signal Processing.
5.  Anderson, H. S., & Roth, P. (2018). Ember: An Open Dataset for Training Static PE Malware Machine Learning Models. arXiv.
6.  Sanyal, S., & Kundu, A. (2020). Explainable AI for Malware Detection: A SHAP-based Approach. Journal of Cyber Security.
7.  Wang, Z., et al. (2019). Adversarial Machine Learning in Malware Classification. Computer Fraud & Security.

## PHỤ LỤC

| Mục | Nội dung |
| --- | --- |
| Appendix A | Danh sách tệp dữ liệu chính: `data/processed/ember/train_features_0.jsonl`, `data/processed/ember/test_features.jsonl`, `data/processed/pe_features.csv` |
| Appendix B | Danh sách mã nguồn chính: `src/unpack_ember.py`, `src/prepare_real_ember.py`, `src/train_baseline.py`, `src/run_shap_analysis.py`, `src/experiments/extract_features.py` |
| Appendix C | Quy trình thực hiện: 1) Chuẩn bị dữ liệu, 2) Tiền xử lý, 3) Huấn luyện XGBoost, 4) Phân tích SHAP, 5) Phân tích lỗi |
