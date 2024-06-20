import pandas as pd

# Load the Excel file
file_path = r'C:\Users\lion\Desktop\JEOPARDY_CSV.xlsx'  # Update with your file path
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe
print(df.head())

# Strip any leading or trailing spaces from column names
df.columns = df.columns.str.strip()

# Check for missing values
print(df.isnull().sum())

# Handle missing values (if any)
df.dropna(inplace=True)  # Drop rows with any missing values

# Basic statistics
print(df.describe())

# Value counts for categorical columns
print(df['Category'].value_counts().head(10))
print(df['Round'].value_counts())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Update with your actual file path
file_path = r'C:\Users\lion\Desktop\JEOPARDY_CSV.xlsx'
df = pd.read_excel(file_path)

# Strip any leading or trailing spaces from column names
df.columns = df.columns.str.strip()

# Clean the 'Value' column
# Remove any leading/trailing spaces in 'Value' entries
df['Value'] = df['Value'].str.strip()

# Replace non-numeric values with a default numeric value (0 in this case)
df['Value'].replace(to_replace=r'[^0-9]', value='0', regex=True, inplace=True)

# Convert 'Value' to numeric
df['Value'] = pd.to_numeric(df['Value'])

# Ensure 'Value' is in float format
df['Value'] = df['Value'].astype(float)

# Convert 'Air Date' to datetime
df['Air Date'] = pd.to_datetime(df['Air Date'])

# Extract only the date part from 'Air Date'
df['Air Date'] = df['Air Date'].dt.date

# Distribution of question values
plt.figure(figsize=(10, 6))
df['Value'].value_counts().sort_index().plot(kind='bar')
plt.title('Distribution of Question Values')
plt.xlabel('Value')
plt.ylabel('Count')
print(plt.show())

# Plot the number of questions over time
plt.figure(figsize=(10, 6))
df.groupby('Air Date').size().plot()
plt.title('Number of Questions Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Questions')
print(plt.show())

import pandas as pd

output_path = r'C:\Users\lion\Desktop\Modified_JEOPARDY_CSV.xlsx'
with pd.ExcelWriter(output_path) as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
print(f"Data has been successfully written to {output_path}")
writer.save()