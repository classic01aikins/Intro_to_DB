import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',      # Replace with your MySQL username
            password='your_password'   # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error while creating database: {e}")
            finally:
                cursor.close()
                connection.close()
                print("MySQL connection closed.")
    except Error as e:
        print(f"Failed to connect to MySQL server: {e}")

if __name__ == "__main__":
    create_database()

