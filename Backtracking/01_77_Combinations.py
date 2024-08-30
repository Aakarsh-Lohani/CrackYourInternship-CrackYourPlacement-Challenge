# https://leetcode.com/problems/combinations/description/
# 77. Combinations

# Time Complexity : O(NChooseK)
# Space Complexity : O(NChooseK)
from itertools import combinations
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(list(range(1, n+1)), k)
    

# Slower
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output