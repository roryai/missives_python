from missive import Missive
import random


class Controller:

    def __init__(self):
        self.missives = []

    def get_input(self):
        print("What is your name?")
        name = input()
        print("What message would you like to send to the future?")
        message = input()
        self.missives.append(Missive(name, message))

    def display_random_missive(self):
        missive = random.choice(self.missives)
        missive.display_missive()

cont = Controller()
cont.get_input()
cont.display_random_missive()
