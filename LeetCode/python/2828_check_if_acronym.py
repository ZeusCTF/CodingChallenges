"""
2828. Check if a String Is an Acronym of Words
https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/
Difficulty: Easy  Topic: String

Return True if s is formed by taking the first letter of each word.
"""
from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(w[0] for w in words) == s
