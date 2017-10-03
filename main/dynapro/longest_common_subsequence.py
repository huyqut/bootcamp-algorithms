import numpy as np


def longest_common_subsequence(a: str, b: str) -> str:
    if not a or not b:
        return ''

    table = np.array([''] * len(a), dtype = object)
    if a[0] == b[0]:
        table[0] = a[0]
    for i in range(1, len(a)):
        if a[i] == b[0]:
            table[i] = b[0]
        else:
            table[i] = table[i - 1]
    for i in range(1, len(b)):
        if b[i] == a[0]:
            table[0] = a[0]
        for j in range(1, len(a)):
            if len(table[j - 1]) > len(table[j]):
                table[j] = table[j - 1]
            if b[i] == a[j] and len(table[j]) <= min(i, j):
                table[j] += a[j]
    return table[len(a) - 1]
