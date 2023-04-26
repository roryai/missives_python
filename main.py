from app.db_controller import DatabaseController
from app.missive import Missive
from app.missive_gateway import MissiveGateway
from datetime import datetime


if __name__ == '__main__':
    missive_gateway = MissiveGateway(DatabaseController, "/Users/rory/code/missives_python/missives_test.db")

    # create and insert one test missive
    missive = Missive(name="Rory",
                      message="Hello there",
                      creation_time=datetime(2023, 4, 20, 8, 45, 20, 56178))
    missive_gateway.insert_missive(missive)

    # select, construct and display random missive
    missive_record = missive_gateway.select_one_random_missive()
    missive = Missive.init_from_record(missive_record)
    missive.display_missive()
