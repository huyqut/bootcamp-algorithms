import unittest
from main.dynapro.coin_change import *


class CoinChangeTest(unittest.TestCase):

    def assertChange(self, expected: int, value: int, changes: List[int]):
        self.assertEqual(expected, coin_change(value, changes))

    def testEmpty(self):
        self.assertChange(0, 0, [1, 2, 3])
        self.assertChange(0, 5, [])
        self.assertChange(0, 3, [2])

    def testSingleton(self):
        self.assertChange(1, 3, [3])
        self.assertChange(1, 5, [1])

    def testSimple(self):
        self.assertChange(4, 4, [1, 2, 3])
        self.assertChange(5, 10, [2, 5, 3, 6])
