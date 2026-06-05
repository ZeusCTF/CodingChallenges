"""
657. Robot Return to Origin
https://leetcode.com/problems/robot-return-to-origin/
Difficulty: Easy  Topic: Simulation

Given a string of moves (U/D/L/R), return True if the robot returns to
the origin.

Approach: Count each direction; L must equal R and U must equal D.
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("L") == moves.count("R") and                moves.count("U") == moves.count("D")
