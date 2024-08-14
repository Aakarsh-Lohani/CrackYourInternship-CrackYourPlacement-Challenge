# https://leetcode.com/problems/reverse-words-in-a-string/description/
# 151. Reverse Words in a String

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])