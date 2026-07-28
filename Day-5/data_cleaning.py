import pandas as pd
import numpy as np

def load_data(filepath):
    """Load the dataset from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        print("Dataset loaded successfully.\n")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None

def understand_statistics(df):
    """Print dataset statistics and information."""
    print("--- Dataset Statistics ---")
    print(f"Shape of the dataset: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nDataset Info:")
    df.info()
    print("\nSummary Statistics:")
    print(df.describe())
    print("-" * 25 + "\n")

def clean_data(df):
    """Perform data cleaning: handle missing values and remove duplicates."""
    print("--- Data Cleaning ---")
    
    # 1. Identify missing values
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    # Handling missing values
    # For numerical columns (Age, Salary), we will fill missing values with the median
    print("\nFilling missing values for 'Age' and 'Salary' with their respective medians.")
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Salary'] = df['Salary'].fillna(df['Salary'].median())
    
    # For categorical columns (Department), we will fill missing values with the mode
    print("Filling missing values for 'Department' with the mode.")
    department_mode = df['Department'].mode()[0]
    df['Department'] = df['Department'].fillna(department_mode)
    
    print("\nMissing values after handling:")
    print(df.isnull().sum())
    
    # 2. Identify and remove duplicates
    duplicate_count = df.duplicated().sum()
    print(f"\nNumber of duplicate rows found: {duplicate_count}")
    
    if duplicate_count > 0:
        print("Removing duplicate rows.")
        df = df.drop_duplicates()
        print(f"Shape of the dataset after removing duplicates: {df.shape}")
        
    print("-" * 21 + "\n")
    return df

def save_clean_data(df, output_filepath):
    """Save the cleaned dataset to a new CSV file."""
    df.to_csv(output_filepath, index=False)
    print(f"Cleaned dataset saved to '{output_filepath}'.")

def main():
    input_file = 'dataset.csv'
    output_file = 'cleaned_dataset.csv'
    
    # Step 1: Load Data
    df = load_data(input_file)
    if df is not None:
        # Step 2: Understand dataset statistics
        understand_statistics(df)
        
        # Step 3: Handle missing values and remove duplicates
        cleaned_df = clean_data(df)
        
        # Step 4: Verify the cleaned dataset
        print("--- Final Dataset Verification ---")
        print(cleaned_df.info())
        
        # Step 5: Save the cleaned data
        save_clean_data(cleaned_df, output_file)

if __name__ == "__main__":
    main()
