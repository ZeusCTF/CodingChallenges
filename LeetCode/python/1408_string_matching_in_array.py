"""
1408. String Matching in an Array
https://leetcode.com/problems/string-matching-in-an-array/
Difficulty: Easy  Topic: String

Return all words that are substrings of another word in the array.
"""
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [w for i, w in enumerate(words)
                if any(w in words[j] for j in range(len(words)) if i != j)]
