"""Test class executing unit tests on the class solver."""
import unittest
import solver


class SolverTest(unittest.TestCase):
    """unit test on the solver class."""

    def setUp(self):
        """Test class setup."""
        self.testSolver = solver.Solver()
        # Horizontal test data

        self.testHorizontalRowComplete = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.testHorizontalRowDuplicate = [1, 2, 3, 5, 5, 6, 7, 8, 9]
        self.testHorizontalRowIncomplete = ['O', 2, 3, 4, 'O', 6, 7, 8, 9]
        self.testHorizontalRowShort = [5, 6, 7, 8, 9]
        self.testHorizontalRowLong = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_is_horizontal_complete(self):
        """Testing for complete horizontal input."""
        self.assertTrue(self.testSolver.is_horizontal_complete(
            self.testHorizontalRowComplete))
        self.assertTrue(self.testSolver.is_horizontal_complete(
            self.testHorizontalRowDuplicate))
        self.assertTrue(self.testSolver.is_horizontal_complete(
            self.testHorizontalRowIncomplete))
        self.assertFalse(self.testSolver.is_horizontal_complete(
            self.testHorizontalRowShort))
        self.assertFalse(self.testSolver.is_horizontal_complete(
            self.testHorizontalRowLong))


if __name__ == '__main__':
    unittest.main()
