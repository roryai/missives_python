from time import sleep


class OperatorMessage:

    def __init__(self, command):
        self.pad = "\n"
        print(self.pad)
        self.print_char_by_char(self.selector(command))
        print(self.pad)

    def print_char_by_char(self, string):
        for c in string:
            print(c, end='', flush=True)
            sleep(0.01)

    def selector(self, command):
        match command:
            case 'read_write_learn':
                return "Would you like to write a missive, read a missive, or learn more about this time machine?\n" \
                 "Type 'w' to write, 'r' to read, or 'l' to learn more, then hit enter."

            case 'what_is_your_name':
                return 'What is your name?'

            case 'what_is_your_message':
                return 'What message would you like to send to the future?'

            case 'input_not_recognised':
                return 'Input not recognised, please try again.'

            case 'name_only_letters':
                return 'Name must consist of only letters.'

            case 'message_too_short':
                return 'Your message is too short to be recorded. Please enter another message.'

            case 'missive_recorded':
                return 'Your missive has been added to the temporal archive, thank you.'

            case 'enter_to_continue':
                return 'Hit enter to continue.'

            case 'display_another_missive_or_continue':
                return "Enter 'r' to read another missive, or hit enter to continue"

            case 'time_machine_info':
                return self.time_machine_info()

    def time_machine_info(self):
        return """
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
        """
