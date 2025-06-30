"""
Data Processing Module

This module contains functions for extracting, cleaning, and processing 
experimental data from SIFT (Selective Ion Flotation Technology) experiments.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, Optional


def sift_data_extractor(data: pd.DataFrame, 
                       ppm: bool = True, 
                       pH: bool = False, 
                       slurry: bool = False, 
                       score: bool = False, 
                       NaOH: bool = False) -> pd.DataFrame:
    """
    Extract and standardize experimental data from raw SIFT files.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Raw experimental data from SIFT experiments
    ppm : bool, default=True
        If True, extract concentration data in ppm units
    pH : bool, default=False
        If True, include pH measurements
    slurry : bool, default=False
        If True, include individual slurry component concentrations
    score : bool, default=False
        If True, include expert-assigned quality scores
    NaOH : bool, default=False
        If True, include NaOH addition data
        
    Returns:
    --------
    pd.DataFrame
        Standardized dataset with consistent column names and data types
        
    Notes:
    ------
    This function handles the conversion from raw experimental data format
    to a standardized format suitable for machine learning analysis.
    """
    new_data = pd.DataFrame()
    
    # Extract basic experiment information
    if 'Experiment ID' in data.columns:
        new_data['experiment_id'] = data['Experiment ID']
    if 'Successful Experiment' in data.columns:
        new_data['success'] = data['Successful Experiment']
    else:
        new_data['success'] = 'T'
    
    # Extract quality scores if requested
    if score:
        if 'Success score' in data.columns:
            new_data['score'] = data['Success score']
        else:
            new_data['score'] = 1
    
    # Extract process parameters
    if 'T cold (deg C)' in data.columns:
        new_data['T_cold'] = data['T cold (deg C)'].astype(float)
    if 'T hot (deg C)' in data.columns:
        new_data['T_hot'] = data['T hot (deg C)'].astype(float)
    if 'flow rate (mL/min)' in data.columns:
        new_data['flow_rate'] = data['flow rate (mL/min)'].astype(float)
    if 'slurry concentration (g total solid/100 mL)' in data.columns:
        new_data['slurry_concentration'] = data['slurry concentration (g total solid/100 mL)'].astype(float)
    
    # Extract pH data if requested
    if pH and 'pH of slurry (initial)' in data.columns:
        new_data['pH'] = data['pH of slurry (initial)'].astype(float)
    
    # Extract NaOH data if requested
    if NaOH and 'millimoles NaOH added' in data.columns:
        new_data['NaOH'] = data['millimoles NaOH added'].astype(float)
    
    # Extract slurry component concentrations if requested
    if slurry:
        slurry_components = {
            'slurry concentration (g CaCO3/100 mL)': 'scl_Ca',
            'slurry concentration (g K2CO3/100 mL)': 'scl_K',
            'slurry concentration (g Li2CO3/100 mL)': 'scl_Li',
            'slurry concentration (g (Mg(CO3))4 Mg(OH)2/100 mL)': 'scl_Mg',
            'slurry concentration (g Na2CO3/100 mL)': 'scl_Na',
            'slurry concentration (g SrCO3/100 mL)': 'scl_Sr'
        }
        for column, new_column_name in slurry_components.items():
            if column in data.columns:
                new_data[new_column_name] = data[column].astype(float)
    
    # Extract concentration data (ppm or percentage)
    if ppm:
        ppm_components = {
            'B (ppm)': 'init_B', 'Ca (ppm)': 'init_Ca', 'K (ppm)': 'init_K',
            'Li (ppm)': 'init_Li', 'Mg (ppm)': 'init_Mg', 'Na (ppm)': 'init_Na',
            'Si (ppm)': 'init_Si', 'Sr (ppm)': 'init_Sr', 'Li2CO3 purity (%)': 'init_Li_purity',
            'B (ppm).1': 'fini_B', 'Ca (ppm).1': 'fini_Ca', 'K (ppm).1': 'fini_K',
            'Li (ppm).1': 'fini_Li', 'Mg (ppm).1': 'fini_Mg', 'Na (ppm).1': 'fini_Na',
            'Si (ppm).1': 'fini_Si', 'Sr (ppm).1': 'fini_Sr', 'Li2CO3 purity (%).1': 'fini_Li_purity'
        }
        for column, new_column_name in ppm_components.items():
            if column in data.columns:
                new_data[new_column_name] = data[column].astype(float)
    else:
        percentage_components = {
            'B (%)': 'init_B', 'Ca (%)': 'init_Ca', 'K (%)': 'init_K', 'Li (%)': 'init_Li',
            'Mg (%)': 'init_Mg', 'Na (%)': 'init_Na', 'Si (%)': 'init_Si', 'Sr (%)': 'init_Sr',
            'B (%).1': 'fini_B', 'Ca (%).1': 'fini_Ca', 'K (%).1': 'fini_K', 'Li (%).1': 'fini_Li',
            'Mg (%).1': 'fini_Mg', 'Na (%).1': 'fini_Na', 'Si (%).1': 'fini_Si', 'Sr (%).1': 'fini_Sr'
        }
        for column, new_column_name in percentage_components.items():
            if column in data.columns:
                new_data[new_column_name] = data[column].astype(float)
    
    return new_data


def successful_sift_extraction(data: pd.DataFrame) -> pd.DataFrame:
    """
    Filter SIFT experimental data to include only successful experiments.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Experimental data with success indicators
        
    Returns:
    --------
    pd.DataFrame
        Filtered dataset containing only successful experiments
        
    Notes:
    ------
    This function is essential for model training as it ensures only
    high-quality experimental data is used for machine learning analysis.
    """
    new_data = data[data['success'].isin(['T'])].copy()
    return new_data


def ppm_threshold(element: str) -> Optional[int]:
    """
    Get the battery-grade threshold for each element in ppm.
    
    Parameters:
    -----------
    element : str
        Element name (e.g., 'fini_Ca', 'fini_Mg', etc.)
        
    Returns:
    --------
    int or None
        Battery-grade threshold in ppm, or None if element not found
        
    Notes:
    ------
    These thresholds are based on industry standards for battery-grade
    lithium carbonate specifications.
    """
    fini_threshold = {
        'fini_Ca': 160,
        'fini_K': 10,
        'fini_Mg': 80,
        'fini_Na': 500,
        'fini_Si': 40
    }
    return fini_threshold.get(element) 