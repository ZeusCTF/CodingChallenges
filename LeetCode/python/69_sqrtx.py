"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/
Difficulty: Easy
Topic: Binary Search, Math

Given a non-negative integer x, return the floor of its square root without
using any built-in exponent functions or operators.

Approach: Binary search over [0, x].
  - If mid*mid == x: exact answer.
  - If mid*mid < x:  answer is at least mid; move left bound to mid+1.
  - If mid*mid > x:  answer is less than mid; move right bound to mid-1.
  - When the loop ends, right holds the floor of sqrt(x).

Bug in original: bounds were updated to `mid` instead of `mid±1`,
causing an infinite loop on non-perfect squares (e.g. x=8).
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1   # Fixed: was `left = mid`
            else:
                right = mid - 1  # Fixed: was `right = mid`
        return right
