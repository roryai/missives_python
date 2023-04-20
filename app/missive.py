import datetime


class Missive:

    def __init__(self,
                 name,
                 message,
                 creation_time=datetime.datetime.now()
                 ):
        self.name = name
        self.message = message
        self.location = self.location()
        self.creation_time = creation_time

    def display_missive(self):
        print()
        print(f"Time recorded: {self.format_creation_time()}")
        print(f"Recording location: {self.format_location()}")
        print(f"Scribe: {self.name}")
        print(f"Missive: {self.message}")

    def format_creation_time(self):
        return self.creation_time.strftime("%a, %d %b %Y %H:%M:%S")

    def format_location(self):
        return f"Milky Way, Sol, Earth, {self.location}"

    def location(self):
        return "British Isles, England, London"
