import numpy as np


def binomial_coefficient(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    table = np.empty(n + 1, dtype = int)
    table.fill(0)
    table[0] = 1
    for i in range(1, n + 1):
        for j in reversed(range(1, i + 1)):
            table[j] += table[j - 1]
    return table[k]


print(binomial_coefficient(5, 2))
