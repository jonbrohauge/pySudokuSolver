import unittest
import pytest
import solver


class SolverTest(unittest.TestCase):

    def setUp(self):
        self.testSolver = solver.Solver()
        #Horizontal test data
        self.testHorizontalRowComplete = [1,2,3,4,5,6,7,8,9]
        self.testHorizontalRowDuplicate = [1,2,3,5,5,6,7,8,9]
        self.testHorizontalRowIncomplete = ['O',2,3,4,'O',6,7,8,9]
        self.testHorizontalRowShort = [5,6,7,8,9]
        self.testHorizontalRowLong = [1,2,3,4,5,6,7,8,9,10]

        #Vertical test data
        self.testVerticalRowComplete = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
        self.testVerticalRowDuplicate = [[1],[2],[3],[5],[5],[6],[7],[8],[9]]
        self.testVerticalRowIncomplete = [['O'],[2],[3],[4],['O'],[6],[7],[8],[9]]
        self.testVerticalRowShort = [[5],[6],[7],[8],[9]]
        self.testVerticalRowLong = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

        #Square test data
        self.testSquareComplete = [[1,2,3],[4,5,6],[7,8,9]]
        self.testSquareHorizontalDuplicate = [[1,2,3],[5,5,6],[7,8,9]]
        self.testSquareVerticalDuplicate = [[1,2,4],[4,5,6],[7,8,9]]
        self.testSquareIncomplete = [['O',2,3],[4,'O',6],[7,8,9]]
        self.testSquareShort = [[5,6],[7,8,9]]
        self.testSquareLong = [[1,2,3],[4,5,6],[7,8,9,10]]

    def test_is_horizontal_complete(self):
        self.assertTrue(self.testSolver.is_horizontal_complete(self.testHorizontalRowComplete))
        self.assertTrue(self.testSolver.is_horizontal_complete(self.testHorizontalRowDuplicate))
        self.assertTrue(self.testSolver.is_horizontal_complete(self.testHorizontalRowIncomplete))
        self.assertFalse(self.testSolver.is_horizontal_complete(self.testHorizontalRowShort))
        self.assertFalse(self.testSolver.is_horizontal_complete(self.testHorizontalRowLong))

    def test_is_vertical_complete(self):
        self.assertTrue(self.testSolver.is_vertical_complete(self.testVerticalRowComplete))
        self.assertTrue(self.testSolver.is_vertical_complete(self.testVerticalRowDuplicate))
        self.assertTrue(self.testSolver.is_vertical_complete(self.testVerticalRowIncomplete))
        self.assertFalse(self.testSolver.is_vertical_complete(self.testVerticalRowShort))
        self.assertFalse(self.testSolver.is_vertical_complete(self.testVerticalRowLong))


    def test_is_square_complete(self):
        self.assertTrue(self.testSolver.is_square_complete(self.testSquareComplete))
        self.assertTrue(self.testSolver.is_square_complete(self.testSquareHorizontalDuplicate))
        self.assertTrue(self.testSolver.is_square_complete(self.testSquareVerticalDuplicate))
        self.assertTrue(self.testSolver.is_square_complete(self.testSquareIncomplete))
        self.assertFalse(self.testSolver.is_square_complete(self.testSquareShort))
        self.assertFalse(self.testSolver.is_square_complete(self.testSquareLong))

if __name__ == '__main__':
    unittest.main()
