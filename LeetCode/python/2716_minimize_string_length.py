"""
2716. Minimize String Length
https://leetcode.com/problems/minimize-string-length/
Difficulty: Easy  Topic: Hash Set

Return the length of the minimized string (number of distinct characters).
"""

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
