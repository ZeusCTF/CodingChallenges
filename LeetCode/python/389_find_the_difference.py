"""
389. Find the Difference
https://leetcode.com/problems/find-the-difference/
Difficulty: Easy  Topic: Bit Manipulation / Math

String t is formed by shuffling s and adding one extra letter.  Find it.

Approach: Sum the ASCII values; the difference is the added character.
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))
