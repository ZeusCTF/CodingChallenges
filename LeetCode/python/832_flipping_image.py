"""
832. Flipping an Image
https://leetcode.com/problems/flipping-an-image/
Difficulty: Easy  Topic: Array

Flip each row horizontally, then invert each element (0↔1).

Approach: Reverse each row with [::-1], then use a list comprehension to
toggle bits with `1 - x`.
"""
from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 - x for x in row[::-1]] for row in image]
