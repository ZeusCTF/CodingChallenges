"""
1662. Check If Two String Arrays are Equivalent
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
Difficulty: Easy  Topic: String

Return True if concatenating all strings in word1 equals concatenating
all strings in word2.
"""
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
