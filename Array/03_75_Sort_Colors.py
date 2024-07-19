# https://leetcode.com/problems/sort-colors/description/
# 75. Sort Colors

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,m,h=0,0,len(nums)-1   #partioning the array into 3 parts
        while m<=h:             #m is the current element, l is the index of 0, h is the index of 2
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l] #swap the current element with the element at index l
                l+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m],nums[h]=nums[h],nums[m] #swap the current element with the element at index h
                
                h-=1
        return nums

