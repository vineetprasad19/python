
# Transform Data Using Pandas
# This script cleans and transforms data using Pandas, such as handling missing values and renaming columns.

import pandas as pd

# Load data
df = pd.read_csv('raw_data.csv')

# Rename columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Filter rows
df = df[df['column_name'] > 10]

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)
print("Data transformation complete.")