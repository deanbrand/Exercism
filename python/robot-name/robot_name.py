import string
import random


class Robot:
    def __init__(self):
        self.name = ''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))

    def reset(self):
        random.seed()
        self.name = ''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=3))
