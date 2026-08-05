# Customer Churn Prediction (AI-ML Internship Day 13)

This project contains a simple Machine Learning pipeline to predict customer churn using a Random Forest Classifier. It includes all necessary components as requested for the Day 13 assignment of the Codomax Digital Solutions AI-ML Internship.

## Project Structure

- `dataset.csv`: The dataset containing customer information and their churn status.
- `notebook.ipynb`: A Jupyter Notebook containing data loading, preprocessing, model training, and evaluation.
- `screenshots/`: A folder containing screenshots/visualizations generated during the exploratory data analysis.
- `README.md`: This file, providing project details and setup instructions.

## Dataset Details

The dummy dataset consists of 1000 samples with the following columns:
- **Age**: Age of the customer.
- **Tenure**: Number of months the customer has stayed with the company.
- **MonthlyCharge**: The amount charged to the customer monthly.
- **TotalCharge**: The total amount charged to the customer.
- **ContractType**: The contract term of the customer (Month-to-month, One year, Two year).
- **InternetService**: Customer's internet service provider (DSL, Fiber optic, No).
- **Churn**: Whether the customer churned or not (Yes or No).

## Setup Instructions

1. **Prerequisites**: Make sure you have Python and Jupyter installed, along with the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```
2. **Running the Notebook**:
   - Open your terminal or VS Code in the Day-13 folder.
   - Run `jupyter notebook` and open `notebook.ipynb`.
   - Execute the cells sequentially to see the data processing and model evaluation.

## Day 13 GitHub Upload Instructions

To complete your Day 13 assignment, follow these steps to upload this project to GitHub:

1. **Initialize Git**:
   ```bash
   git init
   ```
2. **Add Files**:
   ```bash
   git add dataset.csv notebook.ipynb screenshots/ README.md
   ```
3. **Commit**:
   ```bash
   git commit -m "Day 13: Customer Churn Prediction Project Files"
   ```
4. **Link to GitHub**:
   - Create a new repository on GitHub (e.g., `Codomax-Internship-Day13`).
   - Copy the repository URL.
   - Run the following commands (replace `<YOUR_REPO_URL>` with your copied URL):
     ```bash
     git branch -M main
     git remote add origin <YOUR_REPO_URL>
     git push -u origin main
     ```

Your project will now be published on GitHub!
