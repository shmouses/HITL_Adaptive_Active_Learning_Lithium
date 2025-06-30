"""
HITL Adaptive Active Learning Lithium - Scripts Package

This package contains utility functions and modules for the HITL-AL framework.
"""

__version__ = "1.0.0"
__author__ = "Shayan Mousavi Masouleh"
__email__ = "shayan.mousavi@nrc-cnrc.gc.ca"

from .data_processing import (
    sift_data_extractor,
    successful_sift_extraction,
    ppm_threshold
)

from .surrogate_generation import (
    latin_hypercube_sample,
    uniform_random_sample,
    sift_lhs_sample
)

from .statistical_analysis import (
    tune_hyperparameters,
    train_model,
    shap_feature_importance,
    plot_data_analysis,
    plot_partial_dependence,
    plot_mutual_information,
    sensitivity_analysis,
    perform_full_analysis,
    find_missing_data
)

from .pareto_optimization import (
    optimize_pareto_front
)

__all__ = [
    # Data processing
    'sift_data_extractor',
    'successful_sift_extraction', 
    'ppm_threshold',
    
    # Surrogate generation
    'latin_hypercube_sample',
    'uniform_random_sample',
    'sift_lhs_sample',
    
    # Statistical analysis
    'tune_hyperparameters',
    'train_model',
    'shap_feature_importance',
    'plot_data_analysis',
    'plot_partial_dependence',
    'plot_mutual_information',
    'sensitivity_analysis',
    'perform_full_analysis',
    'find_missing_data',
    
    # Pareto optimization
    'optimize_pareto_front'
] 