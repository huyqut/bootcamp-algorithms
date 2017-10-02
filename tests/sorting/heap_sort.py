from typing import List

import tests.sorting.base_sort
from main.sorting.heap_sort import heap_sort


class HeapSortTest(tests.sorting.base_sort.BaseSort):

    @classmethod
    def setUpClass(cls):
        cls.sort = staticmethod(heap_sort)
