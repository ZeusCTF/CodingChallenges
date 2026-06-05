"""
2185. Counting Words With a Given Prefix
https://leetcode.com/problems/counting-words-with-a-given-prefix/
Difficulty: Easy  Topic: String

Return the count of words that start with pref.
"""
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for w in words if w.startswith(pref))
