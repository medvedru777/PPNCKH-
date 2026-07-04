import json
import os
import pandas as pd
from tqdm import tqdm

def extract_balanced_samples(jsonl_path, output_parquet_path, samples_per_class=500, random_seed=42):
    """
    Đọc tuần tự file JSONL của EMBER 2018 và trích xuất số lượng mẫu cân bằng.
    
    Tham số:
    - jsonl_path: Đường dẫn tới file train_features_0.jsonl hoặc các file tương tự.
    - output_parquet_path: Đường dẫn lưu file kết quả sau khi trích xuất (.parquet).
    - samples_per_class: Số lượng mẫu cho mỗi nhãn (500 benign, 500 malware).
    - random_seed: Khởi tạo để đảm bảo tính tái lập kết quả khoa học.
    """
    
    benign_samples = []
    malware_samples = []
    
    print(f"[*] Đang quét tuần tự dữ liệu từ: {jsonl_path}")
    
    # Mở và đọc từng dòng của file JSONL (Mỗi dòng là 1 tệp tin)
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in tqdm(f, desc="Đang duyệt mẫu"):
            # Dừng quét nếu cả hai nhóm đã thu thập đủ số lượng
            if len(benign_samples) >= samples_per_class and len(malware_samples) >= samples_per_class:
                break
                
            item = json.loads(line)
            label = item.get('label')
            
            # Phân loại và đưa vào bộ đệm nếu chưa đủ số lượng
            if label == 0 and len(benign_samples) < samples_per_class:
                benign_samples.append(item)
            elif label == 1 and len(malware_samples) < samples_per_class:
                malware_samples.append(item)
                
    # Gộp 2 tập dữ liệu lại thành 1000 mẫu
    total_samples = benign_samples + malware_samples
    
    print(f"[+] Thu thập thành công: {len(benign_samples)} Benign và {len(malware_samples)} Malware.")
    
    # Chuyển đổi sang Pandas DataFrame để tự động "giải phẳng" (Flatten) các trường dữ liệu lồng nhau
    print("[*] Đang cấu trúc hóa dữ liệu sang dạng bảng (DataFrame)...")
    df = pd.json_normalize(total_samples)
    
    # Xáo trộn ngẫu nhiên dữ liệu dựa trên seed cố định để tránh mô hình bị học lệch theo thứ tự lọc
    df = df.sample(frac=1, random_state=random_seed).reset_index(drop=True)
    
    # Tạo thư mục lưu trữ nếu chưa có
    os.makedirs(os.path.dirname(output_parquet_path), exist_ok=True)
    
    # Lưu xuống định dạng Parquet để giữ nguyên cấu trúc kiểu dữ liệu và tối ưu dung lượng ổ đĩa
    df.to_parquet(output_parquet_path, index=False)
    print(f"[+] Đã lưu dữ liệu 1000 mẫu thành công tại: {output_parquet_path}")
    
    return df

# Đoạn code kiểm tra chạy thử module
if __name__ == "__main__":
    # Cấu hình đường dẫn mẫu dựa trên cấu trúc thư mục của bạn
    INPUT_JSONL = r"data\processed\ember\ember2018\train_features_0.jsonl"
    OUTPUT_PARQUET = r"data\processed\ember_1k_balanced.parquet"
    
    # Thực thi (Chỉ chạy khi file INPUT_JSONL thực sự tồn tại)
    if os.path.exists(INPUT_JSONL):
        df_1k = extract_balanced_samples(INPUT_JSONL, OUTPUT_PARQUET)
        print(f"Kích thước bảng dữ liệu: {df_1k.shape}")
    else:
        print(f"[-] Không tìm thấy file gốc tại {INPUT_JSONL}. Vui lòng kiểm tra lại đường dẫn.")