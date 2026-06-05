"""
1704. Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/
Difficulty: Easy  Topic: String, Counting

Return True if the first and second halves of the string contain the same
number of vowels.
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        mid = len(s) // 2
        return (sum(1 for c in s[:mid] if c in vowels) ==
                sum(1 for c in s[mid:] if c in vowels))
