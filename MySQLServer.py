import mysql.connector
from mysql.connector import Error

def create_database():
    # Database connection parameters
    host = 'localhost'  # Change if necessary
    user = 'your_username'  # Replace with your MySQL username
    password = 'your_password'  # Replace with your MySQL password

    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
