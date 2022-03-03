"""
Simple Tic-Tac-Toe
==================
Play Tic-Tac-Toe by entering a row and column number for 0 to 2.
Human player will display a value of 1 for each piece.
AI player will display a value of 2 for each piece.
"""

from math import inf
import numpy as np
import time


def human_move(player):
    """
    Validate the input from the human player

    :param player: player ID
    :return: (row, column)
    """
    while True:
        row, col = get_user_input(player)
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Invalid value. Try again.')
        elif board[row][col] != 0:
            print("That position is already taken.")
        else:
            break
    return row, col


def get_user_input(player):
    """
    Accepts a space separated board position input by the player, and returns the integer values

    :param player: player ID
    :return: (row, column)
    """
    # Get user input
    position = input(f"Player {symbols[player]} position (row col): ").strip().split()
    # Check for two values
    if len(position) != 2:
        return -1, -1
    # Check for numbers only
    try:
        return int(position[0]), int(position[1])
    except ValueError:
        return -1, -1


def draw_board():
    # Draw the raw numpy array
    print(board)
    print()
    # Draw a representational array using X and O
    symbol_board = np.empty(shape=(3, 3), dtype=str)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                symbol_board[i][j] = "X"
            elif board[i][j] == 2:
                symbol_board[i][j] = "O"
            else:
                symbol_board[i][j] = " "
    print(symbol_board)


def check_win():
    """
    Check for a winning combination

    :return: Value of the winning pieces, zero if a tie, None if board is not full and no winner
    """

    # Rows
    for row in range(3):
        if board[row][0] != 0 and board[row][0] == board[row][1] and board[row][0] == board[row][2]:
            return board[row][0]

    # Columns
    for col in range(3):
        if board[0][col] != 0 and board[0][col] == board[1][col] and board[0][col] == board[2][col]:
            return board[0][col]

    # Diagonals
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]

    if board[0][2] != 0 and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]

    # Check if the board is full
    if np.all(board):
        return 0  # Tie
    else:
        return None  # Free spaces remaining


def ai_best_move():
    """
    Make test moves in turn and check the minimax tree node values to find the best move.

    :return: The best move found
    """
    # minimax algorithm
    # https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

    # AI tests moves one by one and uses minimax to look ahead and decide upon the best move
    best_score = -inf
    alpha = -inf
    beta = inf

    start_time = time.time_ns()
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # check that the spot is free
                board[i][j] = players['ai2']  # make a test move
                # AI is the Maximizing player
                # Human is the Minimizing player
                score = minimax(board, alpha, beta, maximizing=False)  # Human is the next player
                board[i][j] = 0  # undo the test move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    stop_time = time.time_ns()
    time_ns = stop_time - start_time
    # print(f'{time_ns = }')
    # minimax:
    #     First move time = 968717800 ns
    # minimax plus alpha-beta:
    #     First move time = 102204800 ns
    return best_move


def minimax(board, alpha, beta, maximizing):
    """
    MiniMax Algorithm.
    A recursive algorithm for choosing the next move. A value is associated with each position or state of the game.
    This value indicates how good it would be for a player to reach that position.
    The player then makes the move that maximizes the minimum value of the position
    resulting from the opponent's possible following moves.

    :param board: Current board state including the test move
    :param alpha: best score for each node
    :param beta: worst score for each node - used to discard losing branches
    :param maximizing: AI = True, Human = False
    :return: The best score found for the current test move
    """
    # Coding Challenge 154: Tic Tac Toe AI with Minimax Algorithm
    # https://www.youtube.com/watch?v=trKjYdBASyQ

    # https://www.youtube.com/watch?v=fT3YWCKvuQE
    # https://github.com/kying18/tic-tac-toe
    # count the number of zero values in the board
    # add 1 because this is used as a multiplier and should never be zero
    free_spaces = 1 + np.count_nonzero(board == 0)

    result = check_win()  # check_win() returns 0 = Tie, 1 = Player 1 win, 2 = Player 2 win, or None
    if result is not None:  # STUPID BOY!! I was using "if result:" - it took me two days to find this error!
        weighted_score = scores[result] * free_spaces
        return weighted_score

    if maximizing:  # ai is the maximizing player (looking for the highest score)
        best_score = -inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # is the spot free
                    board[i][j] = players['ai2']  # make a test move
                    score = minimax(board, alpha, beta, maximizing=False)  # AI is the next player
                    board[i][j] = 0  # undo the test move
                    best_score = max(score, best_score)

                    # Maximizing: check score against beta, update alpha
                    if best_score >= beta:
                        return best_score
                    if best_score > alpha:
                        alpha = best_score

        return best_score

    else:  # human is the minimizing player (looking for the lowest score)
        best_score = inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  # is the spot free
                    board[i][j] = players['human1']  # make a test move
                    score = minimax(board, alpha, beta, maximizing=True)  # Human is the next player
                    board[i][j] = 0  # undo the test move
                    best_score = min(score, best_score)

                    # Minimizing: check score against alpha, update beta
                    if best_score <= alpha:
                        return best_score
                    if best_score < beta:
                        beta = best_score

        return best_score


def main():
    # Game Loop
    game_on = True

    while game_on:
        for player in players:
            print()
            draw_board()
            current_player = players[player]
            if current_player == players['human1']:
                row, col = human_move(current_player)
            else:
                row, col = ai_best_move()
                print(f'AI move: {row} {col}')
            board[row][col] = current_player
            winner = check_win()
            if winner is not None:
                print(f'{winner = }')
                if winner == current_player:
                    print(f"Player {symbols[current_player]} wins!")
                    game_on = False
                    break
                if winner == 0:
                    print("It's a tie!")
                    game_on = False
                    break
    print('Thanks for playing.')


# CONSTANTS
players = {
    "human1": 1,
    "human2": 2,
    "ai1": 1,
    "ai2": 2,
}

symbols = {
    players['human1']: "X",
    players['human2']: "O",
    players['ai1']: "X",
    players['ai2']: "O",
}

# Used by minimax
scores = {
    0: 0,  # Tie
    players['human1']: -10,
    players['human2']: 10,
    players['ai1']: -10,
    players['ai2']: 10,
}


if __name__ == "__main__":
    # Define the matrix representing the game board
    board = np.zeros(shape=(3, 3), dtype=int)

    print("INSTRUCTIONS\n"
          "============\n"
          "Enter a grid position in the form \"row [space] column\"\n"
          "where row and column are integers in the range zero to three.\n"
          "e.g. 1 2 will position your piece on the middle row at the right.")

    main()
