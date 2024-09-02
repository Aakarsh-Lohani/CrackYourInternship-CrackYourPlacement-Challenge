# https://leetcode.com/problems/max-value-of-equation/description/
# 1499. Max Value of Equation

# Time Complexity: O(n)
# Space Complexity: O(n)
from typing import List
from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq = deque()
        max_value = float('-inf')
        
        for x, y in points:
            
            while dq and x - dq[0][1] > k:
                dq.popleft()
            
            if dq:
                max_value = max(max_value, y + x + dq[0][0])
            
            # Remove points from deque that have a smaller value of y - x
            while dq and dq[-1][0] <= y - x:
                dq.pop()
            dq.append((y - x, x))
        return max_value