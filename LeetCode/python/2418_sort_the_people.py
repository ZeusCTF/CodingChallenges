"""
2418. Sort the People
https://leetcode.com/problems/sort-the-people/
Difficulty: Easy  Topic: Sorting

Return names sorted by descending height.
"""
from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
