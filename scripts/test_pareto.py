#!/usr/bin/env python3
"""
Test script for the fixed optimize_pareto_front function.
This script verifies that the pandas compatibility issue has been resolved.
"""

import pandas as pd
import numpy as np
from pareto_optimization import optimize_pareto_front

def test_pareto_optimization():
    """Test the Pareto optimization function with sample data."""
    
    print("Testing Pareto optimization function...")
    
    # Create sample data
    np.random.seed(42)
    n_samples = 100
    
    sample_data = pd.DataFrame({
        'fini_Mg': np.random.uniform(10, 200, n_samples),
        'fini_Ca': np.random.uniform(5, 150, n_samples),
        'T_cold': np.random.uniform(20, 80, n_samples),
        'T_hot': np.random.uniform(80, 120, n_samples),
        'pH': np.random.uniform(6.5, 8.5, n_samples),
        'experiment_id': range(n_samples)
    })
    
    print(f"Created sample data with {len(sample_data)} rows")
    print(f"Columns: {list(sample_data.columns)}")
    print(f"Sample data:\n{sample_data.head()}")
    
    try:
        # Test the function
        print("\nRunning Pareto optimization...")
        pareto_front, pareto_data = optimize_pareto_front(
            sample_data, 
            obj1_col="fini_Mg", 
            obj2_col="fini_Ca",
            min_unique_points=10,
            population_size=50,
            generations=20
        )
        
        print(f"✅ Success! Pareto optimization completed.")
        print(f"Pareto front shape: {pareto_front.shape}")
        print(f"Pareto data shape: {pareto_data.shape}")
        print(f"Pareto front:\n{pareto_front.head()}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_pareto_optimization()
    if success:
        print("\n🎉 All tests passed! The pandas compatibility issue has been resolved.")
    else:
        print("\n💥 Tests failed. Please check the error messages above.")
