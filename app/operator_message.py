import app.styles as styles
from app.printer import Printer


class OperatorMessage:

    def __init__(self, command, printer=Printer()):
        printer.process(self.__selector(command))

    def __selector(self, command):
        match command:
            case 'read_write_learn':
                return self.__read_write_learn()

            case 'what_is_your_name':
                return [{'text': 'What is your name?', 'styling': styles.DEFAULT}]

            case 'what_is_your_message':
                return [{'text': 'What message would you like to send to the future?',
                         'styling': styles.DEFAULT}]

            case 'confirm_submission':
                return self.__confirm_submission()

            case 'input_not_recognised':
                return self.__input_not_recognised()

            case 'name_only_letters':
                return self.__name_only_letters()

            case 'message_too_short':
                return self.__message_too_short()

            case 'message_partially_recorded':
                return self.__message_partially_recorded()

            case 'missive_recorded':
                return [{'text': 'Your missive has been added to the temporal archive, thank you.',
                         'styling': styles.SUCCESS}]

            case 'enter_to_continue':
                return self.__hit_enter_to_continue()

            case 'display_another_missive_or_continue':
                return self.__display_another_missive_or_continue()

            case 'time_machine_info':
                return self.__time_machine_info()

            case 'no_records_found':
                return self.__no_records_found()

            case 'db_operation_failed':
                return self.__db_operation_failed()

    def __read_write_learn(self):
        return [
            {'text': 'Would you like to write a missive, read a missive, or learn more about '
             'this time machine?',
                'styling': styles.DEFAULT},
            {'text': '\nType ',                     'styling': styles.DEFAULT},
            {'text': 'w',                           'styling': styles.HIGHLIGHT},
            {'text': ' to write, ',                 'styling': styles.DEFAULT},
            {'text': 'r',                           'styling': styles.HIGHLIGHT},
            {'text': ' to read, or ',               'styling': styles.DEFAULT},
            {'text': 'l',                           'styling': styles.HIGHLIGHT},
            {'text': ' to learn more, then hit ',   'styling': styles.DEFAULT},
            {'text': 'enter',                       'styling': styles.HIGHLIGHT},
            {'text': '.',                           'styling': styles.DEFAULT},
        ]

    def __confirm_submission(self):
        return [
            {'text': 'Would you like to submit your message, or start again?',
             'styling': styles.DEFAULT},
            {'text': '\nType ',                             'styling': styles.DEFAULT},
            {'text': 'y',                                   'styling': styles.HIGHLIGHT},
            {'text': ' then hit ',                          'styling': styles.DEFAULT},
            {'text': 'enter',                               'styling': styles.HIGHLIGHT},
            {'text': ' to submit your missive, or type ',   'styling': styles.DEFAULT},
            {'text': 'n',                                   'styling': styles.HIGHLIGHT},
            {'text': ' then hit ',                          'styling': styles.DEFAULT},
            {'text': 'enter',                               'styling': styles.HIGHLIGHT},
            {'text': ' to start again.',                    'styling': styles.DEFAULT},
        ]

    def __input_not_recognised(self):
        return [
            {'text': '⚠️', 'styling': styles.WARNING_SIGN},
            {'text': ' Input not recognised, please try again.', 'styling': styles.WARNING_BODY},
            {'text': '⚠️', 'styling': styles.WARNING_SIGN}
        ]
    
    def __name_only_letters(self):
        return [
             {'text': '⚠️', 'styling': styles.WARNING_SIGN},
             {'text': 'Name must begin with letters and not be excessive in length.',
              'styling': styles.WARNING_BODY},
             {'text': '⚠️', 'styling': styles.WARNING_SIGN}
        ]

    def __message_too_short(self):
        return [
            {'text': '⚠️', 'styling': styles.WARNING_SIGN},
            {'text': 'Your message is too short to be recorded. Please enter another message.',
             'styling': styles.WARNING_BODY},
            {'text': '⚠️', 'styling': styles.WARNING_SIGN}
        ]

    def __message_partially_recorded(self):
        return [
            {'text': '⚠️', 'styling': styles.WARNING_SIGN},
            {'text': 'Only the first 1000 characters of your message were recorded.',
             'styling': styles.WARNING_BODY},
            {'text': '⚠️', 'styling': styles.WARNING_SIGN}
        ]

    def __no_records_found(self):
        return [
            {'text': '⚠️', 'styling': styles.WARNING_SIGN},
            {'text': 'No missives found; temporal archive empty.',
             'styling': styles.WARNING_BODY},
            {'text': '⚠️', 'styling': styles.WARNING_SIGN}
        ]

    def __db_operation_failed(self):
        return [
            {'text': '⚠️', 'styling': styles.WARNING_SIGN},
            {'text': 'Database inaccessible, please try again.',
             'styling': styles.WARNING_BODY},
            {'text': '⚠️', 'styling': styles.WARNING_SIGN}
        ]

    def __hit_enter_to_continue(self):
        return [
            {'text': 'Hit ',            'styling': styles.DEFAULT},
            {'text': 'enter',           'styling': styles.HIGHLIGHT},
            {'text': ' to continue.',   'styling': styles.DEFAULT}
        ]

    def __display_another_missive_or_continue(self):
        return [
            {'text': '\n\nType ',                           'styling': styles.DEFAULT},
            {'text': 'r',                                   'styling': styles.HIGHLIGHT},
            {'text': ' then hit ',                          'styling': styles.DEFAULT},
            {'text': 'enter',                               'styling': styles.HIGHLIGHT},
            {'text': ' to read another missive, or hit ',   'styling': styles.DEFAULT},
            {'text': 'enter',                               'styling': styles.HIGHLIGHT},
            {'text': ' to return to menu.',                 'styling': styles.DEFAULT}
        ]

    def __time_machine_info(self):
        return [{'text': """
    This is a time machine that allows you to send messages to people in the future.
    
    It was discovered aboard the wreck of the Mary Celeste, in the captain's cabin.
    
    The machine was operational and running at the time of discovery.
    
    It is made of exotic materials, some of which were previously unknown to science.
    
    Messages can be recorded by many means, including using a pen or stylus.
    A keyboard has been deemed to be the most desirable interface for 21st century 
    users due to its familiarity.
    
    The machine does not record the electrical output from the keyboard. Instead, it
    records the intent of the user as expressed through the choices they make about
    which keys to press. When a robot presses the keys nothing happens.
    
    The mechanism by which this machine operates is unknown, as is the origin or 
    identity of the creators.
    
    We do not know who else may be reading your messages.
        """, 'styling': styles.INFO}]
