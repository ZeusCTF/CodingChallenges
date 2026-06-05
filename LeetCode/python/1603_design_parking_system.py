"""
1603. Design Parking System
https://leetcode.com/problems/design-parking-system/
Difficulty: Easy
Topic: Design, Simulation

Implement a parking system with big, medium, and small spots.
addCar(carType) returns True if there is a spot available for that type,
otherwise False.  carType is 1 (big), 2 (medium), or 3 (small).

Approach: Store available spots in a list indexed by carType-1.
  Decrement by 1 when a car parks.

Bug in original: `self.spots[carType - 1] -= carType` subtracted the car
type value instead of 1, causing medium cars to consume 2 spots and small
cars to consume 3 spots.
"""


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # Index 0 = big, 1 = medium, 2 = small
        self.spots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        idx = carType - 1
        if self.spots[idx] > 0:
            self.spots[idx] -= 1  # Fixed: was `-= carType`
            return True
        return False
