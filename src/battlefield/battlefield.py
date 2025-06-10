from typing import Literal, Any
from src.shoots.shoot import Shooting
from src.vessels.vessel import Vessel

import random

class Battlefield:
    def __init__(self, size: int=10):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.vessels = []

    def print(self, hide_ships: bool=False) -> None:
        print('  ' + ' '.join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.grid):
            display_row = []
            for cell in row:
                if hide_ships and cell in ['P', 'E', 'C', 'S']:
                    display_row.append('.')
                else:
                    display_row.append(cell)
            print(chr(ord('A') + idx), '|', ' '.join(display_row))

    def place_vessel_randomly(self, vessel: Vessel) -> None:
        placed = False
        while not placed:
            vertical = random.choice([True, False])
            line = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            placed = vessel.place(self.grid, line, col, vertical)
        self.vessels.append(vessel)

    def receive_shot(self, line: int, col: int) -> (tuple[Literal[True], Any | None] | tuple[Literal[False], None]):
        cell = self.grid[line][col]
        if cell in ['P', 'E', 'C', 'S']:
            self.grid[line][col] = Shooting.RIGTH.value
            vessel = next((v for v in self.vessels if v.symbol == cell), None)
            if vessel:
                vessel.hit()
            return True, vessel
        elif cell == Shooting.WATER.value:
            self.grid[line][col] = Shooting.WRONG.value
            return False, None
        return False, None
    
    def is_valid_position(self, line, col):
        return 0 <= line < self.size and 0 <= col < self.size

    def all_vessels_destroyed(self) -> bool:
        return all(vessel.is_destroyed() for vessel in self.vessels)