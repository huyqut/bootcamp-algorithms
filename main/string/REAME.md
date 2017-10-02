# String Algorithms

## String Search - Knuth-Morris-Pratt (KMP)

Idea of the KMP: If there is a mismatch between the haystack and the needle, the index of the needle does not need to reset at the beginning (and the index of the haystack does not need to go to exactly the next one). If we can find a pattern in such a way that we can go back to the middle of the string, then it is easier.

Solution: Find a proper suffix which is also a proper prefix.


