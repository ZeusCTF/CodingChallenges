"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Topic: Math, String

Return True if the integer reads the same forwards and backwards.
Negative numbers are never palindromes.

Approach: Convert to string and compare to its reverse.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
