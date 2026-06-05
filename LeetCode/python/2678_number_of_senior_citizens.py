"""
2678. Number of Senior Citizens
https://leetcode.com/problems/number-of-senior-citizens/
Difficulty: Easy  Topic: String

Each entry in details is a string; characters at index 11-12 encode age.
Return the count of passengers strictly older than 60.
"""
from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for d in details if int(d[11:13]) > 60)
