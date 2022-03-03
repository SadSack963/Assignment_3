import global_vars
import numpy as np
from global_vars import DIMENSION


def evaluate_board(game_state: np.ndarray):
    """
    Check for a winning combination

    :param game_state: current state of the game
    :return: 0 = Tie,
             1 = Player 1 win,
             2 = Player 2 win,
             or None if the game_state is not full and there is no winner yet
    """
    # Rows
    for row in range(DIMENSION):
        if game_state[row][0] != 0:
            winner = game_state[row][0]
            for col in range(DIMENSION):
                if game_state[row][0] != game_state[row][col]:
                    winner = 0
                    break
            if winner != 0:
                return winner

    # Columns
    for col in range(DIMENSION):
        if game_state[0][col] != 0:
            winner = game_state[0][col]
            for row in range(DIMENSION):
                if game_state[0][col] != game_state[row][col]:
                    winner = 0
                    break
            if winner != 0:
                return winner

    # Diagonals
    if game_state[0][0] != 0:
        winner = game_state[0][0]
        for row_col in range(DIMENSION):
            if game_state[0][0] != game_state[row_col][row_col]:
                winner = 0
        if winner != 0:
            return winner

    if game_state[0][DIMENSION - 1] != 0:
        winner = game_state[0][DIMENSION - 1]
        for row_col in range(DIMENSION):
            if game_state[0][DIMENSION - 1] != game_state[row_col][- row_col - 1]:
                winner = 0
        if winner != 0:
            return winner

    # Check if the game_state is full
    if np.all(game_state):
        return 0  # Tie
    else:
        return None  # Free spaces remaining


def check_for_winner(player):
    """
    Check if there is a winner.

    :param player: Human or AI player
    :return: bool - True if there is a winner or a tie
    """

    winner = evaluate_board(global_vars.board)
    if winner:
        # print(f"Player {player.value} wins!")
        global_vars.player_msg.message_time(f"Player {player.value} wins!", time=2)
        return True
    if winner == 0:
        # print("It's a tie!")
        global_vars.player_msg.message_time("It's a tie!", time=2)
        return True
    return False
