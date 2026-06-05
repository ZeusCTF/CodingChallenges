"""
1460. Make Two Arrays Equal by Reversing Subarrays
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
Difficulty: Easy  Topic: Sorting

Return True if arr can be made equal to target by reversing subarrays.
Two arrays can be made equal this way if and only if they contain the same
elements (same multiset).
"""
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
