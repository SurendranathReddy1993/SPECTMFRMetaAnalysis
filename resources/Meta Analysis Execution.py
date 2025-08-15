# 02_meta_analysis.py
from scipy.stats import norm
import numpy as np

def calculate_metrics(df):
    """Compute diagnostic metrics with Delta method CIs"""
    df['Sensitivity'] = df['TP']/(df['TP']+df['FN'])
    df['Specificity'] = df['TN']/(df['TN']+df['FP'])
    
    # Delta method implementation
    df['SE_logPLR'] = np.sqrt(
        (1-df['Sensitivity'])/(df['Sensitivity']*(df['TP']+df['FN'])) + 
        df['Specificity']/((1-df['Specificity'])*(df['TN']+df['FP']))
    )
    return df