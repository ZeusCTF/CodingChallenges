"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
Difficulty: Easy
Topic: Math

Reverse the digits of a signed 32-bit integer.  Return 0 if the reversed
value overflows the 32-bit signed range [-2^31, 2^31 - 1].

Approach: Convert to string, reverse, handle sign separately.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_val = sign * int(str(abs(x))[::-1])
        if reversed_val < -2**31 or reversed_val > 2**31 - 1:
            return 0
        return reversed_val
