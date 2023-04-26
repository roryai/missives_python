import sqlite3
from sqlite3 import Error


class DatabaseController:

    def __init__(self, path="/Users/rory/code/missives_python/missives.db"):
        self.connection = self.init_db(path)

    def init_db(self, path):
        connection = self.connect_to_db(path)
        self.execute_query(connection, self.create_missives_table_statement())
        return connection

    def connect_to_db(self, path):
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

    def select_one_random_missive_statement(self):
        return """
        SELECT * FROM missives WHERE id IN (SELECT id FROM missives ORDER BY RANDOM() LIMIT 1);
        """

    def select_missive_by_name_statement(self, name):
        return f"""
        SELECT * FROM missives WHERE name = '{name}';
        """

    def delete_all_records_statement(self):
        return """
        DELETE FROM missives;
        """

    def count_missives_statement(self):
        return """
        SELECT COUNT(*) FROM missives;
        """

    def insert_missive(self, missive):
        self.execute_query(self.connection, self.insert_missive_statement(missive))

    def select_one_random_missive(self):
        return self.execute_read_query(self.connection, self.select_one_random_missive_statement())[0]

    def select_missive_by_name(self, name):
        return self.execute_read_query(self.connection, self.select_missive_by_name_statement(name))[0]

    def delete_all_missives(self):
        self.execute_query(self.connection, self.delete_all_records_statement())

    def count_missives(self):
        return self.execute_read_query(self.connection, self.count_missives_statement())
