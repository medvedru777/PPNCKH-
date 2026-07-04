import os
import lief
import pandas as pd

def extract_pe_features(file_path, label):
    try:
        binary = lief.parse(file_path)
        if not binary:
            return None
        
        features = {
            'filename': os.path.basename(file_path),
            'label': label,
            'sizeof_code': binary.optional_header.sizeof_code if binary.has_optional_header else 0,
            'sizeof_image': binary.optional_header.sizeof_image if binary.has_optional_header else 0,
            'sizeof_initialized_data': binary.optional_header.sizeof_initialized_data if binary.has_optional_header else 0,
            'numberof_sections': binary.header.numberof_sections if binary.has_header else 0,
        }
        
        import_count = 0
        if binary.has_imports:
            for imp in binary.imports:
                import_count += len(imp.entries)
        features['total_api_imports'] = import_count
        
        return features
    except Exception:
        return None

def process_directory(directory, label):
    data = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            feat = extract_pe_features(file_path, label)
            if feat:
                data.append(feat)
    return data

if __name__ == "__main__":
    print("Bắt đầu trích xuất đặc trưng...")
    malware_data = process_directory("data/raw/malware", label=1)
    benign_data = process_directory("data/raw/benign", label=0)
    
    df = pd.DataFrame(malware_data + benign_data)
    df.to_csv("data/processed/pe_features.csv", index=False)
    print(f"Đã trích xuất xong! Tổng số mẫu: {len(df)}. Dữ liệu lưu tại data/processed/pe_features.csv")