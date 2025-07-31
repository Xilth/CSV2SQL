import pandas as pd
csv_file = 'C:\\xampp\\data_import_devel\\mst_member_type.csv'

# Step 1: Read the header line manually
with open(csv_file, 'r', encoding='utf-8') as f:
    header_line = f.readline().strip()

# Step 2: Manually split and clean column names
columns = []
for col in header_line.split(','):
    cleaned_col = col.strip().strip('"')  # Remove any spaces and double quotes
    columns.append(cleaned_col)

print("Detected Columns:", columns)

# Step 3: Read the rest of the CSV using these columns
df = pd.read_csv(csv_file, names=columns, skiprows=1)

print(df.head())
