# https://leetcode.com/problems/majority-element/description/
# 169. Majority Element


# Time Complexity : O(n)
# Space Complexity : O(1)
from typing import List
# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None 

        for num in nums:
            if count==0:
                candidate = num
            count+=(1 if candidate==num else -1)
        return candidate 