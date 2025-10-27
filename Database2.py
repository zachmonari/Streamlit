import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='mydatabase',
            user='root',
            password='Zachary4637?'  # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Connected to MySQL database")
            return connection

    except Error as e:
        print(f"Error: {e}")
        return None


# Test the connection
connection = create_connection()