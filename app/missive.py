class Missive:

    def __init__(self, name, message):
        self.name = name
        self.message = message

    def display_missive(self):
        print()
        print(f"Name: {self.name}")
        print(f"Missive: {self.message}")
