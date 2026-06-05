"""
3110. Score of a String
https://leetcode.com/problems/score-of-a-string/
Difficulty: Easy  Topic: String

The score is the sum of absolute differences of ASCII values between
adjacent characters.
"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))
