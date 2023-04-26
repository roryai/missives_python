from datetime import datetime


class Missive:

    def __init__(self,
                 name,
                 message,
                 creation_time=None,
                 location=""
                 ):
        self.name = name
        self.message = message
        self.creation_time = self.creation_time(creation_time)
        self.location = self.location(location)

    def creation_time(self, time):
        if time:
            return time
        else:
            datetime.now()

    def location(self, location):
        if location:
            return location
        else:
            return "British Isles, England, London"

    def format_creation_time(self):
        return self.creation_time.strftime("%a, %d %b %Y %H:%M:%S")

    def format_location(self):
        return f"Milky Way, Sol, Earth, {self.location}"

    def display_missive(self):
        print()
        print(f"Time recorded: {self.format_creation_time()}")
        print(f"Recording location: {self.format_location()}")
        print(f"Scribe: {self.name}")
        print(f"Missive: {self.message}")
