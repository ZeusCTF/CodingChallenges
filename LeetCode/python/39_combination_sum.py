"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/
Difficulty: Medium  Topic: Backtracking

Find all unique combinations of candidates that sum to target.
The same number may be used multiple times.

Approach: DFS backtracking.  At each step either include candidates[i]
again or move to the next candidate.
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i: int, cur: List[int], total: int) -> None:
            if total == target:
                ans.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return ans
