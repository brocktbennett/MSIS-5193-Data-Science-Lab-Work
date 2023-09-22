import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data into dataframe
loan = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/train_Loan.csv")

# Data Exploration
# Check first few rows of the dataset
print(loan.head())

# Check for missing values
print("\nMissing values by column:")
print(loan.isnull().sum())

# Basic statistics of LoanAmount
print("\nStatistics for LoanAmount:")
print(loan['LoanAmount'].describe())

# Visualizations
# Histogram with specified bin boundaries
plt.hist(loan['LoanAmount'].dropna(), bins=[100, 200, 300, 400, 500])  # dropping NA values
plt.title('Histogram with Specified Bins')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.show()

# Histogram with auto bin calculation
plt.hist(loan['LoanAmount'].dropna(), bins=10)  # dropping NA values
plt.title('Histogram with 10 Bins')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.show()

# Boxplot for LoanAmount to check for outliers
sns.boxplot(x=loan['LoanAmount'])
plt.title('Box Plot for Loan Amount')
plt.show()

# KDE plot for LoanAmount
sns.kdeplot(loan['LoanAmount'].dropna(), fill=True)
plt.title('Kernel Density Estimation (KDE) for Loan Amount')
plt.show()

# Analysis
# Assuming there's a categorical variable called 'LoanStatus' (or any other relevant column)
# Group by 'LoanStatus' and see the mean loan amount
print("\nMean Loan Amount by LoanStatus:")
print(loan.groupby('Loan_Status')['LoanAmount'].mean())

