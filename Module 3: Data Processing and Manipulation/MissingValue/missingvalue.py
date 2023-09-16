import pandas as pd
from sklearn.impute import SimpleImputer

# Define file paths for datasets
loan_file_path = "/Users/brocktbennett/GitHub/Project Data/train_Loan.csv"
price_file_path = "/Users/brocktbennett/GitHub/Project Data/prod_prices.csv"

# Read the 'loan' dataset with missing values
loan = pd.read_csv(loan_file_path)

# Select the rows that have at least one missing value
loan_with_missing_values = loan[loan.isnull().any(axis=1)].head()

# Drop the rows with missing values
loan_cleaned = loan.dropna(axis=0)

# Show the number of missing values for each column after cleaning
print("Number of missing values in 'loan' dataset after cleaning:")
print(loan_cleaned.isnull().sum())
print()  # Add a blank line for separation

# Delete the 'Dependents' column
loan_cleaned = loan_cleaned.drop(['Dependents'], axis=1)

# Show columns with missing values after dropping 'Dependents'
print("Number of missing values in 'loan' dataset after dropping 'Dependents' column:")
print(loan_cleaned.isnull().sum())
print()  # Add a blank line for separation

# Impute the 'Married' column using the most common value
loan['Married'] = loan['Married'].fillna(loan['Married'].mode()[0])

# Impute the 'Self_Employed' column using the most common value
loan['Self_Employed'] = loan['Self_Employed'].fillna(loan['Self_Employed'].mode()[0])

# Impute the 'LoanAmount' using the mean value
loan['LoanAmount'] = loan['LoanAmount'].fillna(loan['LoanAmount'].mean())

# Read the 'price' dataset
price = pd.read_csv(price_file_path)

# Show columns with missing values in the 'price' dataset
print("Number of missing values in 'price' dataset:")
print(price.isnull().sum())
print()  # Add a blank line for separation

# Forward-fill missing values in the 'price' column
price[['price']] = price[['price']].fillna(method='ffill')

# Show columns with missing values after forward-filling
print("Number of missing values in 'price' dataset after forward-filling:")
print(price.isnull().sum())
print()  # Add a blank line for separation

# Initialize the imputer using SimpleImputer in sklearn, use the most frequent value to impute
imputer = SimpleImputer(strategy='most_frequent')

# Impute 'Gender' using the most frequent value in the column
loan[['Gender']] = imputer.fit_transform(loan[['Gender']])

# Initialize the imputer using SimpleImputer in sklearn, use a new value 'unknown' to impute
imputer_const = SimpleImputer(strategy='constant', fill_value='unknown')

# Impute 'Gender' using the new value 'unknown'
loan[['Gender']] = imputer_const.fit_transform(loan[['Gender']])
