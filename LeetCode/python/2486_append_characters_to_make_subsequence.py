"""
2486. Append Characters to String to Make Subsequence
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
Difficulty: Medium  Topic: Two Pointers, Greedy

Return the minimum number of characters to append to s so that t is a
subsequence of s.

Approach: Greedy two-pointer: advance j each time s[i] matches t[j].
The remaining unmatched characters in t must be appended.
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return len(t) - j
