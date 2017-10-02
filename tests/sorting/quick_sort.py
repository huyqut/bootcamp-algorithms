from typing import List

import tests.sorting.base_sort
from main.sorting.quick_sort import quick_sort


class QuickSortTest(tests.sorting.base_sort.BaseSort):

    @classmethod
    def setUpClass(cls):
        cls.sort = staticmethod(quick_sort)
