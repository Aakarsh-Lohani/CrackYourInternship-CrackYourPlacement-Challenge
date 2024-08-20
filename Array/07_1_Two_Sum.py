# https://leetcode.com/problems/two-sum/description/
# 1. Two Sum

# Time Complexity: O(n)
# Space Complexity: O(n)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return (d[target-nums[i]],i)
            d[nums[i]]=i



# For Sorted array
# Two Pointer Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum_sorted(arr,target):
    l=0
    r=len(arr)-1
    while l<r:
        if arr[l]+arr[r]==target:
            return (l,r)
        elif arr[l]+arr[r]>target:
            r-=1
        else:
            l+=1
    return -1