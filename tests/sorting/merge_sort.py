from typing import List

import tests.sorting.base_sort
from main.sorting.merge_sort import merge_sort


class MergeSortTest(tests.sorting.base_sort.BaseSort):

    def sort(self, numbers: List[int]) -> List[int]:
        return merge_sort(numbers)
