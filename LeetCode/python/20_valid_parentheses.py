"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Topic: Stack

Return True if the input string of brackets is valid (every open bracket
is closed in the correct order).

Approach: Push open brackets onto a stack.  For each closing bracket,
check that the top of the stack holds the matching opener.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in match:
                stack.append(char)
            elif not stack or match[stack[-1]] != char:
                return False
            else:
                stack.pop()
        return not stack
