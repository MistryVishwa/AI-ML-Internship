# Day 7: Machine Learning Basics

## Objective
Learn supervised learning, train-test split, and Linear Regression concepts. 
**Expected Outcome**: ML fundamentals understood.

## Concepts Overview

### 1. Supervised Learning
Supervised learning is a type of machine learning where the model is trained on a **labeled dataset**. This means that each training example is paired with an output label. The model learns to map inputs (features) to the correct output (target). 
- **Example**: Predicting house prices based on features like area, number of bedrooms, etc. (Regression).
- **Example**: Classifying emails as spam or not spam (Classification).

### 2. Train-Test Split
When building a machine learning model, it's crucial to evaluate its performance on unseen data. To do this, we split our dataset into two sets:
- **Training Set (e.g., 80%)**: Used to train the model so it can learn the underlying patterns.
- **Testing Set (e.g., 20%)**: Used to evaluate the model's performance on new, unseen data to ensure it generalizes well and doesn't just memorize the training data (overfitting).

### 3. Linear Regression
Linear Regression is a fundamental supervised learning algorithm used for predicting a continuous target variable. It assumes a linear relationship between the input features ($X$) and the single output variable ($y$).
- **Equation**: $y = mx + c$ (for simple linear regression with one feature), where $m$ is the slope (weight) and $c$ is the y-intercept (bias).
- The goal of the algorithm is to find the best-fitting line through the data points by minimizing the error (usually Mean Squared Error) between the predicted values and the actual values.

## Project Structure
- `linear_regression_example.py`: Python script demonstrating a complete workflow of generating data, performing a train-test split, training a Linear Regression model, and visualizing the results.
- `requirements.txt`: List of dependencies needed to run the script.
- `README.md`: This file.

## Setup Instructions

1. **Open the `Day-7` folder in VS Code.**
2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install Dependencies:**
   Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Script:**
   Execute the python script to see the linear regression model in action:
   ```bash
   python linear_regression_example.py
   ```
   You will see text output in the console evaluating the model (Mean Squared Error), and a plot will open showing the training data, testing data, and the best fit regression line.
