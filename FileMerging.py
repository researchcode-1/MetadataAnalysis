import pandas as pd

# List of CSV file paths
file1 = "abstracts_with_keyword9000.csv"
file2 = "abstracts_with_keywords10000.csv"
file3 = "abstracts_with_keywords15000.csv"

# Function to read CSV with error handling
def read_csv_with_encoding(file_path):
    try:
        # Attempt reading the file with 'utf-8' encoding, and skip errors
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return pd.read_csv(file)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Read each file
df1 = read_csv_with_encoding(file1)
df2 = read_csv_with_encoding(file2)
df3 = read_csv_with_encoding(file3)

# Ensure the files were read correctly
if df1 is not None and df2 is not None and df3 is not None:
    # Merge the DataFrames by appending them
    merged_df = pd.concat([df1, df2, df3], ignore_index=True)

    # Save the merged DataFrame to a new CSV file
    output_file = "merged_file.csv"
    merged_df.to_csv(output_file, index=False)

    print(f"Files merged successfully into {output_file}")
else:
    print("There was an issue with reading the files.")