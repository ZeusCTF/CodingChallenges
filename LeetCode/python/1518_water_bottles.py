"""
1518. Water Bottles
https://leetcode.com/problems/water-bottles/
Difficulty: Easy  Topic: Simulation

Start with numBottles full bottles.  After drinking, exchange every
numExchange empty bottles for one full bottle.  Return total drunk.

Approach: Simulate each round of exchanges.
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empties = numBottles
        while empties >= numExchange:
            new_full = empties // numExchange
            total += new_full
            empties = empties % numExchange + new_full
        return total
