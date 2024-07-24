# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# 442. Find All Duplicates in an Array

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            if nums[abs(num)-1]<0:  # if the mapped position is negative , it means it must have been already visited, as nums contains only positive nos (as per ques)
                ans.append(abs(num))
            else: # marking the position in array as negative(irrespective of the number it contains) to track nos in range 1 to n , -1 in order to go to positions 0 to n-1 (as num is in range 1 to n)
                nums[abs(num)-1]*=-1
        return ans

