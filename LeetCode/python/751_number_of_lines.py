"""
751 (LeetCode 806). Number of Lines To Write String
https://leetcode.com/problems/number-of-lines-to-write-string/
Difficulty: Easy  Topic: Array, Simulation

Count how many lines are needed and the width of the last line.
"""
from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, current = 1, 0
        for c in s:
            w = widths[ord(c) - ord("a")]
            if current + w > 100:
                lines += 1
                current = w
            else:
                current += w
        return [lines, current]
