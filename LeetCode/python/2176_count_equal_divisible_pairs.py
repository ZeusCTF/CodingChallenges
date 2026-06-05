"""
2176. Count Equal and Divisible Pairs in an Array
https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
Difficulty: Easy  Topic: Array

Count pairs (i, j) where i < j, nums[i] == nums[j], and (i*j) % k == 0.
"""
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count
