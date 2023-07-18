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
             location TEXT NOT NULL,
             gathering TEXT NOT NULL
         );
         """

    def insert_missive(self, missive):
        statement = f"""
        INSERT INTO
            missives (name, message, creation_time, location, gathering)
        VALUES
            (?, ?, ?, ?, ?);
         """
        values = [missive.name, missive.message, missive.creation_time, missive.location, missive.gathering]
        self.db_controller.execute_query(statement, values)

    def select_one_random_missive(self):
        statement = """
        SELECT * FROM missives WHERE id IN (SELECT id FROM missives ORDER BY RANDOM() LIMIT 1);
        """  # TODO: handle case where no record is found
        return self.db_controller.execute_read_query(statement)[0]

    def select_missive_by_name(self, name):
        statement = f"""
        SELECT * FROM missives WHERE name = '{name}';
        """
        return self.db_controller.execute_read_query(statement)[0]

    def delete_all_missives(self):
        statement = """
        DELETE FROM missives;
        """
        self.db_controller.execute_query(statement, [])
