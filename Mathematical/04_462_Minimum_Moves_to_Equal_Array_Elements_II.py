# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
# 462. Minimum Moves to Equal Array Elements II

# Time complexity: O(NlogN)
# Space complexity: O(1)
from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        res = 0
        while i < j:
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        return res