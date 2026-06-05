"""
905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/
Difficulty: Easy  Topic: Two Pointers

Return an array with all even integers before all odd integers.

Approach: Partition into two lists and concatenate.
"""
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] +                [x for x in nums if x % 2 != 0]
