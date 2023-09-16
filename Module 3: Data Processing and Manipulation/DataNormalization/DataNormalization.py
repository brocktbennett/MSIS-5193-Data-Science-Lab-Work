import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing

# Define the file path for the dataset
data_file_path = "/Users/brocktbennett/GitHub/Project Data/train_Loan.csv"

# Read a dataset
loan = pd.read_csv(data_file_path)

# Impute missing values in the 'LoanAmount' column with the mean value
loan['LoanAmount'] = loan['LoanAmount'].fillna(loan['LoanAmount'].mean())

# Initialize Min-Max normalization scaler
scaler = preprocessing.MinMaxScaler()

# Normalize the 'LoanAmount' column using Min-Max scaling
loan[['LoanAmount']] = scaler.fit_transform(loan[['LoanAmount']])

# Show the normalized 'LoanAmount' values
print("Normalized 'LoanAmount' values:")
print(loan[['LoanAmount']])
print()  # Add a blank line for separation

# Initialize Z-score normalization scaler
scaler_zscore = preprocessing.StandardScaler()

# Normalize the 'LoanAmount' column using Z-score scaling
loan[['LoanAmount']] = scaler_zscore.fit_transform(loan[['LoanAmount']])

# Show the normalized 'LoanAmount' values
print("Z-score normalized 'LoanAmount' values:")
print(loan[['LoanAmount']])
print()  # Add a blank line for separation

# Create a DataFrame to demonstrate removing duplicates
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})

# Remove duplicates based on all columns
df_new = df.drop_duplicates()

# Show the results after removing duplicates
print("DataFrame after removing duplicates based on all columns:")
print(df_new)
print()  # Add a blank line for separation

# Remove duplicates based on the 'brand' column
df_new = df.drop_duplicates(subset=['brand'])

# Show the results after removing duplicates based on 'brand'
print("DataFrame after removing duplicates based on 'brand' column:")
print(df_new)
print()  # Add a blank line for separation

# Remove duplicates based on columns 'brand' and 'style', keeping the last occurrence
df_new = df.drop_duplicates(subset=['brand', 'style'], keep='last')

# Show the results after removing duplicates based on 'brand' and 'style'
print("DataFrame after removing duplicates based on 'brand' and 'style', keeping the last occurrence:")
print(df_new)
