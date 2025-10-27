import mysql.connector
from mysql.connector import Error


class MySQLDatabase:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='mydatabase',
                user='root',
                password='Zachary4637?'
            )
            print("Connected to MySQL successfully!")

        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def create_user(self, name, email, age):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
            values = (name, email, age)

            cursor.execute(query, values)
            self.connection.commit()
            print(f"User {name} created successfully!")

        except Error as e:
            print(f"Error creating user: {e}")

    def read_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")

            users = cursor.fetchall()
            print("\nAll Users:")
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")

            return users

        except Error as e:
            print(f"Error reading users: {e}")

    def update_user(self, user_id, name=None, email=None, age=None):
        try:
            cursor = self.connection.cursor()

            # Build dynamic update query
            updates = []
            values = []

            if name:
                updates.append("name = %s")
                values.append(name)
            if email:
                updates.append("email = %s")
                values.append(email)
            if age:
                updates.append("age = %s")
                values.append(age)

            values.append(user_id)
            query = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"

            cursor.execute(query, values)
            self.connection.commit()
            print(f"User ID {user_id} updated successfully!")

        except Error as e:
            print(f"Error updating user: {e}")

    def delete_user(self, user_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM users WHERE id = %s"

            cursor.execute(query, (user_id,))
            self.connection.commit()
            print(f"User ID {user_id} deleted successfully!")

        except Error as e:
            print(f"Error deleting user: {e}")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")


# Usage example
if __name__ == "__main__":
    db = MySQLDatabase()

    # Create a new user
    db.create_user("Mike Johnson", "mike@email.com", 28)

    # Read all users
    db.read_users()

    # Update a user (assuming user with ID 1 exists)
    db.update_user(1, name="John Updated", age=26)

    # Delete a user
    # db.delete_user(3)

    # Close connection
    db.close_connection()