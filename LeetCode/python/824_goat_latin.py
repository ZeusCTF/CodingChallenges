"""
824. Goat Latin
https://leetcode.com/problems/goat-latin/
Difficulty: Easy  Topic: String

Convert each word in the sentence to Goat Latin:
  - Vowel-start: append "ma"
  - Consonant-start: move first letter to end, append "ma"
  - Append one 'a' per word index (1-indexed)
"""

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []
        for i, word in enumerate(words, start=1):
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            new_word += "a" * i
            result.append(new_word)
        return " ".join(result)
