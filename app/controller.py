from app.missive import Missive
from app.missive_gateway import MissiveGateway
from app.operator_message import OperatorMessage
from app.db_controller import DatabaseController
from app.input_syntax_verifier import InputSyntaxVerifier


INPUT_PROMPT = '-> '


class Controller:

    def __init__(self):
        self.missive_gateway = MissiveGateway(DatabaseController, '../missives_live.db')
        self.verifier = InputSyntaxVerifier()

    def flow_menu(self, error_message=None):
        self.__pre_flow(error_message)
        match input(INPUT_PROMPT):
            case 'w':
                missive = self.__get_input()
                self.__record_missive(missive)
            case 'r':
                self.__display_random_missive()
            case 'l':
                self.__display_time_machine_info()
            case _:
                self.flow_menu('input_not_recognised')
        self.flow_menu()

    def __pre_flow(self, error_message):
        self.__clear_terminal_window()
        if error_message:
            OperatorMessage(error_message)
        OperatorMessage('read_write_learn')

    def __get_input(self):
        name = self.__get_name()
        message = self.__get_message()
        return self.__confirm_submission(name, message)

    def __confirm_submission(self, name, message):
        OperatorMessage('confirm_submission')
        confirmation = input(INPUT_PROMPT)
        if confirmation == 'y':
            return Missive(name, message)
        elif confirmation == 'n':
            return self.__get_input()
        else:
            OperatorMessage('input_not_recognised')
            return self.__confirm_submission(name, message)

    def __get_name(self):
        OperatorMessage('what_is_your_name')
        name = input(INPUT_PROMPT)
        if self.verifier.check_name(name):
            return name
        else:
            OperatorMessage('name_only_letters')
            return self.__get_name()

    def __get_message(self):
        OperatorMessage('what_is_your_message')
        message = input(INPUT_PROMPT)
        if self.verifier.check_message_min_length(message) is False:
            OperatorMessage('message_too_short')
            return self.__get_message()
        return message

    def __record_missive(self, missive):
        if self.verifier.check_message_max_length(missive.message) is False:
            OperatorMessage('message_partially_recorded')
            missive.message = missive.message[0:1000]
        self.missive_gateway.insert_missive(missive)
        OperatorMessage('missive_recorded')  # TODO make this dependent on success
        self.__enter_to_continue()

    def __display_random_missive(self):
        record = self.missive_gateway.select_one_random_missive()
        if record:
            missive = Missive.init_from_record(record)
            self.__clear_terminal_window()
            missive.display_missive()
            self.__display_another_missive_or_continue()
        else:
            self.__no_records_found()

    def __display_time_machine_info(self):
        self.__clear_terminal_window()
        OperatorMessage('time_machine_info')
        self.__enter_to_continue()

    def __enter_to_continue(self):
        OperatorMessage('enter_to_continue')
        input()

    def __clear_terminal_window(self):
        print("\033[H\033[J", end="")

    def __display_another_missive_or_continue(self):
        OperatorMessage('display_another_missive_or_continue')
        if input() == 'r':
            self.__display_random_missive()
        else:
            self.flow_menu()

    def __no_records_found(self):
        OperatorMessage('no_records_found')
        self.__enter_to_continue()
