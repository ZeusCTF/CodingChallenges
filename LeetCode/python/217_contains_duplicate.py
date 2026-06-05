"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy  Topic: Hash Set

Return True if any value appears at least twice.

Approach: A set holds unique elements; if its length is less than the
array's length, duplicates exist.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
