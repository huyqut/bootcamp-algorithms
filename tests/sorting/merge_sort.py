from typing import List

import tests.sorting.base_sort
from main.sorting.merge_sort import merge_sort


class MergeSortTest(tests.sorting.base_sort.BaseSort):
    @classmethod
    def setUpClass(cls):
        cls.sort = staticmethod(merge_sort)
