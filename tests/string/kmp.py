from main.string.kmp import kmp
import tests.string.base_string


class KMPTest(tests.string.base_string.BaseStringSearchTest):

    @classmethod
    def setUpClass(cls):
        cls.search = staticmethod(kmp)
