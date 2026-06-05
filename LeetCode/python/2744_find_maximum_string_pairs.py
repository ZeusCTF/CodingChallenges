"""
2744. Find Maximum Number of String Pairs
https://leetcode.com/problems/find-maximum-number-of-string-pairs/
Difficulty: Easy  Topic: Hash Map, String

Count pairs (i, j) where words[i] is the reverse of words[j].

Approach: For each word, check whether its reverse has already been seen.
"""
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        pairs = 0
        for word in words:
            if word[::-1] in seen:
                pairs += 1
            seen.add(word)
        return pairs
