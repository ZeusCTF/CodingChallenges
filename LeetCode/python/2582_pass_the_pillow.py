"""
2582. Pass the Pillow
https://leetcode.com/problems/pass-the-pillow/
Difficulty: Easy  Topic: Math, Simulation

n people in a line pass a pillow back and forth.  After `time` seconds,
return the 1-indexed position of the holder.

Approach: The cycle length is 2*(n-1).  Use modulo to find position within
one cycle, then map to the actual index.
"""

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= 2 * (n - 1)
        return time + 1 if time <= n - 1 else n - (time - (n - 1))
