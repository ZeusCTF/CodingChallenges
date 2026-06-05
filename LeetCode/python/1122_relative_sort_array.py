"""
1122. Relative Sort Array
https://leetcode.com/problems/relative-sort-array/
Difficulty: Easy  Topic: Sorting, Hash Map

Sort arr1 so elements appear in the same order as arr2.
Elements not in arr2 go to the end, sorted ascending.

Approach: Process arr2 order first; collect remaining elements, sort, append.
"""
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {v: i for i, v in enumerate(arr2)}
        in_arr2     = [x for x in arr1 if x in order]
        not_in_arr2 = sorted(x for x in arr1 if x not in order)
        return sorted(in_arr2, key=lambda x: order[x]) + not_in_arr2
