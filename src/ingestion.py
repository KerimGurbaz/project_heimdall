import pandas as pd

# Read the CSV file into a Pandas DataFrame.
file_path= "data/raw/insurance fraud claims.csv"

# Print the first 5 rows of the DataFrame to inspect the data.
df = pd.read_csv(file_path)

# Print the total number of rows and columns.
print(df.head())


#print("\n--- Dataset Shape (Rows, Columns) ---")
print(df.shape)
