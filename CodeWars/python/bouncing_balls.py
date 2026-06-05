"""
Bouncing Balls
https://www.codewars.com/kata/bouncing-balls
Topic: Math, Simulation

A ball is dropped from height h.  After each bounce it reaches bounce*h.
A child watches from a window at height window.  Return how many times the
child sees the ball (going down AND coming back up each bounce counts as 2),
or -1 if the parameters are invalid.
"""


def bouncing_ball(h: float, bounce: float, window: float) -> int:
    if h <= 0 or not (0 < bounce < 1) or window >= h:
        return -1
    views = 1           # child always sees the initial drop
    while h * bounce > window:
        h *= bounce
        views += 2      # up + down on each subsequent bounce
    return views
