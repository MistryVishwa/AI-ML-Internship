# Day 9: Prediction Tasks

This project covers the Day 9 task of the Codomax Digital Solutions AI-ML Internship.
The goal is to use a trained Machine Learning model to predict student scores based on the number of study hours.

## Expected Outcome
Use the trained model to predict student scores based on study hours. Predictions are generated successfully.

## Folder Structure
```text
Day-9/
│
├── predict_scores.py       # Main Python script for training (if not found) and predicting
├── requirements.txt        # Required Python libraries
└── README.md               # This setup and instruction file
```

## Setup Instructions

1. **Open in VS Code**: Open the `Day-9` folder directly in Visual Studio Code.
2. **Create a Virtual Environment (Optional but recommended)**:
   Open your terminal in VS Code and run:
   ```bash
   python -m venv venv
   ```
   Activate the environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
3. **Install Dependencies**:
   Install the required libraries using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Code

Run the Python script to execute the predictions:
```bash
python predict_scores.py
```

### What the Script Does:
1. It first checks if a pre-trained model file (`student_score_model.pkl`) exists. 
2. If it does not exist, it trains a simple Linear Regression model on sample study hours vs. scores data and saves the trained model.
3. It then loads the model and predicts scores for a new set of study hours, fulfilling the Day 9 criteria.
