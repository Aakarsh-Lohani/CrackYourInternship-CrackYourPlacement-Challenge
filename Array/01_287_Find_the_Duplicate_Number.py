# https://leetcode.com/problems/find-the-duplicate-number/description/
# 287. Find the Duplicate Number

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        l=[0 for j in range (0,n)]
        for i in nums:
            if l[i-1]==0:
                l[i-1]=1

            else:
                return i