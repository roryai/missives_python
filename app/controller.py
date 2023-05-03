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
        self.clear_terminal_window()
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
        self.record_missive(name, message)

    def get_name(self):
        OperatorMessage('what_is_your_name')
        name = input()
        # two or more letters only of any case
        if re.search("^[a-zA-Z]{2,}$", name):
            return name
        else:
            OperatorMessage('name_only_letters')
            return self.get_name()

    def get_message(self):
        OperatorMessage('what_is_your_message')
        message = input()
        if len(message) < 10:
            OperatorMessage('message_too_short')
            return self.get_message()
        return message

    def record_missive(self, name, message):
        missive = Missive(name, message)
        self.missive_gateway.insert_missive(missive)
        OperatorMessage('missive_recorded')
        self.enter_to_continue()

    def display_random_missive(self):
        self.clear_terminal_window()
        record = self.missive_gateway.select_one_random_missive()
        missive = Missive.init_from_record(record)
        missive.display_missive()
        self.display_another_missive_or_continue()

    def display_time_machine_info(self):
        self.clear_terminal_window()
        OperatorMessage('time_machine_info')
        self.enter_to_continue()

    def enter_to_continue(self):
        OperatorMessage('enter_to_continue')
        input()

    def clear_terminal_window(self):
        print("\033[H\033[J", end="")

    def display_another_missive_or_continue(self):
        OperatorMessage('display_another_missive_or_continue')
        if input() == 'r':
            self.display_random_missive()
        else:
            self.flow_menu()

Controller().flow_menu()
