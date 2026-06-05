"""
1791. Find Center of Star Graph
https://leetcode.com/problems/find-center-of-star-graph/
Difficulty: Easy  Topic: Graph

The center node appears in every edge.  Find it by checking which node
the first two edges share.
"""
from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]
        return a if a == c or a == d else b
