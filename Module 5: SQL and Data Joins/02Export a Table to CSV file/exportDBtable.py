import csv
import os
from mysql.connector import connection

# Function to export data from a table to a CSV file
def export_table_to_csv(table_name, file_name):
    # Connect to the MySQL database
    cnx = connection.MySQLConnection(
        user='readonlyuser',
        password='Msis5193Fall2023',
        host='34.70.89.75',
        database='classicmodels'
    )

    # Initialize a cursor for executing SQL queries
    cursor = cnx.cursor()

    # Select data from the specified table
    cursor.execute(f"SELECT * FROM {table_name}")

    # Get information about the table's columns
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]

    # Specify the file path
    file_path = os.path.join('/Users/brocktbennett/GitHub/Project Data', file_name)

    # Save the table data to a CSV file
    with open(file_path, 'w', newline='') as fp:
        writer = csv.writer(fp)

        # Write the header row with field names to the CSV file
        writer.writerow(field_names)

        # Iterate through the query results and write each row to the CSV file
        for row in cursor:
            writer.writerow(row)

    # Close the database connection
    cnx.close()

# Define a list of datasets to export (table name, file name)
datasets_to_export = [
    ('customers', 'customers.csv'),
    ('employees', 'employees.csv'),
    ('orders', 'orders.csv'),
]

# Initialize a list to keep track of exported datasets
exported_datasets = []

# Iterate through the list and export each dataset
for table_name, file_name in datasets_to_export:
    print(f"Exporting data from '{table_name}' to '{file_name}'")
    export_table_to_csv(table_name, file_name)
    exported_datasets.append(table_name)

# List the remaining datasets
remaining_datasets = [table for table, _ in datasets_to_export if table not in exported_datasets]
if remaining_datasets:
    print("Remaining datasets to export:", ", ".join(remaining_datasets))
else:
    print("All datasets have been exported.")

