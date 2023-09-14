import pandas as pd

# Read CSV File
csv_file_path = "/Users/brocktbennett/GitHub/Project Data/Salaries.csv"
df_salaries = pd.read_csv(csv_file_path)

# Print the first 10 records
print("---------Printing out the first 10 records-------------")
print(df_salaries.head(10))

# Get the dimensions of the DataFrame
num_rows, num_columns = df_salaries.shape
print("---------List number of rows and columns-------------")
print(f"Number of columns: {num_columns}")
print(f"Number of rows: {num_rows}")

# Print Data Types of Each Column
print("Data Types of Each Column:")
print(df_salaries.dtypes)
print()

# Select and print the 'salary' column
salary_column = df_salaries['salary']
print("---------Select Column 'salary'-------------")
print(salary_column.head())

# Select and print specific rows and columns using iloc
print("---------Select Rows 10 to 19 and Columns 0, 3, 4, 5 using iloc-------------")
selected_data = df_salaries.iloc[10:20, [0, 3, 4, 5]]
print(selected_data)

# Data Slicing Examples
print("---------Data Slicing Examples-------------")
first_row = df_salaries.iloc[0]  # First row of the DataFrame
last_row = df_salaries.iloc[-1]  # Last row of the DataFrame

# Data Sorting Examples
print("---------Data Sorting Examples-------------")
# Sort by the 'salary' column in ascending order
sales_sorted_asc = df_salaries.sort_values(by='salary')
print(sales_sorted_asc[['Unnamed: 0', 'rank', 'discipline', 'yrs.since.phd', 'yrs.service', 'sex', 'salary']].head(10))

# Sort by the 'salary' column in descending order
sales_sorted_desc = df_salaries.sort_values(by='salary', ascending=False)
print(sales_sorted_desc[['Unnamed: 0', 'rank', 'discipline', 'yrs.since.phd', 'yrs.service', 'sex', 'salary']].head(10))
