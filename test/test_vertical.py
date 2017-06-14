import unittest
import solver


class SolverTest(unittest.TestCase):

    def setUp(self):
        self.testSolver = solver.Solver()

        #Vertical test data
        self.testVerticalRowComplete = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
        self.testVerticalRowDuplicate = [[1],[2],[3],[5],[5],[6],[7],[8],[9]]
        self.testVerticalRowIncomplete = [['O'],[2],[3],[4],['O'],[6],[7],[8],[9]]
        self.testVerticalRowShort = [[5],[6],[7],[8],[9]]
        self.testVerticalRowLong = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

    def test_is_vertical_complete(self):
        self.assertTrue(self.testSolver.is_vertical_complete(self.testVerticalRowComplete))
        self.assertTrue(self.testSolver.is_vertical_complete(self.testVerticalRowDuplicate))
        self.assertTrue(self.testSolver.is_vertical_complete(self.testVerticalRowIncomplete))
        self.assertFalse(self.testSolver.is_vertical_complete(self.testVerticalRowShort))
        self.assertFalse(self.testSolver.is_vertical_complete(self.testVerticalRowLong))

if __name__ == '__main__':
    unittest.main()
