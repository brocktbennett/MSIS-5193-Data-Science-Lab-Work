import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Read the 'food' dataset
food = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/groceries.csv")

# Print basic information about the dataset
print("Basic Information about the 'food' dataset:")
print(food.info())
print()  # Add a blank line for separation

# Show summary statistics for numeric columns
print("Summary Statistics for Numeric Columns:")
print(food.describe())
print()  # Add a blank line for separation

# Show the distribution of product groups
print("Distribution of Product Groups:")
product_group_distribution = food['product_group'].value_counts()
print(product_group_distribution)
print()  # Add a blank line for separation

# Visualize the distribution of product groups (you can add data visualization code here)

# Analyze sales trends over time
food['sales_date'] = pd.to_datetime(food['sales_date'])
food['year'] = food['sales_date'].dt.year
food['month'] = food['sales_date'].dt.month

# Show monthly sales trends
monthly_sales_trends = food.groupby(['year', 'month'])['sales_quantity'].sum()
print("Monthly Sales Trends:")
print(monthly_sales_trends)
print()  # Add a blank line for separation

# Visualize monthly sales trends (you can add data visualization code here)

# Analyze the relationship between price and sales_quantity
correlation = food['price'].corr(food['sales_quantity'])
print(f"Correlation between Price and Sales Quantity: {correlation:.2f}")
print()  # Add a blank line for separation

# Perform additional data exploration and analysis as needed

# Save the cleaned and analyzed dataset to a new CSV file
food.to_csv("cleaned_and_analyzed_food_data.csv", index=False)
