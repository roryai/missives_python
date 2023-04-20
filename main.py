from app.db_controller import DatabaseController
from app.missive import Missive
from datetime import datetime


if __name__ == '__main__':
    # init db
    db_controller = DatabaseController()
    connection = db_controller.connect_to_db()

    # drop missives if exists
    delete_statement = "DROP TABLE IF EXISTS missives;"
    db_controller.execute_query(connection, delete_statement)

    # create table
    db_controller.execute_query(connection, db_controller.create_missives_table_statement())

    # create and insert one test missive
    missive = Missive(name="Rory", message="Hello there", creation_time=datetime(2023, 4, 20, 8, 45, 20, 56178))
    db_controller.execute_query(connection, db_controller.insert_missive_statement(missive))

    # read data
    select_one_random_record = "SELECT * FROM missives WHERE id IN (SELECT id FROM missives ORDER BY RANDOM() LIMIT 1)"
    users = db_controller.execute_read_query(connection, select_one_random_record)

    name = users[0][1]
    message = users[0][2]
    creation_time = users[0][3]
    location = users[0][4]
    missive = Missive(name=name,
                      message=message,
                      creation_time=datetime.strptime(creation_time, '%Y-%m-%d %H:%M:%S.%f'),
                      location=location
                      )
    missive.display_missive()
