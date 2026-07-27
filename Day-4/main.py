"""
Day 4 - Pandas Fundamentals
Codomax Digital Solutions AI/ML Internship

Topics Covered:
1. Import Pandas
2. Load Dataset
3. Explore Rows
4. Explore Columns
5. Dataset Information
6. Summary Statistics
"""

import pandas as pd


print("=" * 60)
print("CODOMAX DIGITAL SOLUTIONS")
print("AI/ML Internship - Day 4")
print("Pandas Dataset Exploration")
print("=" * 60)


# Load Dataset
df = pd.read_csv("data/student_scores.csv")

print("\nDataset Loaded Successfully!")
print("-" * 60)

# Display first rows
print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset Shape")
print(df.shape)

print("\nRows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names")
print(df.columns.tolist())

print("\nDataset Information")
print("-" * 60)
df.info()

print("\nSummary Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nStudent Names")
print(df["Name"])

print("\nMath Scores")
print(df["Math"])

print("\nAverage Marks")

subjects = ["Math", "Science", "English", "Computer"]

for subject in subjects:
    print(f"{subject}: {df[subject].mean():.2f}")

print("\nHighest Marks")

for subject in subjects:
    print(f"{subject}: {df[subject].max()}")

print("\nLowest Marks")

for subject in subjects:
    print(f"{subject}: {df[subject].min()}")

print("\nComplete Dataset")
print(df)

summary = []

summary.append("Dataset Summary")
summary.append("=" * 40)
summary.append(f"Rows: {df.shape[0]}")
summary.append(f"Columns: {df.shape[1]}")
summary.append(f"Columns: {', '.join(df.columns)}")

summary.append("\nAverage Scores")

for subject in subjects:
    summary.append(f"{subject}: {df[subject].mean():.2f}")

summary.append("\nMaximum Scores")

for subject in subjects:
    summary.append(f"{subject}: {df[subject].max()}")

summary.append("\nMinimum Scores")

for subject in subjects:
    summary.append(f"{subject}: {df[subject].min()}")

with open("output/dataset_summary.txt", "w") as file:
    file.write("\n".join(summary))

print("\nDataset summary saved inside output/dataset_summary.txt")

print("\nDay 4 Completed Successfully!")