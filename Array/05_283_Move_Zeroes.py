# https://leetcode.com/problems/move-zeroes/description/
# 283. Move Zeroes

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[p1]=nums[i]
                p1+=1
        for j in range(p1,len(nums)):
            nums[j]=0
        return nums
        
        """
        Do not return anything, modify nums in-place instead.
        """