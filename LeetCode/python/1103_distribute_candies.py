"""
1103. Distribute Candies to People
https://leetcode.com/problems/distribute-candies-to-people/
Difficulty: Easy  Topic: Simulation

Distribute candies to num_people in a circle; the i-th give (1-indexed)
gives min(i, remaining) candies.  Return the final distribution.
"""
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 0
        while candies > 0:
            result[i % num_people] += min(i + 1, candies)
            candies -= i + 1
            i += 1
        return result
