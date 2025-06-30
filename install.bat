@echo off
REM HITL Adaptive Active Learning Lithium - Installation Script for Windows
REM This script sets up the environment for reproducing the research

echo 🚀 Setting up HITL Adaptive Active Learning Lithium Environment
echo ================================================================

REM Check if conda is installed
where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Conda is not installed. Please install Anaconda or Miniconda first.
    echo    Download from: https://docs.conda.io/en/latest/miniconda.html
    pause
    exit /b 1
)

REM Check if git is installed
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Git is not installed. Please install Git first.
    pause
    exit /b 1
)

echo ✅ Prerequisites check passed

REM Create conda environment
echo 📦 Creating conda environment...
conda env create -f environment.yml

REM Activate environment
echo 🔄 Activating environment...
call conda activate hitl-lithium

REM Verify installation
echo 🔍 Verifying installation...
python -c "import numpy, pandas, sklearn, optuna, shap, platypus; print('✅ All core packages imported successfully'); print(f'NumPy version: {numpy.__version__}'); print(f'Pandas version: {pandas.__version__}'); print(f'Scikit-learn version: {sklearn.__version__}'); print(f'Optuna version: {optuna.__version__}'); print(f'SHAP version: {shap.__version__}')"

REM Install Jupyter kernel
echo 📓 Installing Jupyter kernel...
python -m ipykernel install --user --name=hitl-lithium --display-name="HITL Lithium"

echo.
echo 🎉 Installation completed successfully!
echo ================================================================
echo.
echo To get started:
echo 1. Activate the environment: conda activate hitl-lithium
echo 2. Launch Jupyter: jupyter notebook
echo 3. Open Paper_Reproduction.ipynb
echo.
echo For more information, see the README.md file.
echo.
pause 