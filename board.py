class Board(object):
    """This class defines the board"""

    def __init__(self, board_size):
        """The initializer for the class"""
        self.board_size = board_size
        self.board = []

        for index in range(0, self.board_size):
            value = str(index)
            self.board.append(['O'] * self.board_size)

    def is_on_board(self, x_coordinate, y_coordinate):
        """Is the piece on the board"""
        return bool((0 <= x_coordinate < self.board_size) and (0 <= y_coordinate < self.board_size))

    def updateCell(self, x_coordinate, y_coordinate, value):
        pass

    def print(self):
        """Print the board"""
        for row in self.board:
            print(" ".join(row))
