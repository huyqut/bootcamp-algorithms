from main.string.rabin_karp import rabin_karp
import tests.string.base_string


class RabinKarpTest(tests.string.base_string.BaseStringSearchTest):

    @classmethod
    def setUpClass(cls):
        cls.search = staticmethod(rabin_karp)
