import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(
    user='readonlyuser',
    password='Msis5193Fall2023',
    host='34.70.89.75',
    database='northwind'
)

# Initialize a cursor for executing SQL queries
cursor = cnx.cursor()

try:
    # Use a SQL query to fetch table names from the information schema
    cursor.execute("SHOW TABLES")

    # Fetch all the table names
    table_names = [row[0] for row in cursor]

    # Print the list of available datasets (tables)
    if table_names:
        print("Available datasets (tables):")
        for table_name in table_names:
            print(table_name)
    else:
        print("No datasets found in the database.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the database connection
    cursor.close()
    cnx.close()
