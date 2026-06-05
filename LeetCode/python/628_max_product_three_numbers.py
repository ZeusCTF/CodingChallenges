"""
628. Maximum Product of Three Numbers
https://leetcode.com/problems/maximum-product-of-three-numbers/
Difficulty: Easy  Topic: Sorting, Math

Return the maximum product of any three integers in the array.

Approach: Sort the array.  The answer is either the top three values or
the two smallest (most negative) multiplied by the largest.
"""
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[0] * nums[1] * nums[-1])
