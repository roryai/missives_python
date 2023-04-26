class MissiveGateway:

    def __init__(self, db_controller, db_path):
        self.db_controller = db_controller(table_init_statement=self.create_missives_table_statement(),
                                           path=db_path)

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

    def select_all_missives_statement(self):
        return """
        SELECT * FROM missives;
        """

    def insert_missive(self, missive):
        self.db_controller.execute_query(self.insert_missive_statement(missive))

    def select_one_random_missive(self):
        return self.db_controller.execute_read_query(self.select_one_random_missive_statement())[0]

    def select_missive_by_name(self, name):
        return self.db_controller.execute_read_query(self.select_missive_by_name_statement(name))[0]

    def delete_all_missives(self):
        self.db_controller.execute_query(self.delete_all_records_statement())

    def count_missives(self):
        return self.db_controller.execute_read_query(self.count_missives_statement())[0][0]

    def select_all_missives(self):
        return self.db_controller.execute_read_query(self.select_all_missives_statement())
