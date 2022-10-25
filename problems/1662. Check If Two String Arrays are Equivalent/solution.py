from operator import add
from functools import reduce

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return reduce(add, word1) == reduce(add, word2)
