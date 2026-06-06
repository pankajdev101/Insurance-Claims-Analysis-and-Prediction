# Insurance Claims Analysis and Prediction

## Project Overview
This project analyzes insurance claims data using SQL Server, Python, and Power BI. The objective is to perform data cleaning, exploratory data analysis (EDA), dashboard development, and machine learning prediction.

## Tools Used
- SQL Server
- Python
- Pandas
- NumPy
- Scikit-Learn
- Power BI
- Jupyter Notebook

## Dataset Columns
- Claim_ID
- Client
- Hospital
- Processor
- Gender
- Age
- State
- District
- Region
- Disease_Group
- Claim_Submission_Date
- Claim_Amount_Submitted
- Processing_Days
- Claim_Completion_Date
- SLA_Days
- Within_SLA
- Claim_Status
- Deduction_Amount
- Approved_Amount
- Rejection_Reason
- Deduction_Reason
- Queries_Raised
- Query_Resolution_Days
- Fraud_Risk_Score
- Duplicate_Claim_Probability
- Predicted_SLA_Breach
- Rejection_Probability

## Data Extraction
- Imported insurance claims data into SQL Server.
- Connected SQL Server with Python using PyODBC.
- Extracted data for analysis and modeling.

## Data Cleaning
- Removed duplicate records based on Claim_ID.
- Handled missing values.
- Corrected data types.
- Cleaned categorical columns.
- Standardized text values.

## SQL Analysis Performed

### Claim Analysis
- Total Claims
- Approved Claims
- Rejected Claims
- Pending Claims

### Financial Analysis
- Total Claim Amount Submitted
- Total Approved Amount
- Total Deduction Amount

### State Analysis
- State-wise Claims
- State-wise Approved Amount

### Disease Analysis
- Disease Group-wise Claims
- Disease Group-wise Approval Rate

### SLA Analysis
- Claims Within SLA
- Claims Breaching SLA
- Average Processing Time

### Fraud Analysis
- High Fraud Risk Claims
- Fraud Risk Score Distribution

## Exploratory Data Analysis (EDA)
- Claim Status Distribution
- Age Distribution
- Gender-wise Claims
- State-wise Claims
- Disease Group Analysis
- Fraud Risk Analysis
- SLA Performance Analysis

## Dashboard Development
Created an interactive Power BI dashboard with:

- Total Claims
- Approval Rate
- Rejection Rate
- Total Approved Amount
- Average Processing Days
- State-wise Claims
- Disease Group Analysis
- Fraud Risk Insights
- SLA Compliance Analysis

## Machine Learning Prediction

### Prediction Objective
Predict whether a claim will be:

- Approved
- Rejected
- Pending

### Model Used
- Random Forest Classifier

### Features Used
- Age
- Gender
- State
- Disease_Group
- Claim_Amount_Submitted
- Processing_Days
- SLA_Days
- Deduction_Amount
- Approved_Amount
- Queries_Raised
- Query_Resolution_Days
- Fraud_Risk_Score
- Duplicate_Claim_Probability

### Evaluation Metrics
- Accuracy Score
- Confusion Matrix

## Key Insights
- Identified factors affecting claim approval and rejection.
- Analyzed fraud risk patterns.
- Evaluated SLA compliance performance.
- Compared hospital and state-level claim performance.
- Built a predictive model for claim status prediction.

## Files Included
- insurance_claim_analysis.py
- insurance_claims_dashboard.pbid
- 03_claim_status_prediction.ipynb
- README.md

## Author
Pankaj Patel
