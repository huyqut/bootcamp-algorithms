HASH_CONST = 1000000000000037
HASH_BASE = 101


def rabin_karp(haystack: str, needle: str) -> int:
    if not haystack or not needle:
        return -1
    pattern = initial_roll_hash(needle)
    hash_value = initial_roll_hash(haystack[:len(needle)])
    if pattern == hash_value:
        if needle == haystack[:len(needle)]:
            return 0
    for i in range(len(needle), len(haystack)):
        significant = (ord(haystack[i - len(needle)]) * pow(HASH_BASE, len(needle) - 1, HASH_CONST)) % HASH_CONST
        hash_value -= significant
        if hash_value < 0:
            hash_value += HASH_CONST
        hash_value = (hash_value * HASH_BASE) % HASH_CONST
        hash_value = (hash_value + ord(haystack[i])) % HASH_CONST
        if hash_value == pattern:
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1


def initial_roll_hash(identifier: str) -> int:
    hash_value = 0
    for c in identifier:
        hash_value = ((hash_value * HASH_BASE) % HASH_CONST + ord(c)) % HASH_CONST
    return hash_value
