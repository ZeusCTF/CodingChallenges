"""
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/
Difficulty: Easy  Topic: String

Return the length of the last word in the string (words separated by spaces).

Approach: Walk backwards, skipping trailing spaces, then count non-space chars.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        count = 0
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
        return count
