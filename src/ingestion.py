import pandas as pd

# Define the relative path to the raw data
file_path ="data/raw/insurance fraud claims.csv"
columns_to_keep=['policy_number', 'age', 'fraud_reported']

print("---Read Specific Columns ----")
df =pd.read_csv(file_path, usecols=columns_to_keep)
print("First 3 rows:\n", df.head(3), "\n")

print("--- TASK 2: Set Index Column ---")
df_indexed=pd.read_csv(file_path, usecols=columns_to_keep, index_col='policy_number')
print("First 3 rows with indexed policy_number:\n", df_indexed.head(3), "\n")

print("--- TASK 3: Check Data Types ---")
print(df_indexed.dtypes, "\n")

print("--- TASK 4: Count Missing Values ---")
print(df_indexed.isna().sum(), "\n")

print("--- TASK 5: Unique Values in 'fraud_reported' ---")
print(df_indexed['fraud_reported'].unique(), "\n")
