"""
number of players fixed to got from terminal input

input variables: grid size
the player who reaches the highest position as per the grid size wins
program terminates when the player reaches the highest position

game flow steps:
step 1:
rolling ice
step 2:
check dice side value
step 3:
move the player to the new position
step 4:
check if the player has reached the highest position
step 5:
check that everyone gets the same number of moves
"""
import random

# global variables
play_history = []
current_player_position = []
grid_size = int(input('enter the grid size: '))
highest_position = grid_size * grid_size
number_of_players = int(input('enter the number of players: '))


def roll_dice_():
    """
    function to roll the dice
    """
    dice_roll = random.randint(1, 6)
    return dice_roll


def play_turn(player_position, dice_roll):
    """
    function to play a turn
    """
    player_position += dice_roll
    return player_position


def create_players_():
    """
    function to create players
    """
    for player in range(number_of_players):
        play_history.append({'player': player + 1, 'position': [], 'dice_roll': [], 'win_status': False})
        current_player_position.append(0)


def play_game():
    """
    function to play the game
    """
    while True:
        player = None
        for player in range(number_of_players):
            dice_roll = roll_dice_()
            if play_turn(current_player_position[player], dice_roll) > highest_position:
                play_history[player]['position'].append(current_player_position[player])
                play_history[player]['dice_roll'].append(dice_roll)
                continue
            else:
                current_player_position[player] = play_turn(current_player_position[player], dice_roll)
                play_history[player]['position'].append(current_player_position[player])
                play_history[player]['dice_roll'].append(dice_roll)
                if current_player_position[player] == highest_position:
                    play_history[player]['win_status'] = True
                    print(f'player {player + 1} has won the game')
                    break
            player = player
        if current_player_position[player] == highest_position:
            break


def starting_game():
    """
    function to start the game
    """
    create_players_()
    play_game()


if __name__ == "__main__":
    starting_game()
    # print("players", players)
    print("play history", play_history)
    print("current position", current_player_position)
