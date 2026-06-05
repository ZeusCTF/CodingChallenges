"""
2299. Strong Password Checker II
https://leetcode.com/problems/strong-password-checker-ii/
Difficulty: Easy  Topic: String

A password is strong if:
  - Length >= 8
  - Contains at least one lowercase, uppercase, digit, and special character
  - No two adjacent characters are the same
"""

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        specials = set("!@#$%^&*()-+")
        has_lower = has_upper = has_digit = has_special = False
        for i, c in enumerate(password):
            if i > 0 and c == password[i - 1]:
                return False
            if c.islower():   has_lower   = True
            if c.isupper():   has_upper   = True
            if c.isdigit():   has_digit   = True
            if c in specials: has_special = True
        return has_lower and has_upper and has_digit and has_special
