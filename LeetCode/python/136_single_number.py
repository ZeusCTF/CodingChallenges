"""
136. Single Number
https://leetcode.com/problems/single-number/
Difficulty: Easy  Topic: Bit Manipulation

Every element appears twice except one.  Find the element that appears once.

Approach: XOR all numbers.  Pairs cancel (a ^ a == 0); the lone element remains.
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result
