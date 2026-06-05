"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Topic: Two Pointers, Greedy

Find the two lines that together with the x-axis form a container holding
the most water.

Approach: Two pointers starting at each end.  The area is limited by the
shorter side; move that pointer inward in search of a taller line.
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            water = max(water, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return water
