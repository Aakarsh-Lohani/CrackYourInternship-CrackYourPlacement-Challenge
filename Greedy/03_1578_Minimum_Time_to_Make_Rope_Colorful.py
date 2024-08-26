# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
# 1578. Minimum Time to Make Rope Colorful

# Time Complexity : O(N)
# Space Complexity: O(1)
from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total_cost = 0
        prev_cost = cost[0]
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                total_cost += min(prev_cost, cost[i])
                prev_cost = max(prev_cost, cost[i])
            else:
                prev_cost = cost[i]
        
        return total_cost