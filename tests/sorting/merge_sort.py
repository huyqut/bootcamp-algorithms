from sorting.merge_sort import merge_sort
import tests.sorting.base_sort
from typing import List


class MergeSortTest(tests.sorting.base_sort.BaseSort):

    def sort(self, numbers: List[int]) -> List[int]:
        return merge_sort(numbers)
