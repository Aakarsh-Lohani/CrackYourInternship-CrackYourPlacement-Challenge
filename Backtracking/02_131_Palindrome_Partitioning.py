# https://leetcode.com/problems/palindrome-partitioning/description/
# 131. Palindrome Partitioning

# Fast
# Time Complexity: O(N * 2^N) (Check)
# Space Complexity: O(N * 2^N) (Check)
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # Precompute palindromes
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
        
        def backtrack(start: int, path: List[str]):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result


# Slow
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int, path: List[str]):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result