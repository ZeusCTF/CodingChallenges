"""
2404. Most Frequent Even Element
https://leetcode.com/problems/most-frequent-even-element/
Difficulty: Easy  Topic: Hash Map

Return the most frequent even element.  On a tie, return the smaller one.
Return -1 if there are no even elements.
"""
from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq: dict = {}
        for n in nums:
            if n % 2 == 0:
                freq[n] = freq.get(n, 0) + 1
        if not freq:
            return -1
        return min(freq, key=lambda x: (-freq[x], x))
