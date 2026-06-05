"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
Topic: String

Find the longest common prefix among all strings in the array.

Approach: Sort the array; only the first and last strings need to be
compared, because all other strings lie alphabetically between them.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s = sorted(strs)
        prefix = ""
        for i, char in enumerate(s[0]):
            if i < len(s[-1]) and char == s[-1][i]:
                prefix += char
            else:
                break
        return prefix
