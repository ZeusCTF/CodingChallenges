"""
1. Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Hash Map

Given an array of integers and a target, return the indices of the two
numbers that add up to the target.

Approach: itertools.combinations enumerates every pair; check sum.
"""
import itertools
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (ix, x), (iy, y) in itertools.combinations(enumerate(nums), 2):
            if x + y == target:
                return [ix, iy]
        return []
