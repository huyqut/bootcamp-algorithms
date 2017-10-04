import unittest
from main.dynapro.knap_sack_0_1 import *


class KnapSackTest(unittest.TestCase):

    def formalize_result(self, value: int, takes: List[int], values: List[int]) -> Tuple[int, List[int]]:
        take_list = []
        for i in range(len(takes)):
            if takes[i]:
                take_list.append(i)
                value += values[i]
        return value, take_list

    def assertSack(self, weight: int, weights: List[int], values: List[int], expected: Tuple[int, List[int]]):
        self.assertTupleEqual(expected, knap_sack_0_1(weight, weights, values))

    def testEmpty(self):
        self.assertSack(0, [1, 2, 3], [4, 5, 6], (0, []))
        self.assertSack(10, [], [], (0, []))

    def testSingleton(self):
        self.assertSack(10, [10], [99], (99, [0]))

    def testSimple(self):
        values = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
        self.assertSack(165,
                        [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
                        [92, 57, 49, 68, 60, 43, 67, 84, 87, 72],
                        self.formalize_result(0, [1, 1, 1, 1, 0, 1, 0, 0, 0, 0], values))

    def testComplex(self):
        values = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
        self.assertSack(750,
                        [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120],
                        values,
                        self.formalize_result(0, [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1], values))
