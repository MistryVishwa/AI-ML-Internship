# Day 8: Build the Model

## Objective
Create a Linear Regression model using Scikit-learn and train it with the dataset.
**Expected Outcome**: Model trained successfully.

## Overview
This project demonstrates how to initialize, train, and evaluate a Linear Regression model using `scikit-learn`. We generate a synthetic dataset, split it into training and testing sets, train the model, and then calculate evaluation metrics like Mean Squared Error (MSE) and R-squared.

## Folder Structure
```text
Day-8/
│
├── train_model.py          # Main Python script for model training
├── requirements.txt        # Required Python libraries
└── README.md               # Setup and instruction file
```

## Setup Instructions

1.  **Open in VS Code:** Open the `Day-8` folder directly in VS Code.
2.  **Create a Virtual Environment (Optional but recommended):**
    Open your terminal in VS Code (`Ctrl + \``) and run:
    ```bash
    python -m venv venv
    ```
    Activate the environment:
    - Windows: `.\venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
3.  **Install Dependencies:**
    Install the necessary libraries using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Code

Run the Python script to build and train the model:
```bash
python train_model.py
```

The script will output the training process along with the evaluation scores, concluding with the expected outcome message.
