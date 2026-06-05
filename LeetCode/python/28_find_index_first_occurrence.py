"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Difficulty: Easy  Topic: String

Return the index of the first occurrence of needle in haystack, or -1.

Approach: Python's built-in str.find() returns -1 on miss, matching the spec.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
