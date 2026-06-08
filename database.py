import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

class DatabaseManager:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

    def get_connection(self):
        """Establishes and returns a database connection."""
        try:
            return mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except Error as e:
            print(f"Database Connection Failed: {e}")
            return None

    def fetch_user_expenses(self, user_id: int):
        """Retrieves aggregated expense data for a specific user."""
        conn = self.get_connection()
        if not conn:
            return [], []

        try:
            cursor = conn.cursor()
            # Parameterized query to prevent SQL Injection
            query = """
                SELECT category, SUM(amount) 
                FROM transactions 
                WHERE user_id = %s AND type = 'Expense' 
                GROUP BY category
            """
            cursor.execute(query, (user_id,))
            data = cursor.fetchall()
            
            categories = [row[0] for row in data]
            amounts = [float(row[1]) for row in data]
            return categories, amounts
            
        finally:
            # Ensure resources are always cleaned up
            if conn.is_connected():
                cursor.close()
                conn.close()
