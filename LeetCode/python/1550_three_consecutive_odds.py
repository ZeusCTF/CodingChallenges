"""
1550. Three Consecutive Odds
https://leetcode.com/problems/three-consecutive-odds/
Difficulty: Easy  Topic: Array

Return True if the array contains three consecutive odd numbers.
"""
from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for n in arr:
            count = count + 1 if n % 2 != 0 else 0
            if count == 3:
                return True
        return False
