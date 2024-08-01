# https://leetcode.com/problems/add-binary/description/
# 67. Add Binary

# Time Complexity : O(1)
# Space Complexity : O(n+m)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
    
# Space Complexity: O(n + m), where n is the length of string a and m is the length of string b.