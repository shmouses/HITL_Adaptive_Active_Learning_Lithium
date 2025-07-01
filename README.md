# Human-AI Synergy in Adaptive Active Learning for Lithium Carbonate Crystallization Optimization

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-TBA-blue.svg)](TBA)

## 📋 Table of Contents

- [Overview](#overview)
- [Research Context](#research-context)
- [Key Findings](#key-findings)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Results](#results)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)
- [Contact](#contact)

## 🔬 Overview

This repository contains the complete implementation and supplementary materials for the research paper **"Human-AI Synergy in Adaptive Active Learning for Continuous Lithium Carbonate Crystallization Optimization"** published in *npj Computational Materials*.

Our research demonstrates a novel Human-in-the-Loop Active Learning (HITL-AL) framework that significantly accelerates the optimization of continuous lithium carbonate crystallization from low-grade brines. The framework combines human expertise with AI-driven exploration to discover optimal process conditions for producing battery-grade lithium carbonate.

## 🎯 Research Context

Lithium carbonate ($Li_2CO_3$) is a critical component in lithium-ion batteries, essential for electric vehicles and renewable energy storage. Traditional crystallization processes face significant challenges with:

- **Impurity tolerance**: Managing calcium, magnesium, and other impurities
- **Process optimization**: Balancing yield, purity, and energy efficiency  
- **Resource utilization**: Maximizing extraction from low-grade sources like the Smackover Formation

Our HITL-AL framework addresses these challenges by:
1. **Data-driven exploration** using Pareto frontier analysis
2. **AI-guided exploitation** through Gaussian Process Classification
3. **Human expertise integration** for experimental validation
4. **Adaptive learning** for continuous process improvement

## 🏆 Key Findings

- **Accelerated Discovery**: Achieved battery-grade lithium carbonate in only 38 experiments
- **Critical Parameter Discovery**: Identified the counterintuitive role of cold reactor temperature in magnesium removal
- **Impurity Tolerance**: Findings resulted in increased tolerance to magnesium impurities by 3.5x compared to baseline methods

## 📁 Repository Structure

```
HITL_Adaptive_Active_Learning_Lithium/
├── README.md                           # This file
├── environment.yml                     # Conda environment specification
├── requirements.txt                    # Python package requirements
├── setup.py                           # Package installation script
├── LICENSE                            # MIT License
├── install.sh                         # Unix/Linux installation script
├── install.bat                        # Windows installation script
├── Dockerfile                         # Docker container configuration
├── .dockerignore                      # Docker ignore file
├── .gitignore                         # Git ignore file
├── Paper_Reproduction.ipynb           # Main Jupyter notebook with complete analysis
├── scripts/                           # Utility scripts and modules
│   ├── __init__.py                    # Package initialization
│   ├── main.py                        # Main analysis pipeline demonstration
│   ├── data_loader.py                 # Data loading utilities
│   ├── data_processing.py             # Data extraction and cleaning functions
│   ├── surrogate_generation.py        # Latin Hypercube Sampling functions
│   ├── statistical_analysis.py        # ML model training and analysis
│   └── pareto_optimization.py         # Multi-objective optimization functions
├── Data/                              # Experimental and generated data
│   ├── clean/                         # Cleaned experimental data (CSV/XLSX files)
│   │   
│   ├── raw/                           # Raw experimental data (Excel files)
│   │   
│   └── generated/                     # AI-generated experimental designs
│       
│       
└── docs/                              # Documentation
    └── installation_guide.md          # Detailed installation instructions
```

## 🚀 Installation

### Prerequisites

- **Python**: 3.9 or higher
- **Conda**: Anaconda or Miniconda
- **Git**: For cloning the repository

### Option 1: Conda Environment (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/HITL_Adaptive_Active_Learning_Lithium.git
   cd HITL_Adaptive_Active_Learning_Lithium
   ```

2. **Create and activate the conda environment**:
   ```bash
   conda env create -f environment.yml
   conda activate hitl-lithium
   ```

3. **Verify installation**:
   ```bash
   python -c "import numpy, pandas, sklearn, optuna; print('Installation successful!')"
   ```

### Option 2: Manual Installation

1. **Create a new conda environment**:
   ```bash
   conda create -n hitl-lithium python=3.9
   conda activate hitl-lithium
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Jupyter and additional dependencies**:
   ```bash
   conda install jupyter notebook
   ```

### Option 3: Docker (Alternative)

```bash
# Build the Docker image
docker build -t hitl-lithium .

# Run the container with Jupyter
docker run -p 8888:8888 -v $(pwd):/workspace hitl-lithium
```

## 📖 Usage

### Quick Start

#### Option 1: Jupyter Notebook (Recommended for Exploration)

1. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Open the main notebook**:
   - Navigate to `Paper_Reproduction.ipynb`
   - This notebook contains the complete analysis pipeline

3. **Run the analysis**:
   - Execute cells sequentially from top to bottom
   - The notebook is self-contained and includes all necessary functions

#### Option 2: Scripts Package (Recommended for Production)

1. **Run the complete analysis pipeline**:
   ```bash
   python scripts/main.py
   ```

2. **Use individual modules**:
   ```python
   from scripts.data_loader import load_cleaned_data
   from scripts.statistical_analysis import perform_full_analysis
   
   # Load and analyze data
   data = load_cleaned_data()
   perform_full_analysis(data, features, targets)
   ```

### Detailed Workflow

#### Jupyter Notebook Workflow

The notebook follows the HITL-AL framework with these main sections:

1. **Setup and Configuration** (Cells 0-5)
   - Library imports and environment configuration
   - Version verification for reproducibility

2. **Auxiliary Functions** (Cells 6-15)
   - Data processing and extraction functions
   - Statistical analysis and visualization tools
   - Optimization algorithms (NSGA-II, Pareto frontier)

3. **Data Loading and Preparation** (Cells 16-25)
   - Experimental data loading from SIFT experiments
   - Data cleaning and preprocessing
   - Progressive dataset preparation

4. **Data and Results Inspection** (Cells 26-30)
   - Comprehensive statistical analysis
   - Feature importance analysis
   - Correlation studies

5. **Exploration Phase** (Cells 31-45)
   - Pareto frontier analysis using GPR and NSGA-II
   - Multi-objective optimization for impurity minimization

6. **Human-in-the-Loop Insights** (Cells 46-55)
   - Random walk analysis revealing critical parameters
   - Cold reactor temperature discovery

7. **Exploitation Phase** (Cells 56-65)
   - Gaussian Process Classification for decision boundaries
   - Ray tracing for optimal experiment selection

8. **Final Results and Analysis** (Cells 66-75)
   - Model performance evaluation
   - Parameter distribution analysis

9. **Comparative Simulation** (Cells 76-90)
   - Performance comparison with automated methods
   - Statistical validation of HITL-AL benefits

#### Scripts Package Workflow

The modular scripts package provides the same functionality in a more organized way:

1. **Data Loading** (`scripts/data_loader.py`)
   - `load_cleaned_data()`: Load all cleaned experimental data
   - `load_raw_data()`: Load raw Excel files
   - `prepare_analysis_dataset()`: Prepare data for ML analysis

2. **Data Processing** (`scripts/data_processing.py`)
   - `sift_data_extractor()`: Extract and standardize SIFT data
   - `successful_sift_extraction()`: Filter successful experiments
   - `ppm_threshold()`: Get battery-grade thresholds

3. **Surrogate Generation** (`scripts/surrogate_generation.py`)
   - `sift_lhs_sample()`: Generate Latin Hypercube samples
   - `latin_hypercube_sample()`: Core LHS implementation
   - `uniform_random_sample()`: Random sampling baseline

4. **Statistical Analysis** (`scripts/statistical_analysis.py`)
   - `tune_hyperparameters()`: Optuna-based optimization
   - `perform_full_analysis()`: Complete analysis pipeline
   - `shap_feature_importance()`: SHAP analysis
   - `plot_data_analysis()`: Visualization functions

5. **Pareto Optimization** (`scripts/pareto_optimization.py`)
   - `optimize_pareto_front()`: NSGA-II multi-objective optimization

### Running Individual Components

#### Complete Pipeline

```bash
# Run the complete analysis pipeline
python scripts/main.py
```

#### Individual Modules

```python
# Data loading and preparation
from scripts.data_loader import load_cleaned_data, prepare_analysis_dataset
cleaned_data = load_cleaned_data()
analysis_data, features, targets = prepare_analysis_dataset(cleaned_data)

# Statistical analysis
from scripts.statistical_analysis import perform_full_analysis, tune_hyperparameters
perform_full_analysis(analysis_data, features, targets)

# Surrogate generation
from scripts.surrogate_generation import sift_lhs_sample
surrogate_data = sift_lhs_sample(n_points=1000, seed=42)

# Pareto optimization
from scripts.pareto_optimization import optimize_pareto_front
pareto_front, pareto_data = optimize_pareto_front(surrogate_data)
```

#### Command Line Examples

```bash
# Run individual module demonstrations
python -c "from scripts import data_loader; print('Data loader module imported successfully')"

# Interactive Python session
python -c "
from scripts.data_loader import load_cleaned_data
from scripts.statistical_analysis import get_data_summary, print_data_summary

data = load_cleaned_data()
summary = get_data_summary(data)
print_data_summary(summary)
"
```

### Using the Scripts Package

The `scripts/` directory contains modular Python packages organized by functionality:

#### **Core Modules**

- **`data_loader.py`**: Data loading and preparation utilities
  - `load_cleaned_data()`: Load all cleaned experimental data
  - `load_raw_data()`: Load raw Excel files  
  - `prepare_analysis_dataset()`: Prepare data for ML analysis
  - `get_data_summary()`: Generate comprehensive data summaries

- **`data_processing.py`**: SIFT data extraction and cleaning
  - `sift_data_extractor()`: Extract and standardize experimental data
  - `successful_sift_extraction()`: Filter successful experiments
  - `ppm_threshold()`: Get battery-grade thresholds

- **`surrogate_generation.py`**: Experimental design and sampling
  - `sift_lhs_sample()`: Generate validated experimental designs
  - `latin_hypercube_sample()`: Core LHS implementation
  - `uniform_random_sample()`: Random sampling baseline

#### **Analysis Modules**

- **`statistical_analysis.py`**: Machine learning and statistical analysis
  - `tune_hyperparameters()`: Optuna-based hyperparameter optimization
  - `perform_full_analysis()`: Complete analysis pipeline
  - `shap_feature_importance()`: SHAP analysis for feature importance
  - `plot_data_analysis()`: Comprehensive visualization functions
  - `sensitivity_analysis()`: Model sensitivity analysis

- **`pareto_optimization.py`**: Multi-objective optimization
  - `optimize_pareto_front()`: NSGA-II Pareto frontier extraction

#### **Utility Modules**

- **`main.py`**: Complete analysis pipeline demonstration
  - `main()`: Full HITL-AL analysis pipeline
  - `demo_individual_modules()`: Individual module demonstrations

- **`__init__.py`**: Package initialization and imports

#### **Advanced Usage Examples**

```python
# Custom analysis pipeline
from scripts.data_loader import load_cleaned_data, prepare_analysis_dataset
from scripts.statistical_analysis import tune_hyperparameters, train_model, shap_feature_importance
from scripts.surrogate_generation import sift_lhs_sample
from scripts.pareto_optimization import optimize_pareto_front

# 1. Load and prepare data
cleaned_data = load_cleaned_data()
analysis_data, features, targets = prepare_analysis_dataset(cleaned_data)

# 2. Train custom model
best_params = tune_hyperparameters(analysis_data[features], analysis_data['fini_Mg'])
model = train_model(analysis_data[features], analysis_data['fini_Mg'], best_params)

# 3. Generate surrogate space
surrogate_data = sift_lhs_sample(n_points=10000, seed=42)

# 4. Perform Pareto optimization
pareto_front, pareto_data = optimize_pareto_front(
    surrogate_data, 
    obj1_col="fini_Mg", 
    obj2_col="fini_Ca",
    min_unique_points=50
)

# 5. Analyze results
shap_feature_importance(model, analysis_data[features])
```

### Benefits of the Modular Approach

The scripts package provides several advantages over the notebook-only approach:

#### **🔧 Maintainability**
- **Separation of Concerns**: Each module handles a specific aspect of the analysis
- **Easy Updates**: Modify individual functions without affecting others
- **Version Control**: Track changes to specific functionality

#### **🚀 Reusability**
- **Import Anywhere**: Use functions in other projects or scripts
- **Custom Pipelines**: Build your own analysis workflows
- **API Development**: Functions can serve as building blocks for APIs

#### **🧪 Testing**
- **Unit Testing**: Test individual functions in isolation
- **Integration Testing**: Test complete workflows
- **Regression Testing**: Ensure changes don't break existing functionality

#### **📊 Production Ready**
- **Error Handling**: Robust error handling and validation
- **Logging**: Built-in logging for debugging and monitoring
- **Documentation**: Comprehensive docstrings and type hints

#### **👥 Collaboration**
- **Code Review**: Easier to review specific modules
- **Parallel Development**: Multiple developers can work on different modules
- **Code Sharing**: Share specific functionality with other projects

## 📊 Data

### Experimental Data

The repository includes experimental data from SIFT (Selective Ion Flotation Technology) experiments:

- **Raw Data**: Original experimental measurements
- **Clean Data**: Processed and validated experimental results
- **Generated Data**: AI-suggested experimental conditions


### Data Access

The data files are included in the repository under the `Data/` directory. For large datasets, consider using Git LFS or downloading from the provided data repository.


### Reproducing Results

#### Option 1: Jupyter Notebook
1. Run the complete notebook `Paper_Reproduction.ipynb`
2. Key results are automatically generated and displayed
3. Figures are saved in the notebook output
4. Statistical summaries are printed during execution

#### Option 2: Scripts Package
1. Run the complete pipeline: `python scripts/main.py`
2. Use individual modules for specific analyses
3. Customize the analysis workflow as needed
4. Generate reproducible results programmatically

### Expected Outputs

The analysis generates several key outputs:

- **Pareto Frontier Plots**: Multi-objective optimization results
- **Feature Importance Analysis**: SHAP and mutual information plots
- **Decision Boundary Maps**: GPC classification results
- **Comparative Analysis**: Performance comparison plots
- **Statistical Summaries**: Model performance metrics

### Choosing Your Approach

#### **Use Jupyter Notebook When:**
- 🔍 **Exploring the data** for the first time
- 📚 **Learning the methodology** step by step
- 🎯 **Quick prototyping** and experimentation
- 📊 **Interactive visualization** and analysis
- 👥 **Educational purposes** or presentations

#### **Use Scripts Package When:**
- 🏭 **Production environments** and automated workflows
- 🔄 **Repetitive analysis** with different datasets
- 🧪 **Custom analysis pipelines** and modifications
- 📈 **Batch processing** multiple experiments
- 🤝 **Collaborative development** and code sharing
- 🚀 **Integration** with other systems or APIs

## 🤝 Contributing

We welcome contributions to improve this research and make it more accessible to the community.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests if applicable
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Development Setup

For developers who want to contribute:

```bash
# Clone and setup development environment
git clone https://github.com/your-username/HITL_Adaptive_Active_Learning_Lithium.git
cd HITL_Adaptive_Active_Learning_Lithium

# Create development environment
conda env create -f environment-dev.yml
conda activate hitl-lithium-dev

# Install development dependencies
pip install -e .
```

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to all functions
- Include type hints where appropriate
- Write tests for new functionality

## 📚 Citation

If you use this code in your research, please cite our paper:

```bibtex
@article{mousavi2025human,
  title={Human-AI Synergy in Adaptive Active Learning for Continuous Lithium Carbonate Crystallization Optimization},
  author={Mousavi Masouleh, Shayan and Sanz, Corey A. and Jansonius, Ryan P. and Cronin, Cara and Hein, Jason E. and Hattrick-Simpers, Jason},
  journal={},
  volume={},
  number={},
  pages={},
  year={},
  publisher={},
  doi={}
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License allows you to:
- Use the code commercially
- Modify the code
- Distribute the code
- Use it privately
- Sublicense it

## 📧 Contact

For questions, suggestions, or collaboration opportunities:

- **Lead Author**: Shayan Mousavi Masouleh
- **Corresponding Author**: Jason Hattrick-Simpers

