import numpy as np


def longest_common_subsequence(a: str, b: str) -> str:
    if not a or not b:
        return ''

    table = np.array([[''] * len(a)] * len(b), dtype = object)
    if a[0] == b[0]:
        table[0][0] = a[0]
    for i in range(1, len(a)):
        if a[i] == b[0]:
            table[0][i] = b[0]
        else:
            table[0][i] = table[0][i - 1]
    for i in range(1, len(b)):
        if a[0] == b[i]:
            table[i][0] = str(a[0])
        else:
            table[i][0] = table[i - 1][0]
    for i in range(1, len(b)):
        for j in range(1, len(a)):
            if len(table[i - 1][j]) > len(table[i][j - 1]):
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i][j - 1]
            if b[i] == a[j] and len(table[i][j]) <= min(i, j):
                table[i][j] += a[j]
    return table[len(b) - 1][len(a) - 1]
