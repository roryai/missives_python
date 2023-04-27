from missive import Missive
from missive_gateway import MissiveGateway
from db_controller import DatabaseController


class Controller:

    def __init__(self):
        self.missive_gateway = \
            MissiveGateway(DatabaseController, '/Users/rory/code/missives_python/missives_staging.db')

    def flow_menu(self):
        print('Would you like to write a missive, read a missive, or learn more about this time machine?')
        print("Type 'w' to write, 'r' to read, or 'l' to learn more, then hit enter.")
        branch = input()
        match branch:
            case 'w':
                self.get_input()
            case 'r':
                self.display_random_missive()
            case 'l':
                self.display_time_machine_info()
            case _:
                print("Input not recognised, please try again.")
                print("Type ")
        self.flow_menu()

    def get_input(self):
        print('What is your name?')
        name = input()
        print('What message would you like to send to the future?')
        message = input()
        missive = Missive(name, message)
        self.missive_gateway.insert_missive(missive)

    def display_random_missive(self):
        record = self.missive_gateway.select_one_random_missive()
        missive = Missive.init_from_record(record)
        missive.display_missive()

    def display_time_machine_info(self):
        print("Fill in time machine info")

cont = Controller()
cont.flow_menu()
