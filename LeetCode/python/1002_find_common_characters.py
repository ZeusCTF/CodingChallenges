"""
1002. Find Common Characters
https://leetcode.com/problems/find-common-characters/
Difficulty: Easy  Topic: Hash Map, String

Return a list of all characters that appear in every string (with multiplicity).

Approach: Start with the frequency count of the first word; intersect with
each subsequent word's count using Counter's & operator (takes the minimum).
"""
import collections
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = collections.Counter(words[0])
        for word in words[1:]:
            ans &= collections.Counter(word)
        return list(ans.elements())
