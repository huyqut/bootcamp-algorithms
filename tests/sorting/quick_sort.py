from typing import List

import tests.sorting.base_sort
from main.sorting.quick_sort import quick_sort


class QuickSortTest(tests.sorting.base_sort.BaseSort):

    def sort(self, numbers: List[int]) -> List[int]:
        quick_sort(numbers)
        return numbers
