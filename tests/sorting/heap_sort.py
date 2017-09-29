from typing import List

import tests.sorting.base_sort
from main.sorting.heap_sort import heap_sort


class HeapSortTest(tests.sorting.base_sort.BaseSort):

    def sort(self, numbers: List[int]) -> List[int]:
        heap_sort(numbers)
        return numbers
