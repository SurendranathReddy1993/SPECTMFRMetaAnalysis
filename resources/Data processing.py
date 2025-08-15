# 01_data_processing.py
import pandas as pd

def load_studies(filepath):
    """Load and validate study data"""
    df = pd.read_csv(filepath)
    required_cols = ['Study','TP','FP','FN','TN']
    assert all(col in df.columns for col in required_cols)
    return df

# Example usage:
# studies = load_studies('../data/raw_studies.csv')