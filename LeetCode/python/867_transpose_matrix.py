"""
867. Transpose Matrix
https://leetcode.com/problems/transpose-matrix/
Difficulty: Easy  Topic: Array, Matrix

Return the transpose of a matrix (rows become columns).

Approach: For each column index i, collect matrix[j][i] for all rows j.
"""
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        return [[matrix[r][c] for r in range(rows)] for c in range(cols)]
