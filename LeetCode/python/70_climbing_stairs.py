"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy  Topic: Dynamic Programming

Count the distinct ways to climb n stairs taking 1 or 2 steps at a time.

Approach: This is the Fibonacci sequence.  Use two variables to avoid
storing the full sequence.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
