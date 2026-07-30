import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def main():
    print("--- Day 7: Machine Learning Basics ---")
    print("Topic: Supervised Learning, Train-Test Split, and Linear Regression\n")

    # 1. Generate Synthetic Data
    # Let's create some data that follows a roughly linear relationship (y = 2x + 1) with some noise
    np.random.seed(42) # Set seed for reproducibility
    
    # X represents our feature (e.g., house size in sq ft)
    X = 2 * np.random.rand(100, 1)
    
    # y represents our target variable (e.g., house price)
    # y = 2 * X + 1 + Gaussian noise
    y = 1 + 2 * X + np.random.randn(100, 1) * 0.5 

    print(f"Dataset created with {X.shape[0]} samples.")

    # 2. Train-Test Split
    # We split our data: 80% for training the model, 20% for testing its performance on unseen data.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"Data split into {X_train.shape[0]} training samples and {X_test.shape[0]} testing samples.\n")

    # 3. Initialize and Train the Linear Regression Model (Supervised Learning)
    print("Training the Linear Regression model...")
    model = LinearRegression()
    
    # The fit method is where the model 'learns' the relationship between X_train and y_train
    model.fit(X_train, y_train)
    
    # Retrieve the learned parameters
    intercept = model.intercept_[0]
    slope = model.coef_[0][0]
    print(f"Model trained!")
    print(f"Learned Equation: y = {slope:.2f} * x + {intercept:.2f}\n")

    # 4. Make Predictions on the Test Set
    # We use the testing data (X_test) which the model has never seen before
    y_pred = model.predict(X_test)

    # 5. Evaluate the Model
    # Calculate Mean Squared Error (MSE) to see how far off our predictions are on average
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model Evaluation:")
    print(f"Mean Squared Error (MSE) on Test Set: {mse:.4f}")

    # 6. Visualize the Results
    plt.figure(figsize=(10, 6))
    
    # Plot training data
    plt.scatter(X_train, y_train, color='blue', label='Training Data', alpha=0.6)
    
    # Plot testing data
    plt.scatter(X_test, y_test, color='green', label='Testing Data', marker='x', s=60)
    
    # Plot the Regression Line (Best Fit Line)
    # We plot the line over the whole range of X
    X_range = np.array([[0], [2]])
    y_range_pred = model.predict(X_range)
    plt.plot(X_range, y_range_pred, color='red', linewidth=2, label='Regression Line (Best Fit)')
    
    plt.title('Linear Regression: Train-Test Split Visualization')
    plt.xlabel('Feature (X)')
    plt.ylabel('Target (y)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    print("\nOpening visualization plot... Close the plot window to exit the script.")
    plt.show()

if __name__ == "__main__":
    main()
