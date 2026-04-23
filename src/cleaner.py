import pandas as pd
file_path ="data/raw/insurance fraud claims.csv"

# ==========================================
# SETUP: Read the raw data completely
# ==========================================

print("---SETUP: Initial Data State---")
df=pd.read_csv(file_path)
print(f"Original Data Shape : {df.shape}\n")

# ==========================================
# TASK 1: Column Amputation (Drop _c39)
# ==========================================
print("--- TASK 1: Dropping Garbage Column ---")
df.drop('_c39', axis=1, inplace=True)
print(f"Shape after dropping '_39': {df.shape}\n")

# ==========================================
# TASK 2: Targeted Row Resection
# ==========================================
print("--- TASK 2: Dropping Rows with Null Policy Numbers ---")
# subset=['policy_number'] ensures we ONLY drop rows where this specific column is NaN.
# If we used df.dropna() without subset, we would destroy rows with NaNs in irrelevant columns.
df.dropna(subset=['policy_number'], inplace=True)
print(f"Shape after dropping invalid policies: {df.shape}\n")

# ==========================================
# TASK 3: Prosthesis (Imputing Missing Age)
# ==========================================
print("--- TASK 3: Imputing Missing Ages ---")
# 1. Calculate the mean of existing ages, rounded to 1 decimal place
mean_age = round(df['age'].mean(), 1)
print(mean_age)
print(df.describe())

# 2. Fill NaN values in the 'age' column with this mean value
# We reassign it to the column to follow modern Pandas best practices
df['age']= df['age'].fillna(mean_age)
print(f"Filled missing ages with the dataset mean: {mean_age}\n")


# ==========================================
# TASK 4: Date Formatting (String to DateTime)
# ==========================================
print("--- TASK 4: Converting Date Format ---")
# Converting 'incident_date' from object (string) to proper datetime format.
# errors='coerce' forces invalid date strings (like "unknown") to become NaT (Not a Time).
if 'incident_date' in df.columns:
    print(f"Old type: {df['incident_date'].dtype}")
    df['incident_date'] = pd.to_datetime(df['incident_date'], errors='coerce')
    print(f"New type: {df['incident_date'].dtype}\n")


# ==========================================
# TASK 5: Logic Filter (Boolean Indexing)
# ==========================================
print("--- TASK 5: Filtering Impossible Ages ---")
# Keeping only rows where age is logically valid (between 18 and 100).
# The '&' symbol is used instead of 'and' for element-wise Pandas evaluation.
df = df[(df['age']>=18) & (df['age']<=100)]
print(f"Final Data Shape after all cleaning: {df.shape}\n")
