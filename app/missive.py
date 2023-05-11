from datetime import datetime
from printer import Printer
import colours


class Missive:

    def __init__(self,
                 name,
                 message,
                 creation_time=None,
                 location="British Isles, England, London",
                 gathering="Burning Nest '23",
                 printer=Printer()
                 ):
        self.name = name
        self.message = message
        self.creation_time = creation_time or datetime.now()
        self.location = location
        self.gathering = gathering
        self.printer = printer

    @classmethod
    def init_from_record(cls, record):
        return Missive(name=record[1],
                       message=record[2],
                       creation_time=datetime.strptime(record[3], '%Y-%m-%d %H:%M:%S.%f'),
                       location=record[4])

    def format_creation_time(self):
        return self.creation_time.strftime("%a, %d %b %Y %H:%M")

    def format_location(self):
        return f"Milky Way, Sol, Earth, {self.location}"

    def display_missive(self):
        return self.printer.process([
            ("\nTime recorded:      ",      colours.WHITE),
            (self.format_creation_time(),   colours.YELLOW),
            ("\nRecording location: ",      colours.WHITE),
            (self.format_location(),        colours.YELLOW),
            ("\nGathering:          ",      colours.WHITE),
            (self.gathering,                colours.YELLOW),
            ("\n\nScribe:  ",               colours.WHITE),
            (self.name,                     colours.MAGENTA),
            ("\nMissive: ",                 colours.WHITE),
            (self.message,                  colours.CYAN)
        ])
