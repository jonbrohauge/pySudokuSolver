import unittest
import board


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board_size = 9
        self.testBoard = board.Board(self.board_size)
        #self.testBoard.place_piece(2, 3)

    def test_create_board(self):
        self.assertEqual(self.board_size, self.testBoard.board_size)

    def test_is_on_board(self):
        self.fail('unit test test_is_on_board is not done')

    def test_is_piece_set(self):
        self.fail('unit test test_is_piece_set is not done')
        #self.assertRaises(Exception, self.testBoard.place_piece, 2, 3)


if __name__ == '__main__':
    unittest.main()
