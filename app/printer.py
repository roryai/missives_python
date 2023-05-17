from time import sleep
from rich import print


class Printer:

    def __init__(self, dev=False):
        self.dev = dev

    def process(self, messages):
        print()
        for message in messages:
            self.process_two(message['text'], message['styling'])
        print()

    def process_two(self, text, styling):
        rate = self.set_rate(styling['rate'])
        self.print_char_by_char(text, styling['colour'], styling['font_style'], rate)

    def set_rate(self, rate):
        if self.dev:
            return 0.0001
        else:
            return rate

    def print_char_by_char(self, message, colour, font_style, rate):
        for char in message:
            print(f'[{font_style} {colour}]{char}[/{font_style} {colour}]', end='', flush=True)
            sleep(rate)
