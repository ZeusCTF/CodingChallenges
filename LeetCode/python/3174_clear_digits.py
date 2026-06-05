"""
3174. Clear Digits
https://leetcode.com/problems/clear-digits/
Difficulty: Easy  Topic: Stack, String

Remove all digits and the closest non-digit character to the left of each digit.

Approach: Use a stack.  For a letter push it; for a digit pop the last letter.
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
