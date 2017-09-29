import sys
from tests.sorting.sort_params import INPUT, EXPECTED

EMPTY = {
    INPUT: [],
    EXPECTED: [],
}

SINGLETON = {
    INPUT: [0],
    EXPECTED: [0],
}

SIMPLE = {
    INPUT: [4, 3, 5, 1, 3, 2, -3, -11, 8, -13],
    EXPECTED: [-13, -11, -3, 1, 2, 3, 3, 4, 5, 8],
}

MIN = {
    INPUT: [0, -13, -3, -sys.maxsize - 1, 7, 100],
    EXPECTED: [-sys.maxsize - 1, -13, -3, 0, 7, 100],
}

MAX = {
    INPUT: [0, -13, -3, sys.maxsize, 7, 100],
    EXPECTED: [-13, -3, 0, 7, 100, sys.maxsize],
}

MOUNTAIN = {
    INPUT: [-3, 8, 32000, sys.maxsize, 640231, 31, 0, -3],
    EXPECTED: [-3, -3, 0, 8, 31, 32000, 640231, sys.maxsize],
}

VALLEY = {
    INPUT: [sys.maxsize, 3141, 123, 54, -321, -sys.maxsize - 1, 3, 223, sys.maxsize],
    EXPECTED: [-sys.maxsize - 1, -321, 3, 54, 123, 223, 3141, sys.maxsize, sys.maxsize],
}

ASCEND = {
    INPUT: [-sys.maxsize - 1, -sys.maxsize - 1, -142814, -3213, 0, 3214, 3214, 52352, sys.maxsize],
    EXPECTED: [-sys.maxsize - 1, -sys.maxsize - 1, -142814, -3213, 0, 3214, 3214, 52352, sys.maxsize],
}

DESCEND = {
    INPUT: [sys.maxsize, sys.maxsize, 643245, 14341, 14341, 312, 0, -321, -4124, -sys.maxsize - 1],
    EXPECTED: [-sys.maxsize - 1, -4124, -321, 0, 312, 14341, 14341, 643245, sys.maxsize, sys.maxsize]
}

RECTANGLE = {
    INPUT: [1, 1, 1, 1, 1, 1],
    EXPECTED: [1, 1, 1, 1, 1, 1],
}
