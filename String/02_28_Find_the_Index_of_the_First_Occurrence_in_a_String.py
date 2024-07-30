# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# 28. Find the Index of the First Occurrence in a String


# Time Complexity : O(n)
# Space Complexity :O(n)
#faster alternative - Knuth-Morris-Pratt (KMP) algorithm, which has a time complexity of O(n + m)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        lps = self.buildLPS(needle)
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def buildLPS(self, needle: str) -> list:
        lps = [0] * len(needle)
        length = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


#Slow
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)