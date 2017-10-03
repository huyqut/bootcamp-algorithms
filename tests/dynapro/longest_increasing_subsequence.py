import unittest
import sys
from typing import List
from main.dynapro.longest_increasing_subsequence import longest_increasing_subsequence


class LongestIncreasingSubsequenceTest(unittest.TestCase):

    def assertLIS(self, numbers: List[int], lis: List[int]):
        self.assertEqual(lis, longest_increasing_subsequence(numbers))

    def testEmpty(self):
        self.assertLIS([], [])

    def testSingleton(self):
        self.assertLIS([1], [1])

    def testSimple(self):
        self.assertLIS([10, 22, 9, 33, 21, 50, 41, 60, 80], [10, 22, 33, 50, 60, 80])

    def testComplex(self):
        self.assertLIS([3, -1, 5, 8, 2, 3, 12, 7, 9, 10], [-1, 2, 3, 7, 9, 10])

    def testOnes(self):
        self.assertLIS([1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1])

    def testIncreasing(self):
        self.assertLIS([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

    def testDecreasing(self):
        self.assertLIS([5, 4, 3, 2, 1], [5])

    def testMaxInt(self):
        self.assertLIS([10, 22, 9, 33, 21, 50, 41, sys.maxsize, 60], [10, 22, 33, 50, sys.maxsize])

    def testMinInt(self):
        min_int = -sys.maxsize - 1
        self.assertLIS([min_int, 22, min_int, 33, 21, 50, 41, 60, 80], [min_int, 22, 33, 50, 60, 80])
