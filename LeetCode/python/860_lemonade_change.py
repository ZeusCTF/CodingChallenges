"""
860. Lemonade Change
https://leetcode.com/problems/lemonade-change/
Difficulty: Easy  Topic: Greedy

Each lemonade costs $5.  Customers pay with $5, $10, or $20 bills.
Return True if you can give every customer correct change.

Approach: Greedy — for a $20 bill, prefer giving a $10 + $5 over three $5s
to preserve the more flexible $5 bills.
"""
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if not fives:
                    return False
                fives -= 1
                tens += 1
            else:  # bill == 20
                if tens and fives:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True
