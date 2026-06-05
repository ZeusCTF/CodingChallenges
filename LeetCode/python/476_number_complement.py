"""
476. Number Complement
https://leetcode.com/problems/number-complement/
Difficulty: Easy  Topic: Bit Manipulation

Return the complement of the integer (flip all bits in its binary representation).

Approach: Format as binary string, flip each bit, convert back.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]  # strip "0b" prefix
        flipped = "".join("0" if b == "1" else "1" for b in binary)
        return int(flipped, 2)
