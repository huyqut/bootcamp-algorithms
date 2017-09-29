from sorting.heap_sort import heap_sort
import tests.sorting.base_sort
from typing import List


class HeapSortTest(tests.sorting.base_sort.BaseSort):

    def sort(self, numbers: List[int]) -> List[int]:
        heap_sort(numbers)
        return numbers
