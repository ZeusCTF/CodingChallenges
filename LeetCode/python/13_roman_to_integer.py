"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy
Topic: Hash Map, String

Convert a Roman numeral string to an integer.

Approach: Walk left to right.  If the current symbol's value is greater
than the previous one, we need to subtract twice the previous value
(because we already added it) and add the current.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for char in reversed(s):
            cur = roman[char]
            if cur < prev:
                total -= cur
            else:
                total += cur
            prev = cur
        return total
