import pandas as pd
from sklearn.impute import SimpleImputer

# Read the 'loan' dataset with missing values (modify the file path accordingly)
loan = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/train_Loan.csv")

# Select the rows that have at least one missing value
loan_with_missing_values = loan[loan.isnull().any(axis=1)].head()

# Drop the rows with missing values
loan_cleaned = loan.dropna(axis=0)

# Show the number of missing values for each column
print(loan_cleaned.isnull().sum())

# Delete the 'Dependents' column
loan_cleaned = loan_cleaned.drop(['Dependents'], axis=1)

# Show columns with missing values
print(loan_cleaned.isnull().sum())

# Impute the 'Married' column using the most common value
loan['Married'] = loan['Married'].fillna(loan['Married'].mode()[0])

# Impute the 'Self_Employed' column using the most common value
loan['Self_Employed'] = loan['Self_Employed'].fillna(loan['Self_Employed'].mode()[0])

# Impute the 'LoanAmount' using the mean value
loan['LoanAmount'] = loan['LoanAmount'].fillna(loan['LoanAmount'].mean())

# Read the 'price' dataset (modify the file path accordingly)
price = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/prod_prices.csv")

# Show columns with missing values
print(price.isnull().sum())

# Forward-fill missing values in the 'price' column
price[['price']] = price[['price']].fillna(method='ffill')

# Show columns with missing values
print(price.isnull().sum())

# Initialize the imputer using SimpleImputer in sklearn, use the most frequent value to impute
imputer = SimpleImputer(strategy='most_frequent')

# Impute 'Gender' using the most frequent value in the column
loan[['Gender']] = imputer.fit_transform(loan[['Gender']])

# Initialize the imputer using SimpleImputer in sklearn, use a new value 'unknown' to impute
imputer_const = SimpleImputer(strategy='constant', fill_value='unknown')

# Impute 'Gender' using the new value 'unknown'
loan[['Gender']] = imputer_const.fit_transform(loan[['Gender']])
