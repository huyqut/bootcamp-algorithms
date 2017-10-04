import unittest
from main.dynapro.min_cost_path import *


class MinCostPathTest(unittest.TestCase):

    def assertPath(self, matrix: List[List[int]], expected: Tuple[int, List[Tuple[int, int]]]):
        self.assertTupleEqual(expected, min_cost_path(np.array(matrix)))

    def testEmpty(self):
        self.assertPath([], (0, []))
        self.assertPath([[], []], (0, []))

    def testSingleTon(self):
        self.assertPath([[1]], (1, [(0, 0)]))

    def testHorizontal(self):
        self.assertPath([[3, 5, 1, 7]], (16, [(0, 0), (0, 1), (0, 2), (0, 3)]))

    def testVertical(self):
        self.assertPath([[3], [5], [1], [7]], (16, [(0, 0), (1, 0), (2, 0), (3, 0)]))

    def testSimple(self):
        self.assertPath([[1, 2, 3], [4, 8, 2], [1, 5, 3]], (11, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]))

    def testComplex(self):
        self.assertPath([[31, 100, 65, 12, 18],
                         [10, 13, 47, 157, 6],
                         [100, 113, 174, 11, 13],
                         [88, 124, 41, 20, 140],
                         [99, 32, 111, 41, 20]],
                        (350, [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4)]))

