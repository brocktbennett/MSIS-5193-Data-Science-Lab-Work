# Import necessary modules
from mysql.connector import connection


# Function to establish and return a MySQL database connection
def establish_connection():
    """
    Establishes a MySQL database connection and returns the connection object.

    Returns:
        cnx (MySQLConnection): The MySQL connection object.
    """
    cnx = connection.MySQLConnection(
        user='readonlyuser',  # User name for the MySQL connection
        password='Msis5193Fall2023',  # Password for the MySQL connection
        host='34.70.89.75',  # Host address of the MySQL server
        database='classicmodels'  # Database name to connect to
    )
    return cnx


# Function to show all tables in the database
def show_tables(cursor):
    """
    Prints the names of all tables in the database.

    Parameters:
        cursor (MySQLCursor): The MySQL cursor object to execute SQL statements.
    """
    cursor.execute("SHOW TABLES")  # SQL command to show tables
    print("Tables in database:")
    for table in cursor:
        print(table)


# Function to show all records in the 'employees' table
def show_employees(cursor):
    """
    Prints all records in the 'employees' table along with the column headers.

    Parameters:
        cursor (MySQLCursor): The MySQL cursor object to execute SQL statements.
    """
    # Execute the SQL query to select all records from 'employees'
    cursor.execute("SELECT * FROM employees")

    # Fetch column headers from the cursor description
    column_headers = [desc[0] for desc in cursor.description]

    # Print column headers
    print("Column Headers:", column_headers)

    # Print the records under the headers
    print("Records in table 'employees':")
    for record in cursor:
        print(record)


# Main function that calls the above functions
def main():
    """
    Main function that establishes a MySQL connection, shows tables and employee records,
    then closes the connection.
    """
    # Establish a MySQL connection using the establish_connection function
    cnx = establish_connection()

    # Create a cursor object to execute SQL queries
    cursor = cnx.cursor()

    # Show the names of all tables in the database
    show_tables(cursor)

    # Show all records in the 'employees' table
    show_employees(cursor)

    # Close the cursor and the MySQL connection to free up resources
    cursor.close()
    cnx.close()


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
