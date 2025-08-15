# 03_visualization.py
import matplotlib.pyplot as plt

def forest_plot(estimates, ci_low, ci_high, labels, title):
    """Generate publication-ready forest plot"""
    plt.figure(figsize=(10,6))
    y_pos = range(len(estimates))
    
    plt.errorbar(estimates, y_pos, 
                 xerr=[estimates-ci_low, ci_high-estimates],
                 fmt='o', capsize=5)
    
    plt.yticks(y_pos, labels)
    plt.axvline(x=1, color='grey', ls='--')  # Null line
    plt.title(title)
    plt.tight_layout()
    return plt