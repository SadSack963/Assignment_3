import global_vars
import numpy as np
from global_vars import DIMENSION


def heuristic_score(test_move: tuple, game_state: np.ndarray):
    """
    Calculate a heuristic score.
    + 100 for EACH 3-in-a-line (with 1 empty cell)
    +  10 for EACH two-in-a-line (with 2 empty cells)
    +   1 for EACH one-in-a-line (with 3 empty cells)

    :param test_move: current position under test
    :type test_move: tuple
    :param game_state: state of the game_state during the test move
    :type game_state: numpy array
    :return: heuristic score for the current position under test
    :rtype: int
    """
    def score_row():
        # Test row
        total = 0
        for y in range(DIMENSION):
            if game_state[i][y] == player:
                total += 1
            elif game_state[i][y] != 0:
                total = 0
                break
        if total == DIMENSION - 1:
            return 100
        elif total == DIMENSION - 2:
            return 10
        elif total > 0:
            return 1
        else:
            return 0

    def score_col():
        # Test column
        total = 0
        for x in range(DIMENSION):
            if game_state[x][j] == player:
                total += 1
            elif game_state[x][j] != 0:
                total = 0
                break
        if total == DIMENSION - 1:
            return 100
        elif total == DIMENSION - 2:
            return 10
        elif total > 0:
            return 1
        else:
            return 0

    def score_diag():
        # Test diagonals
        total = 0
        if i == j:
            for x in range(DIMENSION):
                if game_state[x][x] == player:
                    total += 1
                elif game_state[x][x] != 0:
                    total = 0
                    break
        elif i == DIMENSION - j - 1:
            for x in range(DIMENSION):
                y = DIMENSION - x - 1
                if game_state[x][y] == player:
                    total += 1
                elif game_state[x][y] != 0:
                    total = 0
                    break
        if total == DIMENSION - 1:
            return 100
        elif total == DIMENSION - 2:
            return 10
        elif total > 0:
            return 1
        else:
            return 0

    i = test_move[0]
    j = test_move[1]
    player = game_state[i][j]
    # Return heuristic score
    return score_row() + score_col() + score_diag()
