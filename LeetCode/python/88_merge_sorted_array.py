"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy  Topic: Two Pointers

Merge nums2 into nums1 in-place.  nums1 has m valid elements followed by n
zeros; nums2 has n elements.

Approach: Fill from the back to avoid overwriting unprocessed elements.
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
