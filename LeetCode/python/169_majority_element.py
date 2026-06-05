"""
169. Majority Element
https://leetcode.com/problems/majority-element/
Difficulty: Easy  Topic: Array, Sorting

The majority element appears more than n/2 times.  Return it.

Approach: Sort the array; the element at the middle index is always the
majority element.
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
