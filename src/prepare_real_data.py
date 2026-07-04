import json
import pandas as pd
import glob
import os

def extract_real_ember():
    # Dùng dấu * để quét tất cả các file JSONL trong thư mục
    input_pattern = "data/processed/ember/ember2018/train_features_*.jsonl"
    output_file = "data/raw/ember_1k_real.parquet"

    file_list = glob.glob(input_pattern)
    if not file_list:
        print(f"Lỗi: Không tìm thấy file nào khớp với đường dẫn {input_pattern}")
        return

    malware_data = []
    benign_data = []

    print(f"Đã tìm thấy {len(file_list)} file JSONL. Đang tiến hành quét sâu để tìm đủ 500 mã độc và 500 an toàn...")

    for input_file in file_list:
        print(f"Đang quét file: {os.path.basename(input_file)}...")
        with open(input_file, 'r') as f:
            for line in f:
                try:
                    record = json.loads(line)
                    label = record.get('label', -1)

                    if label == -1:
                        continue

                    # Rút trích các đặc trưng chuẩn để so sánh Header vs API (Yêu cầu T15)
                    features = {
                        'label': label,
                        'header_coff_timestamp': record.get('header', {}).get('coff', {}).get('timestamp', 0),
                        'header_optional_sizeof_code': record.get('header', {}).get('optional', {}).get('sizeof_code', 0),
                        'header_optional_sizeof_headers': record.get('header', {}).get('optional', {}).get('sizeof_headers', 0),
                        'sections_count': len(record.get('section', {}).get('sections', [])),
                    }

                    # Đếm tổng số hàm API được import
                    imports_dict = record.get('imports', {})
                    total_api_calls = sum(len(funcs) for funcs in imports_dict.values()) if isinstance(imports_dict, dict) else 0
                    features['api_calls_count'] = total_api_calls

                    # Phân loại và thêm vào list
                    if label == 1 and len(malware_data) < 500:
                        malware_data.append(features)
                    elif label == 0 and len(benign_data) < 500:
                        benign_data.append(features)

                    # Tối ưu hóa: Nếu đã đủ 1000 mẫu thì thoát ngay lập tức
                    if len(malware_data) == 500 and len(benign_data) == 500:
                        break
                except Exception:
                    continue
        
        # Thoát vòng lặp quét file nếu đã gom đủ
        if len(malware_data) == 500 and len(benign_data) == 500:
            break

    print(f"\nThành công! Đã gom đủ {len(malware_data)} mã độc và {len(benign_data)} an toàn.")
    
    if len(malware_data) == 0 or len(benign_data) == 0:
        print("Lỗi: Dữ liệu vẫn bị thiếu nhãn. Hãy kiểm tra lại bộ dữ liệu EMBER.")
        return

    # Gộp, xáo trộn và lưu file
    df = pd.DataFrame(malware_data + benign_data)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df.to_parquet(output_file)
    print(f"Đã lưu tập dữ liệu chuẩn 1K mẫu tại: {output_file}")

if __name__ == "__main__":
    extract_real_ember()