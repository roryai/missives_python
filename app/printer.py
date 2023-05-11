from time import sleep
from rich import print

DEFAULT_RATE = 0.015


class Printer:

    def process(self, specification):
        print()
        for properties in specification:
            rate = DEFAULT_RATE
            message = properties[0]
            colour = properties[1]
            if len(properties) > 2:
                rate = properties[2]
            self.print_char_by_char(message, colour, rate)
        print()

    def print_char_by_char(self, message, colour, rate):
        for char in message:
            print(f"[bold {colour}]{char}[/bold {colour}]", end='', flush=True)
            sleep(rate)

