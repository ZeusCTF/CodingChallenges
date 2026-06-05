"""
3019. Number of Changing Keys
https://leetcode.com/problems/number-of-changing-keys/
Difficulty: Easy  Topic: String

Count how many times the key changes (case-insensitive) while typing s.
"""

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        return sum(1 for i in range(1, len(s)) if s[i] != s[i - 1])
