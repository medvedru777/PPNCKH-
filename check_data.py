import pandas as pd
try:
    df = pd.read_parquet('data/raw/ember_1k_balanced.parquet')
    print("--- Label stats in data/raw/ember_1k_balanced.parquet ---")
    print(df['label'].value_counts())
    print("------------------------------------------------------")
except Exception as e:
    print(f"Error reading file: {e}")
