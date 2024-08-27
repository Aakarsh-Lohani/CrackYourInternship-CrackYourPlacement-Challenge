# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/
# 1647. Minimum Deletions to Make Character Frequencies Unique

# Time Complexity : O(NlogN) (Check)
# Space Complexity: O(N)
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        freq = list(counter.values())
        freq.sort(reverse=True)
        
        deletions = 0
        for i in range(1, len(freq)):
            while freq[i] > 0 and freq[i] >= freq[i - 1]:
                freq[i] -= 1
                deletions += 1
                
        return deletions