from typing import List

class Vessel:
    def __init__(self, name: str, symbol: str, size: int):
        self.name = name
        self.symbol = symbol
        self.size = size
        self.hits = 0

    def place(self, grid: List[str], line: int, col: int, vertical: bool) -> bool:
        for i in range(self.size):
            x = line + i if vertical else line
            y = col if not vertical else col
            if x >= len(grid) or y >= len(grid) or grid[x][y] != '.':
                return False
        for i in range(self.size):
            x = line + i if vertical else line
            y = col if not vertical else col
            grid[x][y] = self.symbol
        return True

    def hit(self) -> None:
        self.hits += 1

    def is_destroyed(self) -> bool:
        return self.hits >= self.size

class Vessels:
    AIRCRAFT_CARRIE = Vessel("Porta-Aviões", "P", 5)
    BATTLESHIP = Vessel("Encouraçado", "E", 4)
    CRUISER = Vessel("Cruzador", "C", 3)
    SUBMARINE = Vessel("Submarino", "S", 2)