# Import Python Libraries
import pandas as pd
print("---------Reading the CSV-------------")
# Read CSV File
df_salaries = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/Salaries.csv")
# The above command has many optional arguments to fine-tune the data import process
# Python and other languages can read excel, index_col, read_stata, read_sas
print("---------printing out the first 10 records-------------")
# Explore data frames, listing 5 if left blank (), or list 10 (10)
# print it out
print(df_salaries.head(10))

print("---------List number of rows and columns-------------")
print(f"Number of columns:{df_salaries.shape[1]}")
print(f"Number of rows:{df_salaries.shape[0]}")
print("Data Types of Each Column: ")
print(df_salaries.dtypes)
print()

