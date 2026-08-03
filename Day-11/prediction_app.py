import numpy as np
from sklearn.linear_model import LinearRegression

def create_and_train_model():
    # Synthetic data for study hours vs score
    # A simple linear relationship with slight variance
    hours = np.array([1.1, 1.5, 2.0, 2.5, 2.7, 3.2, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5]).reshape(-1, 1)
    scores = np.array([14, 18, 22, 26, 29, 32, 36, 42, 45, 52, 58, 62, 67, 74, 78, 83, 86, 92, 97])

    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(hours, scores)
    return model

def main():
    print("========================================")
    print("       Student Score Predictor App      ")
    print("========================================")
    print("Training model on historical data...")
    
    model = create_and_train_model()
    
    print("Model trained successfully!")
    print("Type 'exit' or 'quit' to close the program.\n")
    
    while True:
        try:
            user_input = input("Enter the number of study hours: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting program. Goodbye!")
                break
            
            hours = float(user_input)
            
            if hours < 0:
                print("Error: Study hours cannot be negative. Please enter a valid positive number.\n")
                continue
            
            # Predict the score based on the input hours
            predicted_score = model.predict([[hours]])[0]
            
            # Cap the predicted score at a maximum of 100%
            if predicted_score > 100:
                predicted_score = 100.0
            
            print(f"--> Predicted Score for {hours} hours of study: {predicted_score:.2f}%\n")
            
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value for hours.\n")

if __name__ == "__main__":
    main()
