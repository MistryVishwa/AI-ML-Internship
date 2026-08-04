# Day 12 - Project Improvement Tasks

This directory contains the professional project structure as requested. It is organized to serve as a template for your data science and machine learning projects.

## Folder Structure

A professional project structure typically looks like this:

```
Day-12/
│
├── data/                  # Store datasets here (raw, processed)
├── notebooks/             # Jupyter notebooks for exploration and analysis
│   └── 01_Data_Exploration.ipynb
├── src/                   # Reusable source code (scripts, modules)
│   ├── __init__.py
│   └── utils.py
├── README.md              # Project overview and setup instructions
└── requirements.txt       # Dependencies needed to run the project
```

## Setup Instructions

1. **Open the project in VS Code**:
   Open the `Day-12` folder directly in VS Code.
   
2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**:
   Run the following command to install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Notebook**:
   Open `notebooks/01_Data_Exploration.ipynb` in VS Code and select your Python environment (or the virtual environment you just created) as the Jupyter kernel.

## Guidelines Implemented
- **Notebook Formatting**: Notebooks include Markdown cells for structure (headings, explanations) and properly formatted Python code.
- **Comments**: Python code contains detailed inline comments and docstrings.
- **Organization**: Source code and notebooks are separated.

Happy Coding!
