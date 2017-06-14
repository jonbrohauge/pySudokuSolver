class Board(object):
    """This class defines the board"""

    def __init__(self, board_size):
        """The initializer for the class"""
        self.board_size = board_size
        self.board = []

        for index in range(0, self.board_size):
            self.board.append(['0'] * self.board_size)

    def is_on_board(self, x_coordinate, y_coordinate):
        """Is the piece on the board"""
        return bool((0 <= x_coordinate < self.board_size) and (0 <= y_coordinate < self.board_size))

    def place_piece(self, x_coordinate, y_coordinate, value):
        """Place a piece on the board"""
        try:
            if not self.is_on_board(x_coordinate, y_coordinate):
                raise Exception('not_on_board')
            if self.is_piece_set(x_coordinate, y_coordinate):
                raise Exception('piece_is_set')
            self.update_cell(x_coordinate, y_coordinate, value)
        except ValueError as err:
            print(err.args)

    def update_cell(self, x_coordinate, y_coordinate, value):
        """Update the placement of the piece on the board"""

        self.board[(y_coordinate-1)].insert((x_coordinate-1), str(value))
        self.board[(y_coordinate-1)].pop(x_coordinate)

    def print_board(self):
        """Print the board"""
        for row in self.board:
            print(" ".join(row))

    def is_piece_set(self, x_coordinate, y_coordinate):
        """Check to see if a piece is set """
        if self.is_on_board(x_coordinate, y_coordinate):
            return bool(str(self.board[(y_coordinate-1)][(x_coordinate-1)]) != '0')
