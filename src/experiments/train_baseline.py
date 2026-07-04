import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def train_and_evaluate():
    try:
        df = pd.read_csv("data/processed/pe_features.csv")
    except FileNotFoundError:
        print("Không tìm thấy file pe_features.csv. Hãy chạy extract_features.py trước.")
        return

    if len(df) < 4:
        print("Dữ liệu quá ít để chia tập train/test. Hãy thêm file PE vào data/raw/")
        return

    X = df.drop(columns=['filename', 'label'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("Đang huấn luyện XGBoost Baseline...")
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    
    cm = confusion_matrix(y_test, y_pred)
    if cm.size == 4:
        tn, fp, fn, tp = cm.ravel()
        fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    else:
        fpr = 0.0

    print("\n--- KẾT QUẢ MÔ HÌNH CƠ SỞ (BASELINE) ---")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred, zero_division=0):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred, zero_division=0):.4f}")
    print(f"F1-Score:  {f1_score(y_test, y_pred, zero_division=0):.4f}")
    print(f"False Positive Rate (FPR): {fpr:.4f}")

if __name__ == "__main__":
    train_and_evaluate()