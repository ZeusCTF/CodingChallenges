"""
884. Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences/
Difficulty: Easy  Topic: Hash Map, String

Return all words that appear exactly once across both sentences combined.

Approach: Combine both sentences, count word frequencies; keep freq == 1.
"""
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq: dict = {}
        for word in (s1 + " " + s2).split():
            freq[word] = freq.get(word, 0) + 1
        return [word for word, count in freq.items() if count == 1]
