import sqlite3
from sqlite3 import Error


class DatabaseController:


    def connect_to_db(self, path="/Users/rory/code/missives_python/missives.db"):
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print(f"Error '{e}' occurred with database connection")

        return connection

    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
        except Error as e:
            print(f"Error '{e}' occurred with query")

    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error '{e}' occurred with read query")
        return result

    def create_missives_table_statement(self):
        return """
        CREATE TABLE IF NOT EXISTS missives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            creation_time INTEGER,
            location TEXT NOT NULL
        );
        """

    def insert_missive_statement(self, missive):
        return f"""
        INSERT INTO
            missives (name, message, creation_time, location)
        VALUES
            ('{missive.name}', '{missive.message}', '{missive.creation_time}', '{missive.location}');
        """
