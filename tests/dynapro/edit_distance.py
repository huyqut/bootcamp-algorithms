import unittest
from typing import List, Tuple
from main.dynapro.edit_distance import *


class EditDistanceTest(unittest.TestCase):

    def assertDistance(self, source: str, target: str, expected: List[Tuple[str, int, str]]):
        self.assertListEqual(expected, edit_distance(source, target))

    def testEmpty(self):
        self.assertDistance('', '', [])

    def testSingleTon(self):
        self.assertDistance('', 'a', [('+', 0, 'a')])
        self.assertDistance('a', '', [('-', 0, '')])
        self.assertDistance('b', 'a', [('*', 0, 'a')])

    def testSimple(self):
        self.assertDistance('geek', 'gesek', [('+', 1, 's')])
        self.assertDistance('cat', 'cut', [('*', 1, 'u')])
        self.assertDistance('sunday', 'saturday', [('+', 0, 'a'), ('+', 0, 't'), ('*', 2, 'r')])
