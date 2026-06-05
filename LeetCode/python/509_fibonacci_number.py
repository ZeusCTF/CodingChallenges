"""
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
Difficulty: Easy  Topic: Dynamic Programming

Return F(n) where F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).

Approach: Iterative with two variables; O(n) time, O(1) space.
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
