"""
1436. Destination City
https://leetcode.com/problems/destination-city/
Difficulty: Easy  Topic: Hash Map

Find the destination city: the city that is never a source.

Approach: Collect all source cities into a set; return the destination that
doesn't appear as a source.
"""
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = {src for src, _ in paths}
        for _, dest in paths:
            if dest not in sources:
                return dest
        return ""
