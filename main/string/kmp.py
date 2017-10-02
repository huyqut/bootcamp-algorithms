from typing import List


def kmp(haystack: str, needle: str) -> int:
    if not haystack or not needle:
        return -1
    failure = failure_function(needle)
    i = 0
    j = 0
    haystack_size = len(haystack)
    needle_length = len(needle)
    while i < haystack_size and j < needle_length:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if failure[j] >= 0:
                j = failure[j]
            else:
                j = 0
                i += 1

    return -1 if j != needle_length else i - needle_length


def failure_function(needle: str) -> List[int]:
    size = len(needle)
    table = [0] * size
    table[0] = -1
    match = 0
    for pos in range(1, size):
        if needle[pos] == needle[match]:
            table[pos] = table[match]
        else:
            table[pos] = match
            stop = False
            while not stop:
                match = table[match]
                stop = match < 0 or needle[pos] == needle[match]
        match += 1
    return table
