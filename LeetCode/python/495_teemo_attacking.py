"""
495. Teemo Attacking
https://leetcode.com/problems/teemo-attacking/
Difficulty: Easy  Topic: Array, Simulation

Given sorted attack times and a poison duration, return total seconds the
enemy is poisoned (overlapping durations do not stack).

Approach: For each attack, add the full duration unless the next attack
arrives before it expires, in which case add only the gap.
"""
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration
