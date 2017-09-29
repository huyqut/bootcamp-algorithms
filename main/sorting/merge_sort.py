from typing import List


def merge_sort(numbers: List[int]) -> List[int]:
    size = len(numbers)
    if size < 2:
        return numbers
    if size == 2:
        if numbers[0] > numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers
    mid = size // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    merged = [0] * size
    lindex = 0
    rindex = 0
    lsize = mid
    rsize = size - mid

    while lindex < lsize or rindex < rsize:
        prefer_left = True
        if lindex == lsize or rindex < rsize and left[lindex] > right[rindex]:
            prefer_left = False
        if prefer_left:
            merged[lindex + rindex] = left[lindex]
            lindex += 1
        else:
            merged[lindex + rindex] = right[rindex]
            rindex += 1

    return merged
