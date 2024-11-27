# Overview

The aim of this project is to predict whether a loan application will be approved or not. Loan approval is a critical task for financial institutions, and automating this process can help streamline decision-making, reduce manual labor, and improve accuracy. By leveraging historical data, our model predicts the likelihood of loan approval based on key applicant and loan features.

This tool can be useful for:

1. Applicants: To understand their chances of loan approval.
2. Financial Institutions: To speed up the loan approval process and ensure fair and consistent decisions.

# Repo Structure

```
├── data
│   ├── loan_data.csv                    # Cleaned and preprocessed dataset  
│   ├── original_dataset.csv             # Raw dataset used for the project  
├── notebooks  
│   ├── loan-approval_project.ipynb       # Data preparation and cleaning & Exploratory Data Analysis 
├── scripts  
│   ├── test.py                          # Script to test the API for loan predictions  
│   ├── train.py                         # Script to train the final model  
├── .gitignore                           # Git ignore file  
├── .dockerignore                        # Docker ignore file  
├── Dockerfile                           # Dockerfile for serving the model in a container  
├── pyproject.toml                       # Poetry project description and dependencies  
├── poetry.lock                          # Poetry lock file  
├── predict.py                           # Flask API for serving the model  
├── model.bin                            # Serialized trained model
└── README.md
```

# Dataset

The dataset is included in the folder (loan_data.csv). It was gotten from kaggle (https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data).

# Methodology

*Data Cleaning, Data Preparation and Exploratory Data Analysis (EDA)*:
The data was cleaned and preprocessed for better usability. Key insights into the data were explored, visualized and categorical variables were encoded for modeling. All preprocessing steps are documented in loan-approval-project.ipynb.

*Modeling*:
Various machine learning models were tested, and the best-performing model was selected based on accuracy and auc-score.

*Model Training*:
The model was trained using the script train.py and serialized as model.bin.

*Deployment*:
The model is deployed using Flask (predict.py) and is containerized with Docker.

# How to Use the App
Prerequisites:
1. Install and run Docker
2. Install Poetry for managing dependencies

# Instructions:
Build the Docker image:

```bash
docker build -t loan_approval .
```

Run the container:

```bash
docker run -p 9696:9696 loan_approval
```

Test the API:
Run the predict-test.py script to make a prediction:

```bash
python predict-test.py
```

This script sends a sample loan application to the API and returns a prediction (approved or not approved).
