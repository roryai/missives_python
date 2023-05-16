from time import sleep
from rich import print


class Printer:

    def __init__(self, dev=False):
        self.dev = dev

    def process(self, specification):
        print()
        for properties in specification:
            message = properties[0]
            style = properties[1]
            colour = style[0]
            formatting = style[1]
            if self.dev:
                rate = 0.0001
            else:
                rate = style[2]
            self.print_char_by_char(message, colour, formatting, rate)
        print()

    def print_char_by_char(self, message, colour, formatting, rate):
        for char in message:
            print(f"[{formatting[0]} {colour}]{char}[/{formatting[0]} {colour}]", end='', flush=True)
            sleep(rate)

