"""
2942. Find Words Containing Character
https://leetcode.com/problems/find-words-containing-character/
Difficulty: Easy  Topic: String

Return the indices of words that contain the character x.
"""
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
