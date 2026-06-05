"""
3194. Minimum Average of Smallest and Largest Elements
https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
Difficulty: Easy  Topic: Sorting, Two Pointers

Repeatedly pair the smallest and largest elements; return the minimum
average of all pairs.
"""
from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = []
        left, right = 0, len(nums) - 1
        while left < right:
            averages.append((nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return min(averages)
