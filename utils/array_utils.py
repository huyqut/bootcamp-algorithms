from typing import List, Callable


def ascend(numbers: List[int]) -> bool:
    def larger(a: int, b: int) -> bool:
        return a > b
    return monotonic(larger, numbers)


def descend(numbers: List[int]) -> bool:
    def smaller(a: int, b: int) -> bool:
        return a < b
    return monotonic(smaller, numbers)


def strict_ascend(numbers: List[int]) -> bool:
    def larger(a: int, b: int) -> bool:
        return a >= b
    return monotonic(larger, numbers)


def strict_descend(numbers: List[int]) -> bool:
    def smaller(a: int, b: int) -> bool:
        return a <= b
    return monotonic(smaller, numbers)


def monotonic(comparator: Callable[[int, int], bool], numbers: List[int]) -> bool:
    size = len(numbers)
    if size < 2:
        return False
    previous = numbers[0]
    for value in numbers[1:]:
        if not comparator(value, previous):
            return False
        previous = value
    return True
