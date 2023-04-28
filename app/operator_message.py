class OperatorMessage:

    def __init__(self, method):
        self.pad()
        getattr(self, method)()
        self.pad()

    def pad(self):
        print()

    def read_write_learn(self):
        print('Would you like to write a missive, read a missive, or learn more about this'
              ' time machine?')
        print("Type 'w' to write, 'r' to read, or 'l' to learn more, then hit enter.")

    def what_is_your_name(self):
        print('What is your name?')

    def what_is_your_message(self):
        print('What message would you like to send to the future?')

    def input_not_recognised(self):
        print("Input not recognised, please try again.")

    def name_only_letters(self):
        print("Name must consist of only letters.")

    def message_too_short(self):
        print("Your message is too short to be recorded. Please enter another message.")

    def missive_recorded(self):
        print("Your missive has been added to the temporal archive, thank you.")

    def time_machine_info(self):
        print("""
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
        """)
