"""
3042. Count Prefix and Suffix Pairs I
https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/
Difficulty: Easy  Topic: String

Count pairs (i, j) with i < j where words[i] is both a prefix and suffix
of words[j].
"""
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    res += 1
        return res
