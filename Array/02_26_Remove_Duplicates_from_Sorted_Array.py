# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# 26. Remove Duplicates from Sorted Array

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
        return j
