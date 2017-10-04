from typing import List, Tuple
import numpy as np


def edit_distance(source: str, target: str) -> List[Tuple[str, int, str]]:
    table = np.empty((len(source), len(target)), dtype = object)
    return optimize_distance(source, target, len(source) - 1, len(target) - 1, table)


def optimize_distance(source: str, target: str, i: int, j: int, table: np.ndarray):
    if i < 0:
        return [('+', x, target[x]) for x in range(j + 1)]
    if j < 0:
        return [('-', x, '') for x in range(i + 1)]
    if table[i][j]:
        return table[i][j]
    table[i][j] = []
    if source[i] == target[j]:
        table[i][j] = optimize_distance(source, target, i - 1, j - 1, table).copy()
    else:
        remove = optimize_distance(source, target, i - 1, j, table).copy()
        insert = optimize_distance(source, target, i, j - 1, table).copy()
        replace = optimize_distance(source, target, i - 1, j - 1, table).copy()
        if len(remove) < len(insert):
            if len(remove) < len(replace):
                table[i][j] = remove
                table[i][j].append(('-', i, ''))
            else:
                table[i][j] = replace
                table[i][j].append(('*', i, target[j]))
        else:
            if len(insert) < len(replace):
                table[i][j] = insert
                table[i][j].append(('+', i, target[j]))
            else:
                table[i][j] = replace
                table[i][j].append(('*', i, target[j]))
    return table[i][j]


print(edit_distance('sunday', 'saturday'))
