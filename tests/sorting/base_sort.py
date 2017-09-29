import unittest
from typing import List
from tests.sorting import sort_cases


class BaseSort(unittest.TestCase):

    def sort(self, numbers: List[int]) -> List[int]:
        pass

    def testSimple(self):
        actual = self.sort(sort_cases.SIMPLE['input'])
        self.assertListEqual(sort_cases.SIMPLE['expected'], actual)
