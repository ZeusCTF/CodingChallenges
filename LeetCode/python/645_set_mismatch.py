"""
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/
Difficulty: Easy  Topic: Math

An array of n integers should contain 1..n exactly once, but one number
is duplicated and one is missing.  Return [duplicate, missing].

Approach: Use sum and sum-of-squares formulas to derive both values.
"""
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff_sum   = n * (n + 1) // 2 - sum(nums)           # missing - dup
        diff_sumsq = n * (n + 1) * (2 * n + 1) // 6 - sum(x ** 2 for x in nums)
        # diff_sumsq = missing^2 - dup^2 = (missing+dup)(missing-dup)
        dup_plus_miss = diff_sumsq // diff_sum               # missing + dup
        missing = (diff_sum + dup_plus_miss) // 2
        dup     = dup_plus_miss - missing
        return [dup, missing]
