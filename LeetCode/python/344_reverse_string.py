"""
344. Reverse String
https://leetcode.com/problems/reverse-string/
Difficulty: Easy  Topic: Two Pointers

Reverse a list of characters in-place.

Approach: Python slice assignment reverses in-place.
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
