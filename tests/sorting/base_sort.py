import unittest
from typing import List, Dict, Callable
from tests.sorting import sort_cases
from tests.sorting.sort_params import *


class BaseSort(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sort: Callable[[List[int]], List[int]] = None

    def baseAssert(self, test_case: Dict[str, List[int]]):
        actual = self.sort(test_case[INPUT])
        self.assertListEqual(test_case[EXPECTED], actual)

    def testEmpty(self):
        self.baseAssert(sort_cases.EMPTY)

    def testSingleton(self):
        self.baseAssert(sort_cases.SINGLETON)

    def testSimple(self):
        self.baseAssert(sort_cases.SIMPLE)

    def testBigMin(self):
        self.baseAssert(sort_cases.MIN)

    def testBigMax(self):
        self.baseAssert(sort_cases.MAX)

    def testMountain(self):
        self.baseAssert(sort_cases.MOUNTAIN)

    def testValley(self):
        self.baseAssert(sort_cases.VALLEY)

    def testAscend(self):
        self.baseAssert(sort_cases.ASCEND)

    def testDescend(self):
        self.baseAssert(sort_cases.DESCEND)

    def testRectangle(self):
        self.baseAssert(sort_cases.RECTANGLE)
