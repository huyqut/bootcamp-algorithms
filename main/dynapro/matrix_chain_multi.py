import numpy as np
from typing import List


def matrix_chain_multi(matrix_sizes: List[int]) -> int:
    if len(matrix_sizes) < 3:
        return 0
    table = np.empty((len(matrix_sizes), len(matrix_sizes)), dtype = object)
    return permute_chain(0, len(matrix_sizes) - 1, matrix_sizes, table)


def permute_chain(begin: int, end: int, matrix_sizes: List[int], table: np.ndarray) -> int:
    if begin + 1 >= end:
        return 0
    if table[begin][end]:
        return table[begin][end]
    for i in range(begin + 1, end):
        first = permute_chain(begin, i, matrix_sizes, table)
        second = permute_chain(i, end, matrix_sizes, table)
        total = first + second + matrix_sizes[begin] * matrix_sizes[i] * matrix_sizes[end]
        if not table[begin][end] or total < table[begin][end]:
            table[begin][end] = total
    return table[begin][end]
