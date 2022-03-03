from math import ceil
from turtle import onscreenclick
from global_vars import *


class HumanPlayer:
    def __init__(self, value: int):
        self.value = value
        self.row = -1
        self.col = -1

    def get_move(self, screen):
        """
        Get a valid grid selection.\n
        The selected move is stored in self.row, self,col
        Update the Turtle Graphics window while looking for mouse clicks

        :param screen: Turtle Graphics window
        :return: nothing
        """
        self.row = -1
        self.col = -1
        onscreenclick(self.get_mouse_click_coord)
        while self.row == -1 or self.col == -1:
            screen.window.update()

    def get_mouse_click_coord(self, x, y):
        """
        Derive the selected grid position from the mouse click coordinates.\n
        The selected move is stored in self.row, self,col

        :param x: mouse click x coordinate from turtle.onscreenclick()
        :param y: mouse click y coordinate from turtle.onscreenclick()
        :return: nothing
        """
        if -BORDER_LINE_COORD < x < BORDER_LINE_COORD and -BORDER_LINE_COORD < y < BORDER_LINE_COORD:
            # Convert mouse coordinates to row, col of the grid
            self.row, self.col = (ceil((GRID_OFFSET - y) / GRID_LINE_INCREMENT),
                                  ceil((GRID_OFFSET + x) / GRID_LINE_INCREMENT))
