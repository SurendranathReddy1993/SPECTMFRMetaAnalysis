# Diagnostic Test Accuracy Meta-Analysis Workflow

## 📌 Project Overview
Systematic review and meta-analysis of cardiac imaging diagnostic performance using Python statistical packages.
# Diagnostic Test Accuracy Meta-Analysis

![Meta-Analysis Workflow](https://img.shields.io/badge/Workflow-Statistical_Analysis-blue)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-green)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A complete Python workflow for conducting diagnostic test accuracy meta-analyses, including statistical synthesis and visualization of sensitivity, specificity, likelihood ratios, and diagnostic odds ratios.

## 📌 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Workflow](#-workflow)
- [File Structure](#-file-structure)
- [Usage](#-usage)
- [Methodology](#-methodology)
- [Outputs](#-outputs)
- [License](#-license)
- [Citation](#-citation)

## ✨ Features
- **Complete statistical pipeline** from raw data to publication-ready figures
- **Random-effects meta-analysis** using DerSimonian-Laird method
- **Delta method implementation** for accurate confidence intervals
- **Automated quality checks** for data validation
- **Reproducible research** with version control support
- **Multiple visualization options** (forest plots, SROC)

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
```bash
# Clone repository
git clone https://github.com/SurendranathReddy1993/SPECTMFRMetaAnalysis.git
cd diagnostic-meta-analysis

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
