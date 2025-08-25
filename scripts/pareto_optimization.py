import pandas as pd
import numpy as np
from platypus import NSGAII, Problem, Real, Integer
import warnings
warnings.filterwarnings('ignore')

def optimize_pareto_front(df, obj1_col="fini_Mg", obj2_col="fini_Ca", 
                         min_unique_points=30, population_size=100, generations=50):
    """
    Optimize Pareto front using NSGA-II algorithm for multi-objective optimization.
    
    This function finds the Pareto optimal solutions for minimizing two objectives
    (typically impurity levels) using the NSGA-II evolutionary algorithm.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe containing the data to optimize
    obj1_col : str, default="fini_Mg"
        Column name for first objective (e.g., magnesium impurity)
    obj2_col : str, default="fini_Ca"
        Column name for second objective (e.g., calcium impurity)
    min_unique_points : int, default=30
        Minimum number of unique Pareto points to collect
    population_size : int, default=100
        Population size for NSGA-II algorithm
    generations : int, default=50
        Number of generations for NSGA-II algorithm
    
    Returns:
    --------
    tuple : (pandas.DataFrame, pandas.DataFrame)
        - First dataframe: Objective-only Pareto front
        - Second dataframe: Full data for Pareto front points
    
    Notes:
    ------
    - Uses modern pandas methods (pd.concat instead of deprecated append)
    - Implements NSGA-II multi-objective optimization
    - Filters for unique Pareto optimal solutions
    - Handles edge cases and provides robust error handling
    """
    
    try:
        # Validate input data
        if df.empty:
            raise ValueError("Input dataframe is empty")
        
        required_cols = [obj1_col, obj2_col]
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        # Check for valid numeric data
        if not pd.api.types.is_numeric_dtype(df[obj1_col]) or not pd.api.types.is_numeric_dtype(df[obj2_col]):
            raise ValueError(f"Objective columns {obj1_col} and {obj2_col} must be numeric")
        
        # Remove rows with NaN values in objective columns
        df_clean = df.dropna(subset=[obj1_col, obj2_col]).copy()
        if df_clean.empty:
            raise ValueError("No valid data after removing NaN values")
        
        # Create optimization problem
        class ParetoProblem(Problem):
            def __init__(self, data, obj1_col, obj2_col):
                super().__init__(1, 2)  # 1 variable (index), 2 objectives
                self.data = data
                self.obj1_col = obj1_col
                self.obj2_col = obj2_col
                self.types[0] = Integer(0, len(data) - 1)  # Index bounds
                self.directions[0] = Problem.MINIMIZE  # Minimize both objectives
                self.directions[1] = Problem.MINIMIZE
                
            def evaluate(self, solution):
                idx = int(solution.variables[0])
                row = self.data.iloc[idx]
                solution.objectives[0] = row[self.obj1_col]
                solution.objectives[1] = row[self.obj2_col]
        
        # Initialize problem and algorithm
        problem = ParetoProblem(df_clean, obj1_col, obj2_col)
        algorithm = NSGAII(problem, population_size=population_size)
        
        # Run optimization
        algorithm.run(generations)
        
        # Extract Pareto front
        pareto_front_unique = pd.DataFrame(columns=df_clean.columns)
        
        for solution in algorithm.result:
            if solution.objectives[0] < float('inf') and solution.objectives[1] < float('inf'):
                idx = int(solution.variables[0])
                pareto_row = df_clean.iloc[idx:idx+1]
                
                # Use pd.concat instead of deprecated append
                pareto_front_unique = pd.concat([pareto_front_unique, pareto_row], ignore_index=False)
        
        # Remove duplicates and sort
        pareto_front_unique = pareto_front_unique.drop_duplicates()
        pareto_front_unique = pareto_front_unique.sort_values([obj1_col, obj2_col])
        
        # Ensure minimum unique points
        if len(pareto_front_unique) < min_unique_points:
            print(f"Warning: Only {len(pareto_front_unique)} unique Pareto points found (requested: {min_unique_points})")
        
        # Create objective-only dataframe
        pareto_front_df = pareto_front_unique[[obj1_col, obj2_col]].copy()
        pareto_front_df = pareto_front_df.reset_index(drop=True)
        
        return pareto_front_df, pareto_front_unique
        
    except Exception as e:
        print(f"Error in optimize_pareto_front: {str(e)}")
        # Return empty dataframes on error
        empty_df = pd.DataFrame(columns=[obj1_col, obj2_col])
        return empty_df, pd.DataFrame(columns=df.columns if not df.empty else []) 