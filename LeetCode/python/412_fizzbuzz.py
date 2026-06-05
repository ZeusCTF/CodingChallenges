"""
412. Fizz Buzz
https://leetcode.com/problems/fizz-buzz/
Difficulty: Easy  Topic: Math, String

Return a list of strings for 1..n: "FizzBuzz" if divisible by 3 and 5,
"Fizz" if by 3, "Buzz" if by 5, otherwise the number as a string.
"""
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
