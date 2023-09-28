from mysql.connector import connection

# Connect to the DB server
cnx = connection.MySQLConnection(
    user='readonlyuser',
    password='Msis5193Fall2023',
    host='34.70.89.75',
    database='classicmodels'
)

# Initialize the cursor
cursor = cnx.cursor()

try:
    # INNER JOIN: Select customer information along with their respective sales representatives' information.
    cursor.execute("""
    SELECT customers.customerNumber, customers.customerName, employees.employeeNumber, employees.firstName, employees.lastName
    FROM customers
    INNER JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber;
    """)

    print("INNER JOIN Results:")
    for row in cursor:
        print(row)

    # LEFT JOIN: Select all customers and their sales representatives (if available).
    cursor.execute("""
    SELECT customers.customerNumber, customers.customerName, employees.employeeNumber, employees.firstName, employees.lastName
    FROM customers
    LEFT JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber;
    """)

    print("\nLEFT JOIN Results:")
    for row in cursor:
        print(row)

    # RIGHT JOIN: Select all employees and their corresponding customers (if any).
    cursor.execute("""
    SELECT employees.employeeNumber, employees.firstName, employees.lastName, customers.customerNumber, customers.customerName
    FROM employees
    RIGHT JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber;
    """)

    print("\nRIGHT JOIN Results:")
    for row in cursor:
        print(row)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close DB connection
    cursor.close()
    cnx.close()
