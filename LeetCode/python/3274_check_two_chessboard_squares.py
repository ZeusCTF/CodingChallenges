"""
3274. Check if Two Chessboard Squares Have the Same Color
https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/
Difficulty: Easy  Topic: Math

Two squares have the same color iff the sum of (column_index + row_index)
has the same parity for both squares.

Column a-h maps to 1-8; row 1-8 is already an integer.
"""

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def parity(coord: str) -> int:
            return (ord(coord[0]) - ord('a') + int(coord[1])) % 2
        return parity(coordinate1) == parity(coordinate2)
