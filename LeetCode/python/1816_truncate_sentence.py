"""
1816. Truncate Sentence
https://leetcode.com/problems/truncate-sentence/
Difficulty: Easy  Topic: String

Return the sentence with only the first k words.
"""

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
