"""
27. Remove Element
https://leetcode.com/problems/remove-element/
Difficulty: Easy  Topic: Two Pointers

Remove all occurrences of val in-place; return the count of remaining elements.

Approach: Write pointer k only advances when the current element != val.
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k
