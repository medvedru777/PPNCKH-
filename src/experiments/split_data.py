import os
import shutil

def split_dataset():
    source_dir = "data/raw/unlabeled"
    malware_dir = "data/raw/malware"
    benign_dir = "data/raw/benign"

    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    if len(files) == 0:
        print("Thư mục unlabeled đang trống! Hãy thả 1000 file vào đó trước.")
        return

    print(f"Đã tìm thấy {len(files)} file. Đang tiến hành chia đôi...")
    mid = len(files) // 2
    
    # Copy nửa đầu vào malware
    for f in files[:mid]:
        shutil.copy(os.path.join(source_dir, f), os.path.join(malware_dir, f))
        
    # Copy nửa sau vào benign
    for f in files[mid:]:
        shutil.copy(os.path.join(source_dir, f), os.path.join(benign_dir, f))
        
    print(f"Xong! Đã ném {mid} file vào malware và {len(files) - mid} file vào benign.")

if __name__ == "__main__":
    split_dataset()