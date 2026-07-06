"import pandas as pd
import numpy as np
import xgboost as xgb
import shap
from scipy.stats import wilcoxon
from sklearn.model_selection import train_test_split

def run_verification():
    print('--- ĐANG TIẾN HÀNH KIỂM ĐỊNH THỐNG KÊ ĐỘC LẬP ---')
    
    # 1. Load dữ liệu (Sử dụng đúng file parquet)
    df = pd.read_parquet('data/ember_1k_balanced.parquet')
    X = df.drop('label', axis=1)
    y = df['label']
    
    # 2. Chia tách dữ liệu (Sử dụng đúng seed 42 để đảm bảo kết quả y hệt)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # 3. Huấn luyện mô hình XGBoost (Baseline đơn giản)
    model = xgb.XGBClassifier(random_state=42, n_estimators=100, max_depth=3, learning_rate=0.1)
    model.fit(X_train, y_train)
    
    # 4. Tính toán giá trị SHAP
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)
    
    # 5. Định nghĩa nhóm đặc trưng
    pe_cols = ['header_coff_timestamp', 'header_optional_sizeof_code', 
               'header_optional_sizeof_headers', 'sections_count']
    api_col = 'api_calls_count'
    
    # Tính tầm quan trọng trung bình tuyệt đối cho mỗi mẫu
    pe_indices = [X_test.columns.get_loc(c) for c in pe_cols]
    api_index = X_test.columns.get_loc(api_col)
    
    pe_importance = np.abs(shap_values[:, pe_indices]).mean(axis=1)
    api_importance = np.abs(shap_values[:, api_index])
    
    # 6. KIỂM ĐỊNH WILCOXON (Mẫu phụ thuộc)
    stat, p_value = wilcoxon(pe_//... a la la... etc)
"