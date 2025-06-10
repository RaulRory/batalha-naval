

# from src.shoots.shooting import Shooting
# from src.vessels.vessel import Vessels
# from src.battlefield.battlefield import Battlefield

import random
from typing import List
from src.shoots.shoot import Shoot
from src.battlefield.battlefield import Battlefield

class Player:
    def __init__(self, name: str, battlefield: List[str]):
        self.name = name
        self.battlefield = battlefield
        self.hits = 0

    def shoot(self, opponent_battlefield: Battlefield):
        raise NotImplementedError

class HumanPlayer(Player):
    def shoot(self, opponent_battlefield: Battlefield) -> Shoot | None:
        while True:
            try:
                line = int(input("Linha para atacar (0-9): "))
                col = int(input("Coluna para atacar (0-9): "))
                if opponent_battlefield.is_valid_position(line, col):
                    return Shoot(line, col)
            except ValueError:
                pass
            print("Posição inválida.")

class ComputerPlayer(Player):
    def shoot(self, opponent_battlefield: Battlefield) -> Shoot:
        line = random.randint(0, 9)
        col = random.randint(0, 9)
        print(f"Computador atira em ({line}, {col})")
        return Shoot(line, col)