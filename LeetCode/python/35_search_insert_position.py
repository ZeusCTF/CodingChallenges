"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
Difficulty: Easy  Topic: Binary Search

Return the index of target in a sorted array, or the index where it would
be inserted to keep the array sorted.

Approach: Standard binary search; when not found, left is the insert position.
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
