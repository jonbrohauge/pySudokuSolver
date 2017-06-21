"""Test class executing unit tests on the class solver."""
import unittest
import solver


class SolverTest(unittest.TestCase):
    """unit test on the solver class."""

    def setUp(self):
        """Test class setup."""
        self.testSolver = solver.Solver()

        # Vertical test data
        self.testVComplete = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        self.testVDuplicate = [[1], [2], [3], [5], [5], [6], [7], [8], [9]]
        self.testVIncomplete = [['O'], [2], [3], [4], ['O'], [6], [7], [8], [9]]
        self.testVShort = [[5], [6], [7], [8], [9]]
        self.testVLong = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

    def test_is_vertical_complete(self):
        """Testing for complete vertical input."""
        self.assertTrue(self.testSolver.is_vertical_complete(
            self.testVertRowComplete))
        self.assertTrue(self.testSolver.is_vertical_complete(
            self.testVertRowDuplicate))
        self.assertTrue(self.testSolver.is_vertical_complete(
            self.testVertRowIncomplete))
        self.assertFalse(self.testSolver.is_vertical_complete(
            self.testVertRowShort))
        self.assertFalse(self.testSolver.is_vertical_complete(
            self.testVertRowLong))


if __name__ == '__main__':
    unittest.main()
