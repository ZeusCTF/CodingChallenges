"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
Difficulty: Easy  Topic: Hash Map, String

Return True if t is an anagram of s (same characters, same frequencies).

Approach: Build character-frequency maps for both strings and compare.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def freq(word: str) -> dict:
            d: dict = {}
            for c in word:
                d[c] = d.get(c, 0) + 1
            return d
        return freq(s) == freq(t)
