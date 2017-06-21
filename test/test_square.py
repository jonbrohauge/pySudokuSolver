"""Test class executing unit tests on the class solver."""
import unittest
import solver


class SolverTest(unittest.TestCase):
    """unit test on the solver class."""

    def setUp(self):
        """Test class setup."""
        self.testSolver = solver.Solver()

        # Square test data
        self.testSquareComplete = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.testSquareHorizontalDuplicate = [[1, 2, 3], [5, 5, 6], [7, 8, 9]]
        self.testSquareVerticalDuplicate = [[1, 2, 4], [4, 5, 6], [7, 8, 9]]
        self.testSquareIncomplete = [['O', 2, 3], [4, 'O', 6], [7, 8, 9]]
        self.testSquareShort = [[5, 6], [7, 8, 9]]
        self.testSquareLong = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]

    def test_is_square_complete(self):
        """Testing for complete square input."""
        self.assertTrue(self.testSolver.is_square_complete(
            self.testSquareComplete))
        self.assertTrue(self.testSolver.is_square_complete(
            self.testSquareHorizontalDuplicate))
        self.assertTrue(self.testSolver.is_square_complete(
            self.testSquareVerticalDuplicate))
        self.assertTrue(self.testSolver.is_square_complete(
            self.testSquareIncomplete))
        self.assertFalse(self.testSolver.is_square_complete(
            self.testSquareShort))
        self.assertFalse(self.testSolver.is_square_complete(
            self.testSquareLong))


if __name__ == '__main__':
    unittest.main()
