# https://leetcode.com/problems/valid-palindrome-ii/description/
# 680. Valid Palindrome II

# Time Complexity: O(n^2)   Check
# Space Complexity: O(n)
# two-pointer technique
class Solution:
    def validPalindrome(self, s: str) -> bool:
            p1=0
            p2=len(s)-1
            while p1<=p2:
                if s[p1]!=s[p2]:
                    string1=s[:p1]+s[p1+1:]
                    string2=s[:p2]+s[p2+1:]
                    return string1==string1[::-1] or string2==string2[::-1]
                p1+=1
                p2-=1
            return True


#Slow
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali_range(i: int, j: int) -> bool:
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True