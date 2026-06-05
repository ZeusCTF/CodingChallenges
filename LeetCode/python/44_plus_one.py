"""
44 (LeetCode 66). Plus One
https://leetcode.com/problems/plus-one/
Difficulty: Easy  Topic: Array, Math

Increment the number represented as an array of digits by one.

Approach: Join digits into an integer, increment, split back to a list.
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(str(d) for d in digits)) + 1
        return [int(d) for d in str(n)]
