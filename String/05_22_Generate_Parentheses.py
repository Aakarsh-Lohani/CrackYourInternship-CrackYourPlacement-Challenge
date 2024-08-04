# https://leetcode.com/problems/generate-parentheses/description/
# 22. Generate Parentheses

# Time Complexity :Check
# Space Complexity : Check

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s = '', l = 0, r = 0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if l < n:
                backtrack(s+'(', l+1, r)
            if r < l:
                backtrack(s+')', l, r+1)

        res = []
        backtrack()
        return res