from typing import List


def quick_sort(numbers: List[int]) -> None:
    quick_divide(numbers, 0, len(numbers))


def partition(numbers: List[int], begin: int, end: int) -> int:
    if not numbers or begin >= end:
        return begin
    pivot = begin
    for index in range(begin + 1, end):
        if numbers[index] <= numbers[begin]:
            pivot += 1
            numbers[index], numbers[pivot] = numbers[pivot], numbers[index]
    numbers[begin], numbers[pivot] = numbers[pivot], numbers[begin]
    return pivot


def quick_divide(numbers: List[int], begin: int, end: int) -> None:
    if not numbers or begin >= end:
        return
    pivot = partition(numbers, begin, end)
    quick_divide(numbers, begin, pivot)
    quick_divide(numbers, pivot + 1, end)
