import unittest
from typing import Dict, Callable, Any
from tests.string import string_cases
from tests.string.string_params import *


class BaseStringSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.search: Callable[[str, str], int] = None

    def assertString(self, case: Dict[str, Any]):
        self.assertEqual(case[MATCH_START], self.search(case[HAYSTACK], case[NEEDLE_MATCH]))
        self.assertEqual(-1, self.search(case[HAYSTACK], case[NEEDLE_NOT_MATCH]))

    def testEmpty(self):
        self.assertString(string_cases.EMPTY)

    def testSingleton(self):
        self.assertString(string_cases.SINGLETON)

    def testSimple(self):
        self.assertString(string_cases.SIMPLE)

    def testAlpha(self):
        self.assertString(string_cases.ALPHA)

    def testNumeric(self):
        self.assertString(string_cases.NUMERIC)

    def testSimple(self):
        self.assertString(string_cases.SIMPLE)

    def testComplex(self):
        self.assertString(string_cases.COMPLEX)

    def testRandom(self):
        self.assertString(string_cases.RANDOM)
