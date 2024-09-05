# https://leetcode.com/problems/subsets/description/
# 78. Subsets

# Time Complexity :O(N*(2^N))
# Space Complexity :O(N∗(2^N))
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, path: List[int]):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        result = []
        backtrack(0, [])
        return result