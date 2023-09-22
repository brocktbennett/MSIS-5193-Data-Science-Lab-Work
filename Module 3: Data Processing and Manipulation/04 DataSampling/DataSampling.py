import pandas as pd
import numpy as np

# Define a function for systematic sampling
def systematic_sampling(df, step):
    # Get the indexes of the sampling data
    indexes = np.arange(0, len(df), step=step)
    # Get the subset based on the indexes
    systematic_sample = df.iloc[indexes]
    # Return the new data frame with sampled data
    return systematic_sample

# Load data into a DataFrame
price = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/prod_prices.csv")

# Impute missing data using forward-fill
price[['price']] = price[['price']].fillna(method='ffill')

# Data sampling using systematic sampling
step_size = 5
pricenew = systematic_sampling(price, step_size)

# Show the systematic sample
print("Systematic Sample of 'price' DataFrame:")
print(pricenew)
print()  # Add a blank line for separation

# Modify the file path to your 'train_Loan.csv' file
loan = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/train_Loan.csv")

# Show the size of the 'loan' DataFrame (number of rows, number of columns)
print(f"Size of 'loan' DataFrame: {loan.shape}")

# Check the number of unique values in the 'Property_Area' column
unique_property_areas = loan['Property_Area'].nunique()
print(f"Number of unique Property Areas: {unique_property_areas}")
print()  # Add a blank line for separation

# Sample 100 rows from each unique value of 'Property_Area'
loansample = loan.groupby('Property_Area', group_keys=False).apply(lambda x: x.sample(100))

# Show the sample based on 'Property_Area'
print("Sampled 'loan' DataFrame by 'Property_Area':")
print(loansample)
print()  # Add a blank line for separation

# Sample 60% of the data based on the combination of 'Property_Area' and 'Education'
sample_fraction = 0.6
loansample = loan.groupby(['Property_Area', 'Education'], group_keys=False).apply(lambda x: x.sample(frac=sample_fraction))

# Show the sample based on 'Property_Area' and 'Education'
print("Sampled 'loan' DataFrame by 'Property_Area' and 'Education':")
print(loansample)
