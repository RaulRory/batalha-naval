from src.battlefield.battlefield import Battlefield
from src.players.players import HumanPlayer, ComputerPlayer
from src.vessels.vessel import Vessels

def start_game():
    player_battlefield = Battlefield()
    computer_battlefield = Battlefield()

    vessels = [Vessels.AIRCRAFT_CARRIE, Vessels.BATTLESHIP, Vessels.CRUISER, Vessels.SUBMARINE]
    for vessel in vessels:
        player_battlefield.place_vessel_randomly(vessel)
        computer_battlefield.place_vessel_randomly(vessel)

    player = HumanPlayer("Jogador", player_battlefield)
    computer = ComputerPlayer("Computador", computer_battlefield)

    turn = 0
    while True:
        print("\nSeu campo de batalha:")
        player_battlefield.print()
        print("\nCampo do computador:")
        computer_battlefield.print(hide_ships=True)

        if turn % 2 == 0:
            shoot = player.shoot(computer_battlefield)
            hit, vessel = computer_battlefield.receive_shot(shoot.line, shoot.col)
            if hit:
                print(f"Você acertou a embarcação: {vessel.name}!")
            else:
                print("Você acertou na água!")
        else:
            shoot = computer.shoot(player_battlefield)
            hit, vessel = player_battlefield.receive_shot(shoot.line, shoot.col)
            if hit:
                print(f"O computador acertou sua embarcação: {vessel.name}!")
            else:
                print("O computador acertou na água!")

        # Verifica vitória
        if computer_battlefield.all_vessels_destroyed():
            print("Parabéns, você venceu!")
            break
        if player_battlefield.all_vessels_destroyed():
            print("O computador venceu!")
            break

        turn += 1

if __name__ == "__main__":
    start_game()
