# Day 10: Model Evaluation Tasks

This project evaluates the performance of a machine learning model (Linear Regression) using standard regression metrics: **Mean Absolute Error (MAE)**, **Mean Squared Error (MSE)**, and **R² Score**. It trains the model on synthetic student data (Study Hours vs. Scores) and calculates these metrics on a test set.

## Folder Structure
```text
Day-10/
│
├── model_evaluation.py     # Main Python script containing the model training and evaluation logic
├── requirements.txt        # Required Python libraries (pandas, scikit-learn, numpy)
└── README.md               # This setup and instruction file
```

## Setup Instructions

1.  **Open in VS Code:** Open the `Day-10` folder directly in VS Code.
2.  **Create a Virtual Environment (Optional but recommended):**
    Open your terminal in VS Code (`Ctrl + \``) and run:
    ```bash
    python -m venv venv
    ```
    Activate the environment:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
3.  **Install Dependencies:**
    Install the required libraries by running:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Code

Run the Python script to train the model and see the evaluation metrics:
```bash
python model_evaluation.py
```

## Explanations of Metrics

- **Mean Absolute Error (MAE):** Calculates the average absolute difference between the predicted values and the actual values. It measures the average magnitude of the errors without considering their direction.
- **Mean Squared Error (MSE):** Calculates the average of the squared differences between the predicted values and the actual values. It gives a higher penalty to larger errors.
- **R-squared Score (R²):** Represents the proportion of the variance for a dependent variable that's explained by an independent variable. A score closer to 1 indicates a better fit.
