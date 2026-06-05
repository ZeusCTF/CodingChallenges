"""
2161. Partition Array According to Given Pivot
https://leetcode.com/problems/partition-array-according-to-given-pivot/
Difficulty: Medium  Topic: Two Pointers, Array

Rearrange so all elements less than pivot come first, then equal, then greater,
preserving relative order within each group.
"""
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less    = [x for x in nums if x < pivot]
        equal   = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]
        return less + equal + greater
