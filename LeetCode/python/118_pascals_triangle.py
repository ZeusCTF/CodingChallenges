"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
Difficulty: Easy  Topic: Array, DP

Return the first numRows rows of Pascal's triangle.

Approach: Each row is built by summing adjacent pairs of the previous row,
padded with a leading and trailing 0.
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            padded = [0] + res[-1] + [0]
            row = [padded[j] + padded[j + 1] for j in range(len(res[-1]) + 1)]
            res.append(row)
        return res
