"""
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
Difficulty: Medium  Topic: Hash Map, Greedy

Given a string, find the length of the longest palindrome that can be built
with those characters.

Approach: Count character frequencies.  Every even-count character
contributes fully.  Odd-count characters contribute their count minus 1.
If any odd-count character exists, we can place one in the center (+1).
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq: dict = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        length = 0
        has_odd = False
        for count in freq.values():
            length += count if count % 2 == 0 else count - 1
            if count % 2 != 0:
                has_odd = True
        return length + (1 if has_odd else 0)
