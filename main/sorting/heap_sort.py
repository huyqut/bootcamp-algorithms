from typing import List


def heap_sort(numbers: List[int]) -> None:
    heapify(numbers)

    for end in reversed(range(1, len(numbers))):
        numbers[0], numbers[end] = numbers[end], numbers[0]
        sift_down(numbers, 0, end)


def heapify(numbers: List[int]) -> None:
    size = len(numbers)
    for index in reversed(range(0, size)):
        sift_down(numbers, index, size)


def sift_down(numbers: List[int], begin: int, end: int) -> None:
    index = begin
    swap = begin
    while index < end:
        lchild = 2 * index + 1
        if lchild >= end:
            break
        if numbers[swap] < numbers[lchild]:
            swap = lchild
        rchild = lchild + 1
        if rchild >= end:
            numbers[swap], numbers[index] = numbers[index], numbers[swap]
            break
        if numbers[swap] < numbers[rchild]:
            swap = rchild
        if swap == index:
            break
        numbers[swap], numbers[index] = numbers[index], numbers[swap]
        index = swap
