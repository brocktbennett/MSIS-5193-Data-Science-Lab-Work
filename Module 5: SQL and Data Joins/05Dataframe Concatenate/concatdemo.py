import pandas as pd

# Create demo dataframes
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

# Concatenate dataframes and save to a new variable
result = pd.concat([df1, df2, df3])

# Show the result
print("Concatenated Dataframes:")
print(result)

# Define a series as a list
series1 = ['X0', 'X1', 'X2', 'X3']

# Convert the series into a dataframe and add a column name 'X'
s1 = pd.Series(series1, name='X')

# Concatenate df1 and s1 by column-wise
result = pd.concat([df1, s1], axis=1)

# Show the result
print("\nConcatenated DataFrame and Series:")
print(result)

# Load data from CSV files
try:
    Salary_1 = pd.read_csv(r'C:\Users\xiluo\Documents\MSIS 5193 Programming I DS and Analytics\datasets-main\datasets-main\basic_salary - 1.csv')
    Salary_2 = pd.read_csv(r'C:\Users\xiluo\Documents\MSIS 5193 Programming I DS and Analytics\datasets-main\datasets-main\basic_salary - 2.csv')

    # Concatenate dataframes
    appendsalary = pd.concat([Salary_1, Salary_2])

    # Show the result
    print("\nConcatenated Salary Dataframes:")
    print(appendsalary)

except Exception as e:
    print(f"Error: {e}")
