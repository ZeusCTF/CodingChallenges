"""
1200. Minimum Absolute Difference
https://leetcode.com/problems/minimum-absolute-difference/
Difficulty: Easy  Topic: Sorting

Find all pairs with the minimum absolute difference.

Approach: Sort the array; the minimum difference is always between adjacent
elements after sorting.
"""
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
        return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)
                if arr[i + 1] - arr[i] == min_diff]
