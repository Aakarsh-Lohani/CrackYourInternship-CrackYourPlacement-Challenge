# https://leetcode.com/problems/permutations-ii/description//
# 47. Permutations II

from typing import Counter, List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        counter = Counter(nums)
        def findAllPermutations(res):
            if len(res) == len(nums):
                permutations.append(res)
                return 
            
            for key in counter:
                if counter[key]:
                    counter[key]-=1 # decrement visited key
                    findAllPermutations(res + [key])    
                    counter[key]+=1 # restore the state of visited key to find the next path
                
        findAllPermutations([])
        return permutations