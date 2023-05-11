import colours
from printer import Printer


class OperatorMessage:

    def __init__(self, command, printer=Printer()):
        printer.process(self.selector(command))

    def selector(self, command):
        match command:
            case 'read_write_learn':
                return self.read_write_learn()

            case 'what_is_your_name':
                return [('What is your name?', colours.DEFAULT_COLOUR)]

            case 'what_is_your_message':
                return [('What message would you like to send to the future?', colours.DEFAULT_COLOUR)]

            case 'input_not_recognised':
                return [('⚠️ Input not recognised, please try again. ⚠️', colours.YELLOW)]

            case 'name_only_letters':
                return [('⚠️ Name must consist of only letters. ⚠️', colours.YELLOW)]

            case 'message_too_short':
                return [('⚠️ Your message is too short to be recorded. Please enter another message. ⚠️', colours.YELLOW)]

            case 'missive_recorded':
                return [('Your missive has been added to the temporal archive, thank you.', colours.MAGENTA)]

            case 'enter_to_continue':
                return self.hit_enter_to_continue()

            case 'display_another_missive_or_continue':
                return self.display_another_missive_or_continue()

            case 'time_machine_info':
                return self.time_machine_info()

    def read_write_learn(self):
        return [
            ("Would you like to write a missive, read a missive, or learn more about this time machine?",
                colours.GREEN, 0.004),
            ("\nType",                          colours.DEFAULT_COLOUR),
            (" w",                              colours.HIGHLIGHT_COLOUR),
            (" to write,",                      colours.DEFAULT_COLOUR),
            (" r",                              colours.HIGHLIGHT_COLOUR),
            (" to read, or",                    colours.DEFAULT_COLOUR),
            (" l",                              colours.HIGHLIGHT_COLOUR),
            (" to learn more, then hit",        colours.DEFAULT_COLOUR),
            (" enter",                          colours.HIGHLIGHT_COLOUR),
            (".",                               colours.DEFAULT_COLOUR)
        ]

    def hit_enter_to_continue(self):
        return [
            ('Hit',             colours.DEFAULT_COLOUR),
            (' enter',          colours.HIGHLIGHT_COLOUR),
            (' to continue.',   colours.DEFAULT_COLOUR)
        ]

    def display_another_missive_or_continue(self):
        return [
            ("Enter",                                   colours.DEFAULT_COLOUR),
            (" r",                                      colours.HIGHLIGHT_COLOUR),
            (" to read another missive, or hit",        colours.DEFAULT_COLOUR),
            (" enter",                                  colours.HIGHLIGHT_COLOUR),
            (" to continue.",                           colours.DEFAULT_COLOUR)
        ]

    def time_machine_info(self):
        return [("""
    This is a time machine that allows you to send messages to people in the future.
    
    It was discovered aboard the wreck of the Mary Celeste, in a centuries-old air pocket.
    The machine was operational and running.
    
    It is made of exotic materials, some of which were unknown to science until the discovery.
    
    Messages can be recorded by many means, including using a pen or stylus.
    A keyboard has been deemed to be the most desirable interface for 21st century 
    users due to its familiarity.
    
    The machine does not record the electrical output from the keyboard. Instead, it
    records the intent of the user as expressed through the choices they make about
    which keys to press. When a robot presses the keys nothing happens.
    
    The mechanism by which this machine operates is unknown, as is the origin or identity
    of the creators.
    
    We do not know who else may be reading your messages.
        """, colours.PURPLE, 0.004)]
