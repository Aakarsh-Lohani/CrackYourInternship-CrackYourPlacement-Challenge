# https://leetcode.com/problems/jump-game/description/
# 55. Jump Game

# Time Complexity : O(n)
# Space Complexity : O(1)
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        good_index = n - 1

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= good_index:
                good_index = i

        return good_index == 0