"""
Utility functions for the Day 12 project.
"""

def clean_data(df):
    """
    Cleans the dataframe by handling missing values.
    
    Args:
        df (pd.DataFrame): The input pandas DataFrame.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Example logic: drop rows with missing values
    return df.dropna()
