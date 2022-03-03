import global_vars
from math import inf
import numpy as np
from evaluate_board_state import evaluate_board
from global_vars import *
from heuristics import heuristic_score

class AIPlayer:
    def __init__(self, value: int):
        """
        AI class definition.

        :param value: Assigned to AI player - 1 = Player 1, 2 = Player 2
        :type value: int
        """
        self.value = value
        self.opposition_value = 2 if self.value == 1 else 1
        self.score = 1
        self.opposition_score = -1
        self.row = -1
        self.col = -1
        self.game_state = 0  # This line is simply to prevent warning "Instance attribute game_state defined outside __init__"

    def get_move(self, screen=None):
        """
        Finds the best possible move for the AI player using the minimax algorithm with alpha-beta pruning. \n

        https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/\n
        The selected move is stored in self.row, self,col

        :param screen: Turtle Graphics window (not used by the AI player)
        :return: nothing
        """
        self.game_state = global_vars.board

        # https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

        # AI tests moves one by one and uses minimax to look ahead and decide upon the best move
        best_move = (0, 0)  # This is only here to define the variables (to remove linter warnings below)
        best_score = -inf  # Maximizing player
        alpha = -inf
        beta = inf

        # ####################################################################
        #    With 3x3 grid there are 9! possible results (362,880)
        #    With 4x4 grid there are 16! possible results (20,922,789,888,000)
        #    We have to limit the depth of look ahead.
        # ####################################################################

        for i in range(DIMENSION):
            for j in range(DIMENSION):
                # print("test move", i, j)
                if self.game_state[i][j] == 0:  # check that the spot is free
                    self.game_state[i][j] = self.value  # make a test move
                    score = self.minimax(self.game_state, alpha, beta, maximizing=False, depth=MAX_LOOKAHEAD)  # next player is Minimizing player
                    # Minimax depth limit reached. Get the heuristic score
                    if score == 0:
                        score = heuristic_score(test_move=(i, j), game_state=self.game_state)
                    self.game_state[i][j] = 0  # undo the test move
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        # print(f'AI move: {best_move[0]} {best_move[1]}')
        self.row = best_move[0]
        self.col = best_move[1]

    def minimax(self, test_state: np.ndarray, alpha: float, beta: float, maximizing: bool, depth: int):
        """
        Test moves at every remaining position on the game_state to find the best possible move. \n
        Maximizing player (current AI player) looks for the highest score. \n
        Minimizing player (opposition) looks for the lowest score. \n

        https://www.youtube.com/watch?v=fT3YWCKvuQE \n
        https://github.com/kying18/tic-tac-toe

        :param test_state: state of the game_state during the test move
        :param alpha: best (highest) score so far for maximizing player
        :param beta: best (lowest) score so far for minimizing player
        :param maximizing: this player is maximizing if True (or minimizing if False)
        :param depth: How far to look ahead
        :return: best score for the current test move
        """

        # Limit of look ahead
        # #################################################################
        # Calculate a heuristic score.
        # + 100 for EACH 3-in-a-line (with 1 empty cell)
        # +  10 for EACH two-in-a-line (with 2 empty cells)
        # +   1 for EACH one-in-a-line (with 3 empty cells)
        # Negate scores for opponent positions
        #
        # Store the location in a list (positions with the same scores).
        # When all tests are done, choose a random location from the list.
        # #################################################################
        if depth == 0:
            return 0

        # count the number of zero values in the game_state
        # add 1 because this is used as a multiplier and should never be zero
        free_spaces = 1 + np.count_nonzero(test_state == 0)

        # if the test state results in a win or draw, then return the score
        result = evaluate_board(test_state)  # check_win() returns 0 = Tie, 1 = Player 1 win, 2 = Player 2 win, or None
        if result == self.value:
            return self.score * free_spaces
        elif result == self.opposition_value:
            return self.opposition_score * free_spaces
        elif result == 0:
            return 0

        if maximizing:  # Maximizing: looking for the highest score
            best_score = -inf
            for i in range(DIMENSION):
                for j in range(DIMENSION):
                    # print("Maximizing", i, j)
                    if test_state[i][j] == 0:  # is the spot free
                        test_state[i][j] = self.value  # make a test move
                        score = self.minimax(test_state, alpha, beta, maximizing=False, depth=depth - 1)  # next player is Minimizing player
                        test_state[i][j] = 0  # undo the test move
                        best_score = max(score, best_score)

                        # Maximizing: check score against beta, update alpha
                        if best_score >= beta:
                            return best_score
                        if best_score > alpha:
                            alpha = best_score

            return best_score

        else:  # Minimizing: looking for the lowest score
            best_score = inf
            for i in range(DIMENSION):
                for j in range(DIMENSION):
                    # print("Minimizing", i, j)
                    if test_state[i][j] == 0:  # is the spot free
                        test_state[i][j] = self.opposition_value  # make a test move
                        score = self.minimax(test_state, alpha, beta, maximizing=True, depth=depth - 1)  # next player is Maximizing player
                        test_state[i][j] = 0  # undo the test move
                        best_score = min(score, best_score)

                        # Minimizing: check score against alpha, update beta
                        if best_score <= alpha:
                            return best_score
                        if best_score < beta:
                            beta = best_score

            return best_score
