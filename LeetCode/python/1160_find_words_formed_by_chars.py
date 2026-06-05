"""
1160. Find Words That Can Be Formed by Characters
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
Difficulty: Easy  Topic: Hash Map

Return the total length of all words that can be spelled using only the
characters in chars (each character used at most as many times as it appears).

Approach: Build a frequency map of chars; for each word check that its
frequency map is a subset.
"""
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_freq: dict = {}
        for c in chars:
            char_freq[c] = char_freq.get(c, 0) + 1

        total = 0
        for word in words:
            word_freq: dict = {}
            for c in word:
                word_freq[c] = word_freq.get(c, 0) + 1
            if all(word_freq.get(c, 0) <= char_freq.get(c, 0) for c in word_freq):
                total += len(word)
        return total
