import pandas as pd

def prepare_real_ember():
    # SỬA DÒNG NÀY: Trỏ đường dẫn tới file EMBER lớn mà bạn tải từ Git
    source_file = "data/raw/TEN_FILE_EMBER_GOC_CUA_BAN.parquet" 
    output_file = "data/raw/ember_1k_balanced.parquet"

    try:
        print(f"Đang đọc dữ liệu gốc từ: {source_file} (Có thể mất vài phút vì file rất lớn)...")
        df = pd.read_parquet(source_file)
    except Exception as e:
        print(f"Lỗi: {e}. Vui lòng sửa lại tên file nguồn ở dòng 5.")
        return

    # 1. Lọc bỏ các mẫu không được dán nhãn (-1)
    if 'label' in df.columns:
        df = df[df['label'] != -1]
    else:
        print("Lỗi: Dữ liệu không có cột 'label'.")
        return

    # 2. Rút trích ngẫu nhiên đúng 500 mẫu mỗi loại
    try:
        benign = df[df['label'] == 0].sample(n=500, random_state=42)
        malware = df[df['label'] == 1].sample(n=500, random_state=42)
    except ValueError:
        print("\n[LỖI]: File EMBER của bạn không đủ 500 mẫu cho một trong hai loại nhãn!")
        print(f"Số lượng hiện có trong file gốc: \n{df['label'].value_counts()}")
        return

    # 3. Gộp lại, xáo trộn và xuất ra file đích
    df_balanced = pd.concat([benign, malware]).sample(frac=1, random_state=42).reset_index(drop=True)
    df_balanced.to_parquet(output_file)

    print(f"\nTuyệt vời! Đã trích xuất đúng 1000 mẫu thật từ EMBER.")
    print(f"Dữ liệu đã được lưu tại: {output_file}")

if __name__ == "__main__":
    prepare_real_ember()