"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy  Topic: Array, Sliding Window

Find the maximum profit from one buy-low / sell-high transaction.

Approach: Track the minimum price seen so far.  At each day, the best
profit if we sell today is prices[i] - min_price.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            min_price = min(min_price, price)
            best = max(best, price - min_price)
        return best
