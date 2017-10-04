import numpy as np
from typing import List


def coin_change(value: int, changes: List[int]) -> int:
    if value == 0:
        return 0
    table = np.empty((value + 1, len(changes)), dtype = object)
    return permute_change(value, len(changes) - 1, changes, table)


def permute_change(value: int, index: int, changes: List[int], table: np.ndarray) -> int:
    if value == 0:
        return 1
    if index < 0:
        return 0
    if table[value][index]:
        return table[value][index]
    if changes[index] > value:
        table[value][index] = permute_change(value, index - 1, changes, table)
    else:
        multiple = value // changes[index]
        table[value][index] = 0
        changes_value = 0
        for m in range(0, multiple + 1):
            table[value][index] += permute_change(value - changes_value, index - 1, changes, table)
            changes_value += changes[index]
    return table[value][index]
