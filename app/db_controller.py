import sqlite3
from sqlite3 import Error


class DatabaseController:

    def __init__(self, table_init_statement=None, path="/Users/rory/code/missives_python/missives.db"):
        self.connection = self.connect_to_db(path)
        if table_init_statement:
            self.execute_query(table_init_statement, [])

    def connect_to_db(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print(f"Error '{e}' occurred with database connection")

        return connection

    def execute_query(self, query, values):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            self.connection.commit()
        except Error as e:
            print(f"Error '{e}' occurred with query")

    def execute_read_query(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error '{e}' occurred with read query")
        return result
