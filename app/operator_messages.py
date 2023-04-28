class OperatorMessages:

    def pad(self):
        print()

    def read_write_learn(self):
        self.pad()
        print('Would you like to write a missive, read a missive, or learn more about this'
              ' time machine?')
        print("Type 'w' to write, 'r' to read, or 'l' to learn more, then hit enter.")
        self.pad()

    def what_is_your_name(self):
        self.pad()
        print('What is your name?')
        self.pad()

    def what_is_your_message(self):
        self.pad()
        print('What message would you like to send to the future?')
        self.pad()

    def input_not_recognised(self):
        self.pad()
        print("Input not recognised, please try again.")
        self.pad()

    def name_only_letters(self):
        self.pad()
        print("Name must consist of only letters.")
        self.pad()

    def message_too_short(self):
        self.pad()
        print("Your message is too short to be recorded. Please enter another message.")
        self.pad()

    def missive_recorded(self):
        self.pad()
        print("Your missive has been added to the temporal archive, thank you.")
        self.pad()

    def time_machine_info(self):
        self.pad()
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
        self.pad()
