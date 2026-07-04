import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
import xgboost as xgb
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score,
                             precision_score, recall_score)
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

FEATURE_GROUPS = {
    "PE Header": [
        "header_coff_timestamp",
        "header_optional_sizeof_code",
        "header_optional_sizeof_headers",
        "sections_count",
    ],
    "API Import": ["api_calls_count"],
}


def _ensure_numpy_shap(shap_values):
    if isinstance(shap_values, list) and len(shap_values) == 2:
        return shap_values[1]
    return np.array(shap_values)


def _save_shap_summary_plot(shap_values, X, output_path):
    plt.figure(figsize=(10, 6))
    shap.summary_plot(shap_values, X, show=False)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def _compute_feature_shap_summary(shap_values, X):
    mean_abs = np.mean(np.abs(shap_values), axis=0)
    return pd.DataFrame({
        "feature": X.columns,
        "mean_abs_shap": mean_abs,
    }).sort_values("mean_abs_shap", ascending=False)


def _compute_group_shap_contributions(feature_summary, groups, output_path):
    records = []
    feature_to_mean = feature_summary.set_index("feature")["mean_abs_shap"].to_dict()
    for group_name, group_features in groups.items():
        selected = [f for f in group_features if f in feature_to_mean]
        if not selected:
            continue
        mean_abs_values = [feature_to_mean[f] for f in selected]
        records.append({
            "group": group_name,
            "features": ", ".join(selected),
            "feature_count": len(selected),
            "group_mean_abs_shap": float(np.sum(mean_abs_values)),
            "group_total_abs_shap": float(np.sum(mean_abs_values) * len(X)),
            "mean_abs_shap_per_feature": float(np.mean(mean_abs_values)),
        })
    group_df = pd.DataFrame(records)
    group_df.to_csv(output_path, index=False)
    return group_df


def _save_group_shap_plot(group_df, output_path):
    plt.figure(figsize=(8, 5))
    plt.bar(group_df['group'], group_df['group_mean_abs_shap'], color=['#0072B2', '#D55E00'])
    plt.title('Group SHAP contribution comparison')
    plt.xlabel('Feature Group')
    plt.ylabel('Mean Absolute SHAP')
    for x, y in enumerate(group_df['group_mean_abs_shap']):
        plt.text(x, y + 0.05, f"{y:.2f}", ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def _save_false_positive_feature_plot(importance_df, output_path):
    top5 = importance_df.head(5)
    plt.figure(figsize=(8, 5))
    plt.barh(top5['feature'][::-1], top5['mean_abs_shap'][::-1], color='#D55E00')
    plt.title('Top false positive feature importance')
    plt.xlabel('Mean Absolute SHAP')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def _save_false_positive_results(model, X_test, X, y_test, y_pred, explainer, output_dir):
    probabilities = model.predict_proba(X_test)[:, 1]
    y_test = y_test.reset_index(drop=True)
    X_test = X_test.reset_index(drop=True)
    y_pred = pd.Series(y_pred, name='predicted').reset_index(drop=True)
    proba_series = pd.Series(probabilities, name='probability').reset_index(drop=True)

    fp_mask = (y_test == 0) & (y_pred == 1)

    false_positive_predictions = X_test.loc[fp_mask].copy()
    false_positive_predictions['label'] = 0
    false_positive_predictions['predicted'] = 1
    false_positive_predictions['probability'] = proba_series[fp_mask].values
    false_positive_predictions.to_csv(os.path.join(output_dir, 'false_positive_predictions.csv'), index=False)

    if false_positive_predictions.empty:
        print('Không có false positive để phân tích.')
        return None

    raw_shap_values = explainer.shap_values(X_test)
    test_shap_values = _ensure_numpy_shap(raw_shap_values)
    false_positive_shap = test_shap_values[fp_mask.values]
    false_positive_shap_df = pd.DataFrame(false_positive_shap, columns=X.columns)
    false_positive_shap_df['label'] = 0
    false_positive_shap_df['predicted'] = 1
    false_positive_shap_df['probability'] = proba_series[fp_mask].values
    false_positive_shap_df.to_csv(os.path.join(output_dir, 'false_positive_shap_values.csv'), index=False)

    mean_abs_shap = np.mean(np.abs(false_positive_shap), axis=0)
    false_positive_importance = pd.DataFrame({
        'feature': X.columns,
        'mean_abs_shap': mean_abs_shap,
    }).sort_values('mean_abs_shap', ascending=False)
    false_positive_importance.to_csv(os.path.join(output_dir, 'false_positive_feature_importance.csv'), index=False)

    _save_false_positive_feature_plot(false_positive_importance, os.path.join('figures', 'false_positive_top_features.png'))
    return false_positive_importance


def train_and_explain():
    file_path = 'data/raw/ember_1k_real.parquet'

    try:
        df = pd.read_parquet(file_path)
    except FileNotFoundError:
        print('Lỗi: Không tìm thấy file parquet. Hãy chạy prepare_real_data.py trước.')
        return

    if 'label' not in df.columns:
        print('Dữ liệu đầu vào không chứa cột label.')
        return

    y = df['label']
    X = df.drop(columns=['label'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print('Đang huấn luyện mô hình XGBoost...')
    model = xgb.XGBClassifier(eval_metric='logloss', random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print('\n--- KẾT QUẢ ĐÁNH GIÁ (Ghi vào báo cáo) ---')
    print(f'Accuracy:  {accuracy_score(y_test, y_pred):.4f}')
    print(f'Precision: {precision_score(y_test, y_pred, zero_division=0):.4f}')
    print(f'Recall:    {recall_score(y_test, y_pred, zero_division=0):.4f}')
    print(f'F1-Score:  {f1_score(y_test, y_pred, zero_division=0):.4f}')

    cm = confusion_matrix(y_test, y_pred)
    print(f'Confusion matrix: {cm.tolist()}')

    print('\nĐang tính toán giá trị phân tán SHAP...')
    explainer = shap.TreeExplainer(model)
    raw_shap_values = explainer.shap_values(X)
    shap_values = _ensure_numpy_shap(raw_shap_values)

    docs_dir = 'docs'
    figures_dir = 'figures'
    results_dir = 'results'
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(figures_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    shap_summary_path = os.path.join(docs_dir, 'shap_summary.png')
    shap_summary_fig_path = os.path.join(figures_dir, 'shap_summary.png')
    _save_shap_summary_plot(shap_values, X, shap_summary_path)
    _save_shap_summary_plot(shap_values, X, shap_summary_fig_path)
    print(f'HOÀN TẤT! Đã lưu biểu đồ SHAP tại: {shap_summary_path} và {shap_summary_fig_path}')

    feature_summary = _compute_feature_shap_summary(shap_values, X)
    feature_summary.to_csv(os.path.join(results_dir, 'feature_shap_summary.csv'), index=False)

    group_df = _compute_group_shap_contributions(feature_summary, FEATURE_GROUPS,
                                               os.path.join(results_dir, 'group_shap_contributions.csv'))
    _save_group_shap_plot(group_df, os.path.join(figures_dir, 'group_shap_contribution.png'))
    print('Đã lưu group SHAP contributions và biểu đồ group_shap_contribution.png')

    _save_false_positive_results(model, X_test, X, y_test, y_pred, explainer, results_dir)
    print('Đã lưu kết quả false positive, SHAP values và biểu đồ false_positive_top_features.png')

    print('\n--- TỔNG KẾT FILE ĐẦU RA ---')
    print(f'- {shap_summary_path}')
    print(f'- {shap_summary_fig_path}')
    print(f'- {os.path.join(results_dir, "feature_shap_summary.csv")}')
    print(f'- {os.path.join(results_dir, "group_shap_contributions.csv")}')
    print(f'- {os.path.join(results_dir, "false_positive_predictions.csv")}')
    print(f'- {os.path.join(results_dir, "false_positive_shap_values.csv")}')
    print(f'- {os.path.join(results_dir, "false_positive_feature_importance.csv")}')


if __name__ == '__main__':
    train_and_explain()
