import unittest
from main.dynapro.matrix_chain_multi import *


class MatrixChainMultiTest(unittest.TestCase):

    def assertMatrix(self, expected: int, sizes: List[int]):
        self.assertEqual(expected, matrix_chain_multi(sizes))

    def testEmpty(self):
        self.assertMatrix(0, [])
        self.assertMatrix(0, [3])
        self.assertMatrix(0, [3, 2])

    def testSingleton(self):
        self.assertMatrix(6000, [10, 20, 30])

    def testSimple(self):
        self.assertMatrix(26000, [40, 20, 30, 10, 30])
        self.assertMatrix(30000, [10, 20, 30, 40, 30])
