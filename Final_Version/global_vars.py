"""
This file is used to store global variables which can be imported into whichever file needs them.
"""

from messenger import Messenger
import numpy as np


# Playing Grid Dimension
DIMENSION = 4  # i.e. 4 = 4 x 4 grid

# Maximum moves to check in minimax
MAX_LOOKAHEAD = 5

# Set up the display
DARK = (60, 60, 60)  # Background colour
WINDOW_SIZE = 600  # i.e. height, width

GRID_SIZE = round(WINDOW_SIZE * 6 / 7)  # Leaves an empty border around the outside of the grid
BORDER_LINE_COORD = round(GRID_SIZE / 2)  # Coordinate of the border line
GRID_LINE_INCREMENT = round(GRID_SIZE / DIMENSION)  # Distance between grid lines

PADDING = GRID_LINE_INCREMENT * 0.15  # space between grid line and X or O
X_START = BORDER_LINE_COORD - PADDING  # X top left starting position
X_SIZE = GRID_LINE_INCREMENT - PADDING * 2  # X height and width
O_CENTER_X = BORDER_LINE_COORD - GRID_LINE_INCREMENT / 2  # O center
O_START_Y = BORDER_LINE_COORD - GRID_LINE_INCREMENT + PADDING  # O starting position
O_RADIUS = X_SIZE / 2  # O radius

GRID_OFFSET = BORDER_LINE_COORD - GRID_LINE_INCREMENT  # Distance from center of the window to the first grid line

# Define the matrix representing the game_state
board = np.zeros(shape=(DIMENSION, DIMENSION), dtype=int)

# Define the Turtle used to write messages to the screen
player_msg = Messenger(
    font_size=24,
    font_type="bold italic",
)
