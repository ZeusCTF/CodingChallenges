"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy  Topic: Two Pointers

Modify nums in-place so duplicates are removed; return the count of unique
elements.

Approach: Slow pointer k marks the next write position.  Fast pointer i
scans ahead; when nums[i] differs from nums[i-1], write it at k.
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
