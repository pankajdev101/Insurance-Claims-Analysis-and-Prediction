# connection with sql and python
import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost;"
    "DATABASE=Insurance;"
    "Trusted_Connection=yes;")

df_claims= pd.read_sql("SELECT * FROM Insurance_Claims", conn)  

#Data Cleaning
# -------------------------

#Duplicate Records Remove

df_claims.drop_duplicates(subset=['Claim_ID'], inplace=True) 

# Missing Values Handle

df_claims['Client'] = df_claims['Client'].fillna('Unknown')
df_claims['Hospital'] = df_claims['Hospital'].fillna('Unknown')
df_claims['State'] = df_claims['State'].fillna('Unknown')
df_claims['Disease_Group'] = df_claims['Disease_Group'].fillna('Unknown')

df_claims['Approved_Amount'] = df_claims['Approved_Amount'].fillna(0)
df_claims['Deduction_Amount'] = df_claims['Deduction_Amount'].fillna(0)
df_claims['Fraud_Risk_Score'] = df_claims['Fraud_Risk_Score'].fillna(0) 

#Data Types Correct

df_claims['Age'] = df_claims['Age'].astype(int)
df_claims['Claim_Amount_Submitted'] = df_claims['Claim_Amount_Submitted'].
astype(float) 

# Date Columns

df_claims['Claim_Submission_Date'] = pd.to_datetime(
    df_claims['Claim_Submission_Date'] 

# 4. Text Cleaning

df_claims['Client'] = (
    df_claims['Client']
    .str.strip()
    .str.replace(' ', '_'))

df_claims['Claim_Status'] = (
    df_claims['Claim_Status']
    .str.strip()
    .str.replace(' ', '_')) 

# 5. Check Remaining Null Values

print(df_claims.isnull().sum())

# 6. Save Cleaned Data

df_claims.to_csv('insurance_claims_cleaned.csv', index=False)

print("Data Cleaning Completed Successfully") 






