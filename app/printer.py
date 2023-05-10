from time import sleep
from rich import print


class Printer:

    def print_char_by_char(self, specification):
        for x in specification:
            message = x[0]
            colour = x[1]
            for char in message:
                print(f"[bold {colour}]{char}[/bold {colour}]", end='', flush=True)
                sleep(0.003)
