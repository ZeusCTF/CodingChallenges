"""
929. Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses/
Difficulty: Easy  Topic: String, Hash Set

Count the number of unique email addresses after applying rules:
  - Local part: ignore dots; ignore '+' and everything after it.
  - Domain part: unchanged.

Approach: Normalise each address and count distinct results with a set.
"""
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            unique.add(local + "@" + domain)
        return len(unique)
