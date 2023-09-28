# Import the pandas library
import pandas as pd

# Load data from CSV files into DataFrames with new names
customers_df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/customers.csv", encoding='latin-1')
employees_df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/employees.csv", encoding='latin-1')
orders_df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/orders.csv", encoding='latin-1')

# Apply a full outer join between customers_df and orders_df on the 'customerNumber' column
df_outer = pd.merge(customers_df, orders_df, on="customerNumber", how='outer')

# Set an option to display all columns
pd.set_option('display.max_columns', None)

# Print the result of the full outer join
print("Full Outer Join Result:")
print(df_outer)

# Apply a left join between customers_df and employees_df on 'salesRepEmployeeNumber' and 'employeeNumber'
df_left = pd.merge(customers_df, employees_df, left_on='salesRepEmployeeNumber', right_on='employeeNumber', how='left')

# Print the result of the left join
print("\nLeft Join Result:")
print(df_left)

# Apply an inner join between customers_df and employees_df on 'salesRepEmployeeNumber' and 'employeeNumber'
df_inner = pd.merge(customers_df, employees_df, left_on='salesRepEmployeeNumber', right_on='employeeNumber', how='inner')

# Print the result of the inner join
print("\nInner Join Result:")
print(df_inner)

# Apply a right join between customers_df and employees_df on 'salesRepEmployeeNumber' and 'employeeNumber'
df_right = pd.merge(customers_df, employees_df, left_on='salesRepEmployeeNumber', right_on='employeeNumber', how='right')

# Print the result of the right join
print("\nRight Join Result:")
print(df_right)
