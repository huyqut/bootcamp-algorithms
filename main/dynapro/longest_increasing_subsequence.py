from typing import List


def longest_increasing_subsequence(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    # Initialize meta info
    trace: List[int] = [-1]
    length: List[int] = [0]
    max_trace = 0

    # Trace the longest subsequence that ends with a number less than the current one
    for i in range(1, len(numbers)):
        trace.append(-1)
        for j in range(i):
            if numbers[j] <= numbers[i] and \
               (trace[i] == -1 or length[j] > length[trace[i]]):
                trace[i] = j
        length.append(1 + length[trace[i]] if trace[i] != -1 else 0)
        if length[i] > length[max_trace]:
            max_trace = i

    # Trace back the longest increasing subsequence to return result
    lis = []
    while max_trace != -1:
        lis.append(numbers[max_trace])
        max_trace = trace[max_trace]

    return list(reversed(lis))
