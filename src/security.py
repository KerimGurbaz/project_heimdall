import pandas as pd
import hashlib

# ==========================================
# TASK 1: Prototyping SHA-256 Hash
# ==========================================
print("--- TASK 1: SHA-256 Prototype ---")

sample_text = "Heimdall_123"
# Hash functions in Python require data to be encoded as bytes, usually utf-8.
byte_data = sample_text.encode('utf-8')
# Create the hash object
hash_object = hashlib.sha256(byte_data)
# Convert the binary hash into a readable hexadecimal string
hashed_result = hash_object.hexdigest()

print(f"Original Text: {sample_text}")
print(f"Hashed Value : {hashed_result}\n")

# ==========================================
# TASK 2: Functionalizing the Masker
# ==========================================
print("--- TASK 2: Creating the mask_pii Function ---")

def mask_pii(text):
    """
    Takes an input string, handles missing values safely, 
    and returns its SHA-256 hex digest.
    """
    # 1. Safety Net: Handle missing or non-string data
    if pd.isna(text) or text == "" or text is None:
        return 'MISSING'
    
    # 2. Convert to string (just in case an integer slipped through)
    text_str = str(text)
    
    # 3. Hash operation
    hashed = hashlib.sha256(text_str.encode('utf-8')).hexdigest()
    
    return hashed

# Testing the function with different edge cases
test_cases = ["Krm_Secure", None, float('nan'), 12345]

print("Function Tests:")
for case in test_cases:
    print(f"Input: {str(case).ljust(12)} -> Output: {mask_pii(case)}")


# ==========================================
# TASK 3: Data Connection
# ==========================================
print("--- TASK 3: Loading Data ---")
file_path = "data/processed/cleaned_claims.csv"

try:
    df = pd.read_csv(file_path)
    print("Data loaded successfully. First 3 rows:\n")
    # Forcing pandas to display the policy_number clearly
    print(df[['policy_number', 'age', 'fraud_reported']].head(3), "\n")
except FileNotFoundError:
    print(f"WARNING: '{file_path}' not found.")
    print("Falling back to raw data to demonstrate the masking process...\n")
    # Fallback to raw data for demonstration
    df = pd.read_csv("data/raw/insurance fraud claims.csv")

# ==========================================
# TASK 4: Mass Destruction (Applying the Hash)
# ==========================================
print("--- TASK 4: Masking PII Column ---")

# .apply() takes the function we created and executes it for every single row in the column
df['policy_number'] = df['policy_number'].apply(mask_pii)

print("First 3 rows after SHA-256 Masking:\n")
print(df[['policy_number', 'age', 'fraud_reported']].head(3), "\n")


# ==========================================
# TASK 5: Reconnaissance and Destruction (Location Data)
# ==========================================
print("--- TASK 5: Masking Additional PII Column ---")

# 'incident_location' contains specific street addresses. 
# Physical locations tied to an event are considered sensitive PII.
target_col = 'incident_location' 

if target_col in df.columns:
    # Applying the exact same hash function to the location column
    df[target_col] = df[target_col].apply(mask_pii)
    
print("Final Data after all masking operations (First 5 rows):\n")

# Dynamically selecting columns to display to keep the terminal output clean
cols_to_print = ['policy_number', 'age', target_col, 'fraud_reported']
existing_cols = [col for col in cols_to_print if col in df.columns]

print(df[existing_cols].head(5), "\n")
