import unittest
from main.dynapro.longest_common_subsequence import *


class LongestCommonSubsequenceTest(unittest.TestCase):

    def assertLCS(self, a: str, b: str, expected: str):
        self.assertEqual(expected, longest_common_subsequence(a, b))

    def testEmpty(self):
        self.assertLCS('', '', '')

    def testSingleton(self):
        self.assertLCS('a', 'a', 'a')
        self.assertLCS('a', 'b', '')

    def testOnes(self):
        self.assertLCS('aaaaa', 'aaa', 'aaa')

    def testSimple(self):
        self.assertLCS('ABCDGH', 'AEDFHR', 'ADH')
        self.assertLCS('AGGTAB', 'GXTXAYB', 'GTAB')
        self.assertLCS('MZJAWXU', 'XMJYAUZ', 'MJAU')
