from tests.string.string_params import *

EMPTY = {
    HAYSTACK: '',
    NEEDLE_MATCH: '',
    MATCH_START: -1,
    NEEDLE_NOT_MATCH: '0',
}

SINGLETON = {
    HAYSTACK: 'a',
    NEEDLE_MATCH: 'a',
    MATCH_START: 0,
    NEEDLE_NOT_MATCH: 'b',
}

ALPHA = {
    HAYSTACK: 'PENPINEAPPLEAPPLEPEN',
    NEEDLE_MATCH: 'LEAP',
    MATCH_START: 10,
    NEEDLE_NOT_MATCH: 'PPAP',
}

NUMERIC = {
    HAYSTACK: '1415926535897932384626433832795',
    NEEDLE_MATCH: '358979',
    MATCH_START: 8,
    NEEDLE_NOT_MATCH: '911',
}

SIMPLE = {
    HAYSTACK: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum',
    NEEDLE_MATCH: 'consectetur adipiscing elit, sed do eiusmod tempor incididunt',
    MATCH_START: 28,
    NEEDLE_NOT_MATCH: 'consectetur adipiscing elit, sed do eiusmod empor incididunt'
}

COMPLEX = {
    HAYSTACK: 'a paricipater in parachute tries to participate in parachute at the dday',
    NEEDLE_MATCH: 'participate in parachute',
    MATCH_START: 36,
    NEEDLE_NOT_MATCH: 'paricipater i parachute',
}

RANDOM = {
    HAYSTACK: 'abccbaabacababccbaabc',
    NEEDLE_MATCH: 'abacababc',
    MATCH_START: 6,
    NEEDLE_NOT_MATCH: 'acbaababcc',
}
