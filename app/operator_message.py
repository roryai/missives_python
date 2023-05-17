import missives_python.app.styles as styles
from missives_python.app.printer import Printer


class OperatorMessage:

    def __init__(self, command, printer=Printer()):
        printer.process(self.selector(command))

    def selector(self, command):
        match command:
            case 'read_write_learn':
                return self.read_write_learn()

            case 'what_is_your_name':
                return [('What is your name?', styles.DEFAULT)]

            case 'what_is_your_message':
                return [('What message would you like to send to the future?',
                         styles.DEFAULT)]

            case 'confirm_submission':
                return self.confirm_submission()

            case 'input_not_recognised':
                return self.input_not_recognised()

            case 'name_only_letters':
                return self.name_only_letters()

            case 'message_too_short':
                return self.message_too_short()

            case 'missive_recorded':
                return [('Your missive has been added to the temporal archive, thank you.',
                         styles.SUCCESS)]

            case 'enter_to_continue':
                return self.hit_enter_to_continue()

            case 'display_another_missive_or_continue':
                return self.display_another_missive_or_continue()

            case 'time_machine_info':
                return self.time_machine_info()

    def read_write_learn(self):
        return [
            ('Would you like to write a missive, read a missive, or learn more about '
             'this time machine?',
                styles.DEFAULT),
            ('\nType ',                     styles.DEFAULT),
            ('w',                           styles.HIGHLIGHT),
            (' to write, ',                 styles.DEFAULT),
            ('r',                           styles.HIGHLIGHT),
            (' to read, or ',               styles.DEFAULT),
            ('l',                           styles.HIGHLIGHT),
            (' to learn more, then hit ',   styles.DEFAULT),
            ('enter',                       styles.HIGHLIGHT),
            ('.',                           styles.DEFAULT)
        ]

    def confirm_submission(self):
        return [
            ('Would you like to submit your message, or start again?', styles.DEFAULT),
            ('\nType ',                             styles.DEFAULT),
            ('y',                                   styles.HIGHLIGHT),
            (' then hit ',                          styles.DEFAULT),
            ('enter',                               styles.HIGHLIGHT),
            (' to submit your missive, or type ',   styles.DEFAULT),
            ('n',                                   styles.HIGHLIGHT),
            (' then hit ',                          styles.DEFAULT),
            ('enter',                               styles.HIGHLIGHT),
            (' to start again.',                    styles.DEFAULT)
        ]

    def input_not_recognised(self):
        return [
            ('⚠️', styles.WARNING_SIGN),
            (' Input not recognised, please try again.', styles.WARNING_BODY),
            ('⚠️', styles.WARNING_SIGN)
        ]
    
    def name_only_letters(self):
        return [
            ('⚠️', styles.WARNING_SIGN),
            (' Name must consist only of letters.', styles.WARNING_BODY),
            ('⚠️', styles.WARNING_SIGN)
        ]

    def message_too_short(self):
        return [
            ('⚠️', styles.WARNING_SIGN),
            (' Your message is too short to be recorded. Please enter another message.',
             styles.WARNING_BODY),
            ('⚠️', styles.WARNING_SIGN)
        ]

    def hit_enter_to_continue(self):
        return [
            ('Hit ',            styles.DEFAULT),
            ('enter',           styles.HIGHLIGHT),
            (' to continue.',   styles.DEFAULT)
        ]

    def display_another_missive_or_continue(self):
        return [
            ('\n\nType ',                           styles.DEFAULT),
            ('r',                                   styles.HIGHLIGHT),
            (' then hit ',                          styles.DEFAULT),
            ('enter',                               styles.HIGHLIGHT),
            (' to read another missive, or hit ',   styles.DEFAULT),
            ('enter',                               styles.HIGHLIGHT),
            (' to return to menu.',                 styles.DEFAULT)
        ]

    def time_machine_info(self):
        return [("""
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
        """, styles.INFO)]
