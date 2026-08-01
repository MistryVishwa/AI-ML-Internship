import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import os

def create_and_train_model():
    """Trains a simple linear regression model for student scores based on study hours and saves it."""
    print("Creating training data...")
    # Synthetic data: study hours and corresponding scores
    data = {
        'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4],
        'Scores': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 85, 62, 41, 42, 17, 95, 30, 24, 67, 69]
    }
    df = pd.DataFrame(data)
    
    X = df[['Hours']]
    y = df['Scores']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Save the model
    joblib.dump(model, 'student_score_model.pkl')
    print("Model trained and saved as 'student_score_model.pkl'.\n")
    return model

def predict_scores():
    """Loads the trained model and predicts student scores based on new study hours."""
    print("--- Day 9: Prediction Tasks ---")
    
    # Check if model exists, if not, create it
    if not os.path.exists('student_score_model.pkl'):
        print("Trained model not found. Training a new model first...")
        model = create_and_train_model()
    else:
        print("Loading existing trained model 'student_score_model.pkl'...\n")
        model = joblib.load('student_score_model.pkl')
    
    # New study hours for prediction
    new_hours = np.array([[9.25], [1.5], [4.0], [7.5], [6.8]])
    print("Study hours to predict scores for:")
    for h in new_hours:
        print(f" - {h[0]} hours")
        
    print("\nGenerating predictions...")
    predictions = model.predict(new_hours)
    
    print("\n--- Prediction Results ---")
    for i in range(len(new_hours)):
        print(f"Study Hours: {new_hours[i][0]:.2f}  =>  Predicted Score: {predictions[i]:.2f}")
    
    print("\nExpected Outcome: Predictions generated successfully.")

if __name__ == "__main__":
    predict_scores()
