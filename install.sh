#!/bin/bash

# HITL Adaptive Active Learning Lithium - Installation Script
# This script sets up the environment for reproducing the research

set -e  # Exit on any error

echo "🚀 Setting up HITL Adaptive Active Learning Lithium Environment"
echo "================================================================"

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "❌ Conda is not installed. Please install Anaconda or Miniconda first."
    echo "   Download from: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

echo "✅ Prerequisites check passed"

# Create conda environment
echo "📦 Creating conda environment..."
conda env create -f environment.yml

# Activate environment
echo "🔄 Activating environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate hitl-lithium

# Verify installation
echo "🔍 Verifying installation..."
python -c "
import numpy, pandas, sklearn, optuna, shap, platypus
print('✅ All core packages imported successfully')
print(f'NumPy version: {numpy.__version__}')
print(f'Pandas version: {pandas.__version__}')
print(f'Scikit-learn version: {sklearn.__version__}')
print(f'Optuna version: {optuna.__version__}')
print(f'SHAP version: {shap.__version__}')
"

# Install Jupyter kernel
echo "📓 Installing Jupyter kernel..."
python -m ipykernel install --user --name=hitl-lithium --display-name="HITL Lithium"

echo ""
echo "🎉 Installation completed successfully!"
echo "================================================================"
echo ""
echo "To get started:"
echo "1. Activate the environment: conda activate hitl-lithium"
echo "2. Launch Jupyter: jupyter notebook"
echo "3. Open Paper_Reproduction.ipynb"
echo ""
echo "For more information, see the README.md file."
echo "" 