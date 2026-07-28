# Day 5 - Data Cleaning Tasks

This folder contains the files for the Day 5 task of the AI-ML Internship at Codomax Digital Solutions. 
The objective is to perform data cleaning tasks, including handling missing values, removing duplicates, and understanding dataset statistics.

## Folder Structure

- `dataset.csv`: A sample dataset containing dirty data (missing values and duplicate rows). You can replace this with your actual dataset if needed.
- `data_cleaning.py`: The main Python script that performs the data cleaning steps using the `pandas` library.
- `requirements.txt`: Lists the Python dependencies required to run the script.
- `cleaned_dataset.csv`: This file will be generated automatically after you run the script, containing the clean dataset.

## Setup Instructions

1. **Prerequisites**: Make sure you have Python installed on your system.
2. **Open Terminal**: Open your terminal (or command prompt/PowerShell) and navigate to this `Day-5` folder in VS Code.
3. **Install Dependencies**: Install the required Python libraries (`pandas` and `numpy`) by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Code

Execute the Python script using the following command:
```bash
python data_cleaning.py
```

## What the Script Does

1. **Loads Data**: It reads `dataset.csv` into a Pandas DataFrame.
2. **Understands Statistics**: It prints the shape, first few rows, dataset info (data types, non-null counts), and summary statistics (mean, min, max, etc.).
3. **Handles Missing Values**:
   - For numerical columns (`Age`, `Salary`), it fills missing `NaN` values with the median of that column.
   - For categorical columns (`Department`), it fills missing values with the mode (most frequent value).
4. **Removes Duplicates**: It identifies any completely duplicate rows and removes them.
5. **Saves Output**: Finally, it saves the cleaned data to a new file named `cleaned_dataset.csv`.
