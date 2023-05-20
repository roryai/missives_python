from missives_python.app.missive import Missive
from missives_python.app.missive_gateway import MissiveGateway
from missives_python.app.operator_message import OperatorMessage
from missives_python.app.db_controller import DatabaseController
from missives_python.app.input_syntax_verifier import InputSyntaxVerifier


INPUT_PROMPT = '-> '


class Controller:

    def __init__(self):
        self.missive_gateway = MissiveGateway(DatabaseController,
                                              '/Users/rory/code/missives_python/missives_live.db')
        self.verifier = InputSyntaxVerifier()

    def flow_menu(self, error_message=None):
        self.pre_flow(error_message)
        match input(INPUT_PROMPT):
            case 'w':
                missive = self.get_input()
                self.record_missive(missive)
            case 'r':
                self.display_random_missive()
            case 'l':
                self.display_time_machine_info()
            case _:
                self.flow_menu('input_not_recognised')
        self.flow_menu()

    def pre_flow(self, error_message):
        self.clear_terminal_window()
        if error_message:
            OperatorMessage(error_message)
        OperatorMessage('read_write_learn')

    def get_input(self):
        name = self.get_name()
        message = self.get_message()
        return self.confirm_submission(name, message)

    def confirm_submission(self, name, message):
        OperatorMessage('confirm_submission')
        confirmation = input(INPUT_PROMPT)
        if confirmation == 'y':
            return Missive(name, message)
        elif confirmation == 'n':
            return self.get_input()
        else:
            OperatorMessage('input_not_recognised')
            return self.confirm_submission(name, message)

    def get_name(self):
        OperatorMessage('what_is_your_name')
        name = input(INPUT_PROMPT)
        if self.verifier.check_name(name):
            return name
        else:
            OperatorMessage('name_only_letters')
            return self.get_name()

    def get_message(self):
        OperatorMessage('what_is_your_message')
        message = input(INPUT_PROMPT)
        if self.verifier.check_message_min_length(message) is False:
            OperatorMessage('message_too_short')
            return self.get_message()
        return message

    def record_missive(self, missive):
        if self.verifier.check_message_max_length(missive.message) is False:
            OperatorMessage('message_partially_recorded')
            missive.message = missive.message[0:1000]
        self.missive_gateway.insert_missive(missive)
        OperatorMessage('missive_recorded')  # TODO make this dependent on success
        self.enter_to_continue()

    def display_random_missive(self):
        record = self.missive_gateway.select_one_random_missive()
        missive = Missive.init_from_record(record)
        self.clear_terminal_window()
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
