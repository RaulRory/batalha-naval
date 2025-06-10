from enum import Enum

class Shooting(Enum):
    WATER = "."
    WRONG = "*"
    RIGTH = "X"

class Shoot:
    def __init__(self, line, col):
        self.line = line
        self.col = col