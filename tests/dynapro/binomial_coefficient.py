import unittest
import sys
from main.dynapro.bionomial_coefficient import *


class BinomialCoefficientTest(unittest.TestCase):

    def assertCoefficient(self, n: int, k: int, c: int):
        self.assertEqual(c, binomial_coefficient(n, k))

    def testZero(self):
        self.assertCoefficient(0, 0, 1)
        self.assertCoefficient(0, 1, 0)

    def testNegative(self):
        self.assertCoefficient(-1, 1, 0)
        self.assertCoefficient(1, -1, 0)

    def testOne(self):
        self.assertCoefficient(1, 0, 1)

    def testSimple(self):
        self.assertCoefficient(5, 2, 10)
        self.assertCoefficient(20, 3, 1140)
        self.assertCoefficient(30, 8, 5852925)
