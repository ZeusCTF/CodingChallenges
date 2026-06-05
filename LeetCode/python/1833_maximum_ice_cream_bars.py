"""
1833. Maximum Ice Cream Bars
https://leetcode.com/problems/maximum-ice-cream-bars/
Difficulty: Medium  Topic: Greedy, Sorting

Buy as many ice cream bars as possible with `coins`.
Greedy: buy the cheapest ones first.
"""
from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        bars = 0
        for price in sorted(costs):
            if price > coins:
                break
            coins -= price
            bars += 1
        return bars
