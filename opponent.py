import random

class Opponent:
    def move(self):
        return (random.randint(0, 25), random.randint(0, 25))
