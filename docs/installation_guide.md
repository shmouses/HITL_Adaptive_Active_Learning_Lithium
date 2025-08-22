# Installation Guide

This guide provides detailed instructions for setting up the HITL Adaptive Active Learning Lithium research environment on different operating systems.

## Prerequisites

Before installing the project, ensure you have the following prerequisites:

### Required Software

1. **Python 3.8 or higher**
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **Conda (Anaconda or Miniconda)**
   - Download from [conda.io](https://docs.conda.io/en/latest/miniconda.html)
   - Verify installation: `conda --version`

3. **Git**
   - Download from [git-scm.com](https://git-scm.com/)
   - Verify installation: `git --version`

### System Requirements

- **RAM**: Minimum 8GB, Recommended 16GB
- **Storage**: At least 5GB free space
- **CPU**: Multi-core processor recommended for faster computation

## Installation Methods

### Method 1: Automated Installation (Recommended)

#### Windows
1. Download the repository:
   ```bash
   git clone https://github.com/your-username/HITL_Adaptive_Active_Learning_Lithium.git
   cd HITL_Adaptive_Active_Learning_Lithium
   ```

2. Run the installation script:
   ```bash
   install.bat
   ```

#### macOS/Linux
1. Download the repository:
   ```bash
   git clone https://github.com/your-username/HITL_Adaptive_Active_Learning_Lithium.git
   cd HITL_Adaptive_Active_Learning_Lithium
   ```

2. Make the script executable and run it:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

### Method 2: Manual Conda Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/HITL_Adaptive_Active_Learning_Lithium.git
   cd HITL_Adaptive_Active_Learning_Lithium
   ```

2. **Create the conda environment**:
   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the environment**:
   ```bash
   conda activate hitl-lithium
   ```

4. **Verify installation**:
   ```bash
   python -c "import numpy, pandas, sklearn, optuna, shap, platypus; print('Installation successful')"
   ```

### Method 3: Manual Pip Installation

1. **Create a new conda environment**:
   ```bash
   conda create -n hitl-lithium python=3.9
   conda activate hitl-lithium
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Jupyter**:
   ```bash
   conda install jupyter notebook matplotlib seaborn
   ```

### Method 4: Docker Installation

1. **Build the Docker image**:
   ```bash
   docker build -t hitl-lithium .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8888:8888 -v $(pwd):/workspace hitl-lithium
   ```

3. **Access Jupyter**:
   - Open your browser and go to `http://localhost:8888`
   - The notebook will be available in the workspace

## Post-Installation Setup

### 1. Verify Installation

Run the verification script to ensure all components are working:

```bash
python -c "
import numpy as np
import pandas as pd
import sklearn
import optuna
import shap
import platypus
import matplotlib.pyplot as plt
import seaborn as sns
import jupyter

print('✅ All packages imported successfully')
print(f'NumPy: {np.__version__}')
print(f'Pandas: {pd.__version__}')
print(f'Scikit-learn: {sklearn.__version__}')
print(f'Optuna: {optuna.__version__}')
print(f'SHAP: {shap.__version__}')
print(f'Platypus: {platypus.__version__}')
"
```

### 2. Install Jupyter Kernel

```bash
python -m ipykernel install --user --name=hitl-lithium --display-name="HITL Lithium"
```

### 3. Test Jupyter

```bash
jupyter notebook
```

Navigate to `Paper_Reproduction.ipynb` and run the first few cells to verify everything works.

## Troubleshooting

### Common Issues

#### 1. Conda Environment Creation Fails

**Error**: `Solving environment: failed with repodata from current_repodata.json`

**Solution**:
```bash
conda clean --all
conda update conda
conda env create -f environment.yml
```

#### 2. Package Import Errors

**Error**: `ModuleNotFoundError: No module named 'platypus'`

**Solution**:
```bash
conda activate hitl-lithium
pip install platypus-opt==1.0.4
```

#### 3. Jupyter Kernel Issues

**Error**: Kernel not found

**Solution**:
```bash
conda activate hitl-lithium
python -m ipykernel install --user --name=hitl-lithium --display-name="HITL Lithium"
jupyter kernelspec list
```

#### 4. Memory Issues

**Error**: Out of memory during computation

**Solution**:
- Close other applications
- Reduce batch sizes in the notebook
- Use smaller datasets for testing

#### 5. File Path Issues (Windows)

**Error**: File not found

**Solution**:
- Use forward slashes in paths: `Data/clean/` instead of `Data\clean\`
- Or use `os.path.join()` for cross-platform compatibility

### Platform-Specific Issues

#### Windows

1. **PowerShell Execution Policy**:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. **Path Length Issues**:
   - Use shorter directory names
   - Enable long path support in Windows

#### macOS

1. **Permission Issues**:
   ```bash
   chmod +x install.sh
   ```

2. **Homebrew Conflicts**:
   - Use conda instead of pip when possible
   - Avoid mixing package managers

#### Linux

1. **Missing Dependencies**:
   ```bash
   sudo apt-get update
   sudo apt-get install build-essential python3-dev
   ```

2. **Display Issues**:
   ```bash
   export DISPLAY=:0
   ```

## Getting Started

After successful installation:

1. **Activate the environment**:
   ```bash
   conda activate hitl-lithium
   ```

2. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

3. **Open the main notebook**:
   - Navigate to `Paper_Reproduction.ipynb`
   - Run cells sequentially from top to bottom

4. **Follow the analysis**:
   - The notebook is self-contained
   - Each section builds on previous results
   - Key findings are highlighted throughout

## Support

If you encounter issues not covered in this guide:

1. Check the [GitHub Issues](https://github.com/your-username/HITL_Adaptive_Active_Learning_Lithium/issues)
2. Create a new issue with:
   - Operating system and version
   - Python and conda versions
   - Complete error message
   - Steps to reproduce the issue

## Uninstallation

To remove the environment:

```bash
conda deactivate
conda env remove -n hitl-lithium
```

To remove the Jupyter kernel:

```bash
jupyter kernelspec remove hitl-lithium
``` 