# https://leetcode.com/problems/longest-common-prefix/description/
# 14. Longest Common Prefix

# Time Complexity : O(m*n)
# Space Complexity :O(1)
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix=strs[0]  # Assuming first word as prefix

        for string in strs[1:]:  #Checking from second word
            while string[:len(prefix)]!=prefix and prefix:
                prefix=prefix[:-1]  #As long as it is not same , we delete the last character of prefix
        return prefix