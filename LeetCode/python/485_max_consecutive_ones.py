"""
485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
Difficulty: Easy  Topic: Array

Find the maximum number of consecutive 1s in a binary array.

Approach: Running counter; reset on 0, track the maximum.
"""
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for n in nums:
            count = count + 1 if n == 1 else 0
            max_count = max(max_count, count)
        return max_count
