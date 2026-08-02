import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_model():
    """Trains a model and evaluates its performance using MAE, MSE, and R² Score."""
    print("--- Day 10: Model Evaluation Tasks ---\n")
    print("Loading data and splitting into training/testing sets...")
    
    # Synthetic data from the Student Score Prediction dataset (Hours vs Scores)
    data = {
        'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4],
        'Scores': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 85, 62, 41, 42, 17, 95, 30, 24, 67, 69]
    }
    df = pd.DataFrame(data)
    
    X = df[['Hours']]
    y = df['Scores']
    
    # Split the dataset: 80% for training and 20% for testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training the Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    print("Making predictions on the test set...")
    y_pred = model.predict(X_test)
    
    print("\n--- Evaluation Metrics ---")
    
    # 1. Mean Absolute Error (MAE)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    
    # 2. Mean Squared Error (MSE)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error (MSE):  {mse:.4f}")
    
    # 3. R-squared Score (R²)
    r2 = r2_score(y_test, y_pred)
    print(f"R-squared Score (R²):      {r2:.4f}")
    
    print("\nExpected Outcome: Model performance measured.")

if __name__ == "__main__":
    evaluate_model()
