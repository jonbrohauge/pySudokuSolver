"""Test class executing unit tests on the class board."""
import unittest
import board


class BoardTest(unittest.TestCase):
    """unit test on the board class."""

    def setUp(self):
        """Test class setup."""
        self.board_size = 9
        self.testBoard = board.Board(self.board_size)
        self.testBoard.place_piece(2, 3, 9)

    def test_create_board(self):
        """Testing for proper board creation."""
        self.assertEqual(self.board_size, self.testBoard.board_size)

    def test_is_on_board(self):
        """Tests to see if the cell requested for update is on the board."""
        self.assertTrue(self.testBoard.is_on_board(2, 3))
        self.assertTrue(self.testBoard.is_on_board(2, 2))
        self.assertFalse(self.testBoard.is_on_board(2, 99))
        self.assertFalse(self.testBoard.is_on_board(99, 3))
        self.assertFalse(self.testBoard.is_on_board(99, 99))

    def test_is_piece_set(self):
        """Tests to see if the cell requested for update has been updated."""
        self.assertTrue(self.testBoard.is_piece_set(2, 3))
        self.assertFalse(self.testBoard.is_piece_set(2, 2))
        self.assertFalse(self.testBoard.is_piece_set(3, 3))
        self.assertRaises(Exception, self.testBoard.place_piece, 2, 3)


if __name__ == '__main__':
    unittest.main()
