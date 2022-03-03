import unittest
import oxo_2d_4x4
import numpy as np
from evaluate_board_state import evaluate_board
import global_vars
from heuristics import heuristic_score


class TestWin(unittest.TestCase):

    def test_win_column(self):
        print('test_win_column')
        board = np.array([
            [2, 1, 2, 0],
            [2, 1, 0, 1],
            [0, 1, 2, 2],
            [1, 1, 1, 2],
        ])
        self.assertEqual(1, evaluate_board(board), "Should be 1")

    def test_win_row(self):
        print('test_win_row')
        board = np.array([
            [2, 1, 2, 0],
            [0, 1, 0, 1],
            [2, 2, 2, 2],
            [1, 1, 1, 2],
        ])
        self.assertEqual(2, evaluate_board(board), "Should be 2")

    def test_win_diagonal(self):
        print('test_win_diagonal')
        board = np.array([
            [2, 1, 2, 1],
            [2, 2, 1, 1],
            [0, 1, 2, 2],
            [1, 1, 1, 0],
        ])
        self.assertEqual(1, evaluate_board(board), "Should be 1")

    def test_win_none(self):
        print('test_win_none')
        board = np.array([
            [2, 1, 2, 0],
            [2, 1, 0, 1],
            [0, 0, 2, 2],
            [1, 1, 1, 2],
        ])
        self.assertIsNone(evaluate_board(board), "Should be None")

    def test_tie(self):
        print('test_tie')
        board = np.array([
            [2, 1, 2, 1],
            [2, 1, 2, 1],
            [1, 2, 2, 2],
            [1, 1, 1, 2],
        ])
        self.assertEqual(0, evaluate_board(board), "Should be 0")

    def test_tie_2(self):
        print('test_tie')
        board = np.array([
            [2, 1, 2, 2],
            [2, 2, 1, 1],
            [1, 1, 1, 2],
            [1, 1, 1, 2],
        ])
        self.assertEqual(0, evaluate_board(board), "Should be 0")


class TestMinimax(unittest.TestCase):

    def test_last_move(self):
        print('test_last_move')
        global_vars.board = np.array([
            [2, 1, 2, 2],
            [2, 2, 1, 1],
            [1, 1, 1, 2],
            [2, 2, 0, 2],
        ])
        ai_player = oxo_2d_4x4.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((3, 2), (ai_player.row, ai_player.col), "Should be (3, 2)")

    def test_block_win_move(self):
        print('test_block_win_move')
        global_vars.board = np.array([
            [2, 1, 2, 1],
            [2, 2, 1, 1],
            [1, 1, 1, 2],
            [0, 2, 0, 2],
        ])
        ai_player = oxo_2d_4x4.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((3, 0), (ai_player.row, ai_player.col), "Should be (3, 0)")

    def test_block_move(self):
        print('test_block_move')
        global_vars.board = np.array([
            [2, 1, 1, 1],
            [2, 2, 0, 1],
            [1, 2, 1, 2],
            [0, 2, 1, 2],
        ])
        ai_player = oxo_2d_4x4.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((1, 2), (ai_player.row, ai_player.col), "Should be (1, 2)")

    def test_block_move_2(self):
        print('test_block_move_2')
        global_vars.board = np.array([
            [2, 0, 1, 1],
            [2, 2, 0, 1],
            [1, 1, 2, 0],
            [0, 2, 1, 1],
        ])
        ai_player = oxo_2d_4x4.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((2, 3), (ai_player.row, ai_player.col), "Should be (2, 3)")

    def test_win_move(self):
        print('test_win_move')
        global_vars.board = np.array([
            [1, 0, 1, 1],
            [2, 2, 0, 2],
            [1, 1, 2, 0],
            [0, 2, 1, 1],
        ])
        ai_player = oxo_2d_4x4.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((1, 2), (ai_player.row, ai_player.col), "Should be (1, 2)")


class TestHeuristics(unittest.TestCase):
    def test_heuristics_row_1(self):
        print('test_heuristics_row_1')
        global_vars.board = np.array([
            [0, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])
        self.assertEqual(2, heuristic_score((0, 1), global_vars.board), "Should be 2")

    def test_heuristics_row_2(self):
        print('test_heuristics_row_2')
        global_vars.board = np.array([
            [0, 2, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
        ])
        self.assertEqual(11, heuristic_score((0, 1), global_vars.board), "Should be 11")

    def test_heuristics_row_3(self):
        print('test_heuristics_row_3')
        global_vars.board = np.array([
            [0, 2, 0, 0],
            [0, 2, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 1, 1],
        ])
        self.assertEqual(101, heuristic_score((0, 1), global_vars.board), "Should be 101")

    def test_heuristics_row_4(self):
        print('test_heuristics_row_4')
        global_vars.board = np.array([
            [0, 2, 0, 0],
            [0, 2, 0, 0],
            [0, 2, 0, 0],
            [0, 1, 0, 0],
        ])
        self.assertEqual(1, heuristic_score((0, 1), global_vars.board), "Should be 1")

    def test_heuristics_col_1(self):
        print('test_heuristics_col_1')
        global_vars.board = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2],
            [0, 0, 0, 0],
        ])
        self.assertEqual(2, heuristic_score((2, 3), global_vars.board), "Should be 2")

    def test_heuristics_col_2(self):
        print('test_heuristics_col_2')
        global_vars.board = np.array([
            [0, 0, 0, 2],
            [0, 0, 0, 0],
            [2, 0, 0, 2],
            [0, 0, 0, 0],
        ])
        self.assertEqual(20, heuristic_score((2, 3), global_vars.board), "Should be 20")

    def test_heuristics_col_3(self):
        print('test_heuristics_col_3')
        global_vars.board = np.array([
            [0, 0, 0, 2],
            [0, 0, 0, 0],
            [2, 2, 0, 2],
            [0, 0, 0, 0],
        ])
        self.assertEqual(110, heuristic_score((2, 3), global_vars.board), "Should be 110")

    def test_heuristics_col_4(self):
        print('test_heuristics_col_4')
        global_vars.board = np.array([
            [0, 0, 0, 2],
            [0, 0, 0, 0],
            [2, 2, 1, 2],
            [0, 0, 0, 0],
        ])
        self.assertEqual(10, heuristic_score((2, 3), global_vars.board), "Should be 10")

    def test_heuristics_col_5(self):
        print('test_heuristics_col_5')
        global_vars.board = np.array([
            [0, 0, 0, 2],
            [0, 0, 0, 1],
            [2, 2, 0, 2],
            [0, 0, 0, 0],
        ])
        self.assertEqual(100, heuristic_score((2, 3), global_vars.board), "Should be 100")

    def test_heuristics_diag_1(self):
        print('test_heuristics_diag_1')
        global_vars.board = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 0],
        ])
        self.assertEqual(3, heuristic_score((2, 2), global_vars.board), "Should be 3")

    def test_heuristics_diag_2(self):
        print('test_heuristics_diag_2')
        global_vars.board = np.array([
            [0, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 0],
        ])
        self.assertEqual(12, heuristic_score((2, 2), global_vars.board), "Should be 12")

    def test_heuristics_diag_3(self):
        print('test_heuristics_diag_3')
        global_vars.board = np.array([
            [0, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 2],
        ])
        self.assertEqual(102, heuristic_score((2, 2), global_vars.board), "Should be 102")

    def test_heuristics_diag_4(self):
        print('test_heuristics_diag_4')
        global_vars.board = np.array([
            [0, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 1, 2, 0],
            [0, 0, 0, 1],
        ])
        self.assertEqual(1, heuristic_score((2, 2), global_vars.board), "Should be 1")

    def test_heuristics_diag_5(self):
        print('test_heuristics_diag_5')
        global_vars.board = np.array([
            [0, 0, 1, 0],
            [0, 2, 0, 0],
            [0, 1, 2, 0],
            [0, 0, 0, 2],
        ])
        self.assertEqual(100, heuristic_score((2, 2), global_vars.board), "Should be 100")


if __name__ == "__main__":
    unittest.main()
