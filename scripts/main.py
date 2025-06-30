"""
Main Script for HITL Adaptive Active Learning Lithium

This script demonstrates how to use all the modules in the scripts package
to perform a complete analysis of the lithium carbonate crystallization data.
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Add the parent directory to the path so we can import from scripts
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.data_loader import (
    load_cleaned_data, 
    load_raw_data, 
    load_generated_data,
    prepare_analysis_dataset,
    get_data_summary,
    print_data_summary
)
from scripts.data_processing import (
    sift_data_extractor,
    successful_sift_extraction,
    ppm_threshold
)
from scripts.surrogate_generation import (
    latin_hypercube_sample,
    uniform_random_sample,
    sift_lhs_sample
)
from scripts.statistical_analysis import (
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
from scripts.pareto_optimization import optimize_pareto_front


def main():
    """
    Main function demonstrating the complete HITL-AL analysis pipeline.
    """
    print("=" * 80)
    print("HITL ADAPTIVE ACTIVE LEARNING LITHIUM - ANALYSIS PIPELINE")
    print("=" * 80)
    
    try:
        # Step 1: Load Data
        print("\n1. LOADING EXPERIMENTAL DATA")
        print("-" * 40)
        
        # Load cleaned data
        print("Loading cleaned experimental data...")
        cleaned_data = load_cleaned_data()
        
        # Generate data summary
        summary = get_data_summary(cleaned_data)
        print_data_summary(summary)
        
        # Step 2: Prepare Analysis Dataset
        print("\n2. PREPARING ANALYSIS DATASET")
        print("-" * 40)
        
        analysis_data, feature_columns, target_columns = prepare_analysis_dataset(cleaned_data)
        
        # Add random feature for baseline comparison
        analysis_data['random'] = np.random.random(size=len(analysis_data))
        feature_columns_with_random = feature_columns + ['random']
        
        print(f"Analysis dataset ready with {len(analysis_data)} experiments")
        
        # Step 3: Statistical Analysis
        print("\n3. PERFORMING STATISTICAL ANALYSIS")
        print("-" * 40)
        
        # Check for missing data
        find_missing_data(analysis_data)
        
        # Perform analysis for magnesium concentration
        print("\nAnalyzing magnesium concentration (fini_Mg)...")
        perform_full_analysis(
            analysis_data, 
            feature_columns_with_random, 
            ['fini_Mg'],
            pair_plot=False  # Set to True for detailed pair plots
        )
        
        # Step 4: Surrogate Space Generation
        print("\n4. GENERATING SURROGATE SPACE")
        print("-" * 40)
        
        # Generate LHS samples for demonstration
        print("Generating Latin Hypercube samples...")
        surrogate_data = sift_lhs_sample(
            n_points=1000,
            bounds=None,  # Use default bounds
            lhs_sampler=True,
            seed=42
        )
        print(f"Generated {len(surrogate_data)} surrogate experimental conditions")
        
        # Step 5: Pareto Optimization (if we have predictions)
        print("\n5. PARETO OPTIMIZATION DEMONSTRATION")
        print("-" * 40)
        
        # For demonstration, we'll create a simple surrogate with random predictions
        print("Creating demonstration surrogate with random predictions...")
        surrogate_data['fini_Mg'] = np.random.uniform(10, 200, len(surrogate_data))
        surrogate_data['fini_Ca'] = np.random.uniform(50, 500, len(surrogate_data))
        
        # Perform Pareto optimization
        pareto_front, pareto_data = optimize_pareto_front(
            surrogate_data,
            obj1_col="fini_Mg",
            obj2_col="fini_Ca",
            min_unique_points=20,
            population_size=100,
            generations=1000
        )
        
        print(f"Found {len(pareto_front)} Pareto-optimal solutions")
        
        # Step 6: Load Generated Data
        print("\n6. LOADING GENERATED DATA")
        print("-" * 40)
        
        try:
            generated_data = load_generated_data()
            print(f"Loaded {len(generated_data)} generated data files")
            
            # List available files
            for filename in generated_data.keys():
                if isinstance(generated_data[filename], pd.DataFrame):
                    print(f"  - {filename}: {len(generated_data[filename])} rows")
                elif isinstance(generated_data[filename], np.ndarray):
                    print(f"  - {filename}: shape {generated_data[filename].shape}")
        except FileNotFoundError:
            print("Generated data directory not found. Skipping this step.")
        
        # Step 7: Results Summary
        print("\n7. ANALYSIS SUMMARY")
        print("-" * 40)
        
        print("✓ Data loading completed successfully")
        print("✓ Statistical analysis performed")
        print("✓ Surrogate space generated")
        print("✓ Pareto optimization demonstrated")
        print("✓ All modules functioning correctly")
        
        print("\n" + "=" * 80)
        print("ANALYSIS PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 80)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        print("Please check your data files and try again.")
        return False


def demo_individual_modules():
    """
    Demonstrate individual module functionality.
    """
    print("\n" + "=" * 80)
    print("INDIVIDUAL MODULE DEMONSTRATIONS")
    print("=" * 80)
    
    # Demo 1: Data Processing
    print("\nDemo 1: Data Processing Functions")
    print("-" * 30)
    
    # Create sample data
    sample_data = pd.DataFrame({
        'Experiment ID': ['EXP001', 'EXP002'],
        'T cold (deg C)': [25, 30],
        'T hot (deg C)': [60, 70],
        'flow rate (mL/min)': [2.0, 3.0],
        'Mg (ppm)': [100, 150],
        'Mg (ppm).1': [50, 80]
    })
    
    # Extract data
    extracted_data = sift_data_extractor(sample_data)
    print(f"Extracted data shape: {extracted_data.shape}")
    print(f"Columns: {list(extracted_data.columns)}")
    
    # Demo 2: Surrogate Generation
    print("\nDemo 2: Surrogate Generation")
    print("-" * 30)
    
    # Generate small LHS sample
    lhs_sample = sift_lhs_sample(n_points=10, seed=42)
    print(f"LHS sample shape: {lhs_sample.shape}")
    print(f"Parameter ranges: {lhs_sample.describe()}")
    
    # Demo 3: Statistical Analysis
    print("\nDemo 3: Statistical Analysis")
    print("-" * 30)
    
    # Create sample data for analysis
    X_sample = pd.DataFrame({
        'T_cold': np.random.uniform(20, 40, 50),
        'T_hot': np.random.uniform(50, 80, 50),
        'flow_rate': np.random.uniform(1, 5, 50)
    })
    y_sample = X_sample['T_cold'] * 0.5 + X_sample['T_hot'] * 0.3 + np.random.normal(0, 5, 50)
    
    # Tune hyperparameters
    best_params = tune_hyperparameters(X_sample, y_sample, n_trials=5)
    print(f"Best parameters: {best_params}")
    
    # Train model
    model = train_model(X_sample, y_sample, best_params)
    print(f"Model trained successfully")
    
    print("\n" + "=" * 80)
    print("INDIVIDUAL MODULE DEMONSTRATIONS COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    # Run the main analysis pipeline
    success = main()
    
    if success:
        # Run individual module demonstrations
        demo_individual_modules()
        
        print("\n🎉 All demonstrations completed successfully!")
        print("\nTo use these modules in your own analysis:")
        print("1. Import the modules: from scripts import data_loader, statistical_analysis, etc.")
        print("2. Use the functions as demonstrated above")
        print("3. Check the docstrings for detailed parameter information")
    else:
        print("\n❌ Analysis pipeline failed. Please check the error messages above.") 