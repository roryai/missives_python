from missive import Missive
from missive_gateway import MissiveGateway
from operator_message import OperatorMessage
from db_controller import DatabaseController
import re


class Controller:

    def __init__(self):
        self.missive_gateway = \
            MissiveGateway(DatabaseController, '/Users/rory/code/missives_python/missives_staging.db')

    def flow_menu(self):
        OperatorMessage('read_write_learn')
        user_input = input()
        match user_input:
            case 'w':
                self.get_input()
            case 'r':
                self.display_random_missive()
            case 'l':
                self.display_time_machine_info()
            case _:
                OperatorMessage('input_not_recognised')
        self.flow_menu()

    def get_input(self):
        name = self.get_name()
        message = self.get_message()
        missive = Missive(name, message)
        OperatorMessage('missive_recorded')
        self.missive_gateway.insert_missive(missive)

    def get_name(self):
        OperatorMessage('what_is_your_name')
        name = input()
        # only two or more letters of any case
        if re.search("^[a-zA-Z]{2,}$", name):
            return name
        else:
            OperatorMessage('name_only_letters')
            self.get_name()

    def get_message(self):
        OperatorMessage('what_is_your_message')
        message = input()
        if len(message) < 10:
            OperatorMessage('message_too_short')
            # bug: if this loops new input isn't recorded. only 1st input ever returned
            # can't be recursive
            self.get_message()
        return message

    def display_random_missive(self):
        record = self.missive_gateway.select_one_random_missive()
        missive = Missive.init_from_record(record)
        missive.display_missive()

    def display_time_machine_info(self):
        OperatorMessage('time_machine_info')

cont = Controller()
cont.flow_menu()
