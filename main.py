
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file (replace 'your_file.csv' with the actual file path)
df_csv = pd.read_csv('/rawData/fire-over-5hecs.csv')

# Skip irrelevant rows and columns to get to the actual data
df_csv_cleaned = df_csv.iloc[2:]
df_csv_cleaned.columns = df_csv.iloc[1]

# Rename the columns for easier access
df_csv_cleaned.rename(columns={
    'Unnamed: 23': '워드1',
    'Unnamed: 24': '워드2',
    'Unnamed: 25': '워드3',
    'Unnamed: 26': '워드4',
    'Unnamed: 27': '워드5',
}, inplace=True)

# Drop any rows where 'log' or 'Word' columns are NaN
df_csv_cleaned.dropna(subset=['워드1', '워드2', '워드3', '워드4', '워드5', 'log'], inplace=True)

# Convert 'Word' columns to string type and 'log' column to float type
for col in ['워드1', '워드2', '워드3', '워드4', '워드5']:
    df_csv_cleaned[col] = df_csv_cleaned[col].astype(str)
df_csv_cleaned['log'] = df_csv_cleaned['log'].astype(float)

# Create a DataFrame for consolidated mean log values across all 'Word' columns
consolidated_mean_log_values_csv = pd.concat([df_csv_cleaned[col] for col in ['워드1', '워드2', '워드3', '워드4', '워드5']], 
                                             keys=['워드1', '워드2', '워드3', '워드4', '워드5']).reset_index()
consolidated_mean_log_values_csv.columns = ['Word_Column', 'Index', 'Category']
consolidated_mean_log_values_csv['log'] = df_csv_cleaned['log'].repeat(5).reset_index(drop=True)

# Calculate mean log value for each category across all 'Word' columns
group_means_consolidated_csv = consolidated_mean_log_values_csv.groupby('Category')['log'].mean().reset_index()
group_means_consolidated_csv.columns = ['Category', 'Consolidated_Mean_Log_Value']

# Sort by 'Consolidated_Mean_Log_Value' and take the top 10 categories
top10_overall_consolidated_csv = group_means_consolidated_csv.sort_values('Consolidated_Mean_Log_Value', ascending=False).head(10)

# Plotting the data
plt.figure(figsize=(15, 8))
sns.barplot(data=top10_overall_consolidated_csv, x='Category', y='Consolidated_Mean_Log_Value')
plt.title('Top 10 Categories by Consolidated Mean Log Value Across All Word Columns')
plt.xlabel('Category')
plt.ylabel('Consolidated Mean Log Value')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
