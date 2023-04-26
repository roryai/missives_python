from app.db_controller import DatabaseController
from app.missive import Missive
from app.missive_gateway import MissiveGateway
from datetime import datetime


if __name__ == '__main__':
    missive_gateway = MissiveGateway(DatabaseController, "/Users/rory/code/missives_python/missives_test.db")

    # create and insert one test missive
    missive = Missive(name="Rory",
                      message="Hello there",
                      creation_time=datetime(2023, 4, 20, 8, 45, 20, 56178)
                      )
    missive_gateway.insert_missive(missive)

    # select random missive and map db data to Missive
    missive_record = missive_gateway.select_one_random_missive()
    name = missive_record[1]
    message = missive_record[2]
    creation_time = missive_record[3]
    location = missive_record[4]

    missive = Missive(name=name,
                      message=message,
                      creation_time=datetime.strptime(creation_time, '%Y-%m-%d %H:%M:%S.%f'),
                      location=location
                      )

    missive.display_missive()
