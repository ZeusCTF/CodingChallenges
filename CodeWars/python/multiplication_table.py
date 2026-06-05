"""
Multiplication Table
https://www.codewars.com/kata/multiplication-table
Topic: Array, Math

Return an n×n multiplication table as a list of lists.
Row i (1-indexed), column j (1-indexed) = i * j.
"""
from typing import List


def multiplication_table(size: int) -> List[List[int]]:
    return [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]
