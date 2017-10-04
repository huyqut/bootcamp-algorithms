import numpy as np
from typing import Tuple, List


def min_cost_path(matrix: np.ndarray) -> Tuple[int, List[Tuple[int, int]]]:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0, []
    r = len(matrix)
    c = len(matrix[0])
    table = np.array([0] * c)
    trace = np.empty(c, dtype = object)
    table[0] = matrix[0][0]
    trace[0] = [(0, 0)]
    for i in range(1, c):
        table[i] = table[i - 1] + matrix[0][i]
        trace[i] = trace[i - 1].copy()
        trace[i].append((0, i))

    for i in range(1, r):
        table[0] += matrix[i][0]
        trace[0].append((i, 0))
        for j in range(1, c):
            if table[j] > table[j - 1]:
                table[j] = table[j - 1]
                trace[j] = trace[j - 1].copy()
            table[j] += matrix[i][j]
            trace[j].append((i, j))

    return table[c - 1], trace[c - 1]
