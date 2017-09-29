from sorting.quick_sort import quick_sort
import tests.sorting.base_sort
from typing import List


class QuickSortTest(tests.sorting.base_sort.BaseSort):

    def sort(self, numbers: List[int]) -> List[int]:
        quick_sort(numbers)
        return numbers
