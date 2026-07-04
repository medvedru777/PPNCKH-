import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

# Bỏ qua các cảnh báo không quan trọng để terminal sạch sẽ
warnings.filterwarnings('ignore')

def train_from_parquet():
    file_path = "data/raw/ember_1k_balanced.parquet" 
    
    print(f"Reading data from: {file_path}")
    df = pd.read_parquet(file_path)

    # Lọc bỏ nhãn -1 (không xác định)
    df = df[df['label'] != -1]
    print(f"Total samples with labels: {len(df)}")
    
    # KIỂM TRA PHÂN BỐ NHÃN
    print("\nLabel distribution (0: Benign, 1: Malicious):")
    print(df['label'].value_counts())

    if len(df['label'].unique()) < 2:
        print("\n[CRITICAL DATA ERROR]: Dataset contains only ONE class!")
        return
    
    y = df['label']
    X = df.drop(columns=['label'])
    
    # Giữ lại các cột dạng số
    X = X.select_dtypes(include=['number'])

    # Chia tập train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("\nTraining XGBoost Baseline...")
    model = xgb.XGBClassifier(eval_metric='logloss', random_state=42)
    model.fit(X_train, y_train)

    # Dự đoán
    y_pred = model.predict(X_test)
    
    print("\n--- BASELINE RESULTS ---")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred, zero_division=0):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred, zero_division=0):.4f}")
    print(f"F1-Score:  {f1_score(y_test, y_pred, zero_division=0):.4f}")

    # VẼ MA TRẬN NHẦM LẪN (Confusion Matrix Plot)
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Benign', 'Malware'],
                yticklabels=['Benign', 'Malware'])
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix - XGBoost Baseline')

    os.makedirs('figures', exist_ok=True)
    plt.savefig('figures/confusion_matrix.png', dpi=300)
    print("\nSaved Confusion Matrix plot to: figures/confusion_matrix.png")

if __name__ == "__main__":
    train_from_parquet()