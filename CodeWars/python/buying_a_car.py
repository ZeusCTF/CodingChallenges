"""
Buying a Car
https://www.codewars.com/kata/buying-a-car
Topic: Math, Simulation

Each month:
  - savingsPerMonth increases by 1000 (starting from the given value)
  - Every even month the depreciation rate increases by 0.5%
  - Both car prices depreciate
Return [months, money_left_over] when savings >= cost of new car minus old car.
"""
from typing import List


def nbMonths(startPriceOld: float, startPriceNew: float,
             savingPerMonth: float, percentLoss: float) -> List:
    months = 0
    savings = 0

    while savings + startPriceOld < startPriceNew:
        months += 1
        savingPerMonth += 1000
        if months % 2 == 0:
            percentLoss += 0.5
        startPriceOld *= (1 - percentLoss / 100)
        startPriceNew *= (1 - percentLoss / 100)
        savings += savingPerMonth

    return [months, round(savings + startPriceOld - startPriceNew)]
