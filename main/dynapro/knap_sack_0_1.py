import numpy as np
from typing import List, Tuple


def knap_sack_0_1(total_weight: int, weights: List[int], values: List[int]) -> Tuple[int, List[int]]:
    table = np.empty((total_weight + 1, len(weights)), dtype = object)
    return fit_sack(total_weight, len(weights) - 1, weights, values, table)


def fit_sack(weight: int, index: int, weights: List[int], values: List[int], table: np.ndarray) -> Tuple[int, List[int]]:
    if weight < 0 or index < 0:
        return 0, []
    if table[weight][index]:
        return table[weight][index]
    # By default, don't take this item
    table[weight][index] = fit_sack(weight, index - 1, weights, values, table)
    if weight >= weights[index]:
        # If the sack can hold the weight of this item, try to take it
        take_item = fit_sack(weight - weights[index], index - 1, weights, values, table)
        # If adding this item results in greater value, choose it
        if take_item[0] + values[index] > table[weight][index][0]:
            table[weight][index] = take_item[0] + values[index], take_item[1] + [index]
    return table[weight][index]
