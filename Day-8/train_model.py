import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import make_regression

def main():
    print("--- Day 8: Build and Train the Model ---")
    
    # 1. Generate a synthetic dataset for linear regression
    print("Loading dataset...")
    X, y = make_regression(n_samples=1000, n_features=5, noise=15.0, random_state=42)
    
    # 2. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Initialize model
    print("Initializing Linear Regression model...")
    model = LinearRegression()
    
    # 4. Train the model
    print("Training the model...")
    model.fit(X_train, y_train)
    
    # 5. Predict and evaluate
    print("Evaluating the model on test data...")
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n--- Model Evaluation ---")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R-squared Score: {r2:.4f}")
    print("\nExpected Outcome: Model trained successfully!")

if __name__ == "__main__":
    main()
