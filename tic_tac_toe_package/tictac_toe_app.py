from tic_tac_toe_package.player import Player
from tic_tac_toe_package.exceptions.invalid_input_error import InvalidInputError
from tic_tac_toe_package.exceptions.cell_has_been_taken_error import CeilHasBeenTakenError
from tic_tac_toe_package.cell_value import CeilValue


def displayGame(player1, player2):
    game_player = Player()
    game_ended = False

    while not game_ended:
        print(f"Your turn player {player1 if game_player.get_player() else player2}")

        try:
            move = input()
            game_player.play(move)
            game_player.print_board()
            print("\n")

            if game_player.check_winner(game_player.get_player()):
                print(f"Player {player1 if game_player.get_player() else player2} wins!")
                break
            elif game_player.is_board_full():
                print("It's a draw!")
                break

        except Exception as exception:
            print(exception)
            game_player.switch_player()


first_player = input("Enter your name")
print(f"Welcome {first_player} you are the first player and you are X in the game")

second_player = input("Enter your name")
print(f"Welcome {second_player} you are the second player and you are O in the game")

displayGame(first_player, second_player)
