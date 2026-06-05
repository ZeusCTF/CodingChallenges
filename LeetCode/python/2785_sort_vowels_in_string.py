"""
2785. Sort Vowels in a String
https://leetcode.com/problems/sort-vowels-in-a-string/
Difficulty: Medium  Topic: String, Sorting

Keep consonants in place; sort the vowels (by ASCII value) among themselves.

Approach: Extract and sort all vowels; walk the string replacing each vowel
position with the next sorted vowel.
"""

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        sorted_vowels = sorted(c for c in s if c in vowels)
        result = list(s)
        idx = 0
        for i, c in enumerate(result):
            if c in vowels:
                result[i] = sorted_vowels[idx]
                idx += 1
        return "".join(result)
