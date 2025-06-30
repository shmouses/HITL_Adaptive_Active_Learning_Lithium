"""
Data Loader Module

This module provides utilities for loading and processing experimental data
from the Data directory in the HITL-AL framework.
"""

import os
import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Tuple
from .data_processing import sift_data_extractor, successful_sift_extraction


def load_cleaned_data(data_dir: str = "Data/clean") -> pd.DataFrame:
    """
    Load all cleaned experimental data from the clean data directory.
    
    Parameters:
    -----------
    data_dir : str, default="Data/clean"
        Path to the cleaned data directory
        
    Returns:
    --------
    pd.DataFrame
        Combined cleaned dataset
        
    Notes:
    ------
    This function loads all CSV files from the clean data directory
    and combines them into a single DataFrame for analysis.
    """
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")
    
    data_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    if not data_files:
        raise FileNotFoundError(f"No CSV files found in {data_dir}")
    
    combined_data = []
    
    for file in data_files:
        file_path = os.path.join(data_dir, file)
        try:
            data = pd.read_csv(file_path)
            data['source_file'] = file  # Track source file
            combined_data.append(data)
            print(f"Loaded {file}: {len(data)} experiments")
        except Exception as e:
            print(f"Error loading {file}: {e}")
    
    if not combined_data:
        raise ValueError("No data could be loaded from any files")
    
    # Combine all datasets
    final_data = pd.concat(combined_data, ignore_index=True)
    print(f"\nTotal experiments loaded: {len(final_data)}")
    
    return final_data


def load_raw_data(data_dir: str = "Data/raw") -> Dict[str, pd.DataFrame]:
    """
    Load raw experimental data from Excel files.
    
    Parameters:
    -----------
    data_dir : str, default="Data/raw"
        Path to the raw data directory
        
    Returns:
    --------
    Dict[str, pd.DataFrame]
        Dictionary mapping filenames to DataFrames
        
    Notes:
    ------
    This function loads all Excel files from the raw data directory
    and returns them as a dictionary for individual processing.
    """
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")
    
    excel_files = [f for f in os.listdir(data_dir) if f.endswith(('.xlsx', '.xls'))]
    if not excel_files:
        raise FileNotFoundError(f"No Excel files found in {data_dir}")
    
    raw_data = {}
    
    for file in excel_files:
        file_path = os.path.join(data_dir, file)
        try:
            data = pd.read_excel(file_path)
            raw_data[file] = data
            print(f"Loaded {file}: {len(data)} experiments")
        except Exception as e:
            print(f"Error loading {file}: {e}")
    
    return raw_data


def load_generated_data(data_dir: str = "Data/generated") -> Dict[str, pd.DataFrame]:
    """
    Load AI-generated experimental designs and results.
    
    Parameters:
    -----------
    data_dir : str, default="Data/generated"
        Path to the generated data directory
        
    Returns:
    --------
    Dict[str, pd.DataFrame]
        Dictionary mapping filenames to DataFrames
        
    Notes:
    ------
    This function loads AI-generated experimental designs, surrogate data,
    and comparative analysis results.
    """
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")
    
    generated_data = {}
    
    # Load CSV files
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    for file in csv_files:
        file_path = os.path.join(data_dir, file)
        try:
            data = pd.read_csv(file_path)
            generated_data[file] = data
            print(f"Loaded {file}: {len(data)} rows")
        except Exception as e:
            print(f"Error loading {file}: {e}")
    
    # Load NPY files (numpy arrays)
    npy_files = [f for f in os.listdir(data_dir) if f.endswith('.npy')]
    for file in npy_files:
        file_path = os.path.join(data_dir, file)
        try:
            data = np.load(file_path)
            generated_data[file] = data
            print(f"Loaded {file}: shape {data.shape}")
        except Exception as e:
            print(f"Error loading {file}: {e}")
    
    # Load files from subdirectories
    for subdir in os.listdir(data_dir):
        subdir_path = os.path.join(data_dir, subdir)
        if os.path.isdir(subdir_path):
            for file in os.listdir(subdir_path):
                if file.endswith(('.csv', '.npy')):
                    file_path = os.path.join(subdir_path, file)
                    try:
                        if file.endswith('.csv'):
                            data = pd.read_csv(file_path)
                        else:
                            data = np.load(file_path)
                        generated_data[f"{subdir}/{file}"] = data
                        print(f"Loaded {subdir}/{file}")
                    except Exception as e:
                        print(f"Error loading {subdir}/{file}: {e}")
    
    return generated_data


def prepare_analysis_dataset(cleaned_data: pd.DataFrame,
                           feature_columns: Optional[List[str]] = None,
                           target_columns: Optional[List[str]] = None) -> Tuple[pd.DataFrame, List[str], List[str]]:
    """
    Prepare dataset for analysis by defining features and targets.
    
    Parameters:
    -----------
    cleaned_data : pd.DataFrame
        Cleaned experimental data
    feature_columns : List[str], optional
        Names of feature columns. If None, uses default features
    target_columns : List[str], optional
        Names of target columns. If None, uses default targets
        
    Returns:
    --------
    Tuple[pd.DataFrame, List[str], List[str]]
        Prepared dataset, feature columns, target columns
        
    Notes:
    ------
    This function prepares the dataset for machine learning analysis
    by defining the feature and target variables.
    """
    # Default feature columns
    if feature_columns is None:
        feature_columns = [
            'T_cold', 'T_hot', 'delta_T', 'flow_rate', 'slurry_concentration',
            'init_Ca', 'init_K', 'init_Li', 'init_Mg', 'init_Na'
        ]
    
    # Default target columns
    if target_columns is None:
        target_columns = ['fini_Mg', 'fini_K', 'fini_Li_purity', 'fini_Ca', 'fini_Na']
    
    # Add delta_T if not present
    if 'delta_T' not in cleaned_data.columns and 'T_cold' in cleaned_data.columns and 'T_hot' in cleaned_data.columns:
        cleaned_data['delta_T'] = cleaned_data['T_hot'] - cleaned_data['T_cold']
    
    # Add battery grade label if not present
    if 'bg' not in cleaned_data.columns and 'fini_Mg' in cleaned_data.columns:
        cleaned_data['bg'] = np.where(cleaned_data['fini_Mg'] < 80, 1, 0)
    
    # Filter to include only available columns
    available_features = [col for col in feature_columns if col in cleaned_data.columns]
    available_targets = [col for col in target_columns if col in cleaned_data.columns]
    
    # Select relevant columns
    analysis_columns = available_features + available_targets
    if 'experiment_id' in cleaned_data.columns:
        analysis_columns.append('experiment_id')
    
    analysis_data = cleaned_data[analysis_columns].copy()
    
    # Remove rows with missing values
    analysis_data = analysis_data.dropna()
    
    print(f"Analysis dataset prepared:")
    print(f"  Features: {available_features}")
    print(f"  Targets: {available_targets}")
    print(f"  Total experiments: {len(analysis_data)}")
    
    return analysis_data, available_features, available_targets


def get_data_summary(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate a comprehensive summary of the dataset.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Dataset to summarize
        
    Returns:
    --------
    Dict[str, Any]
        Summary statistics and information
    """
    summary = {
        'total_experiments': len(data),
        'total_features': len(data.columns),
        'missing_values': data.isnull().sum().to_dict(),
        'data_types': data.dtypes.to_dict(),
        'numeric_columns': data.select_dtypes(include=[np.number]).columns.tolist(),
        'categorical_columns': data.select_dtypes(include=['object']).columns.tolist(),
        'date_columns': data.select_dtypes(include=['datetime']).columns.tolist()
    }
    
    # Add descriptive statistics for numeric columns
    if summary['numeric_columns']:
        summary['descriptive_stats'] = data[summary['numeric_columns']].describe().to_dict()
    
    # Add value counts for categorical columns
    if summary['categorical_columns']:
        summary['categorical_counts'] = {}
        for col in summary['categorical_columns']:
            summary['categorical_counts'][col] = data[col].value_counts().to_dict()
    
    return summary


def print_data_summary(summary: Dict[str, Any]) -> None:
    """
    Print a formatted summary of the dataset.
    
    Parameters:
    -----------
    summary : Dict[str, Any]
        Summary dictionary from get_data_summary()
    """
    print("=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)
    print(f"Total experiments: {summary['total_experiments']}")
    print(f"Total features: {summary['total_features']}")
    
    print(f"\nNumeric features ({len(summary['numeric_columns'])}):")
    for col in summary['numeric_columns']:
        print(f"  - {col}")
    
    print(f"\nCategorical features ({len(summary['categorical_columns'])}):")
    for col in summary['categorical_columns']:
        print(f"  - {col}")
    
    print(f"\nMissing values:")
    missing_data = {k: v for k, v in summary['missing_values'].items() if v > 0}
    if missing_data:
        for col, count in missing_data.items():
            print(f"  - {col}: {count} missing values")
    else:
        print("  - No missing values found")
    
    print("=" * 60) 