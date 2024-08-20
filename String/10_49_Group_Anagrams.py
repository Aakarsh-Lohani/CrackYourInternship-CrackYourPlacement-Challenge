# https://leetcode.com/problems/group-anagrams/description/
# 49. Group Anagrams

# Time Complexity: O(n*k)
# Space Complexity: O(n*k)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Create a frequency count tuple for the word
            count = [0] * 26  # Assuming only lowercase English letters
            for char in word:
                count[ord(char) - ord('a')] += 1
            # Use the tuple as the key
            anagram_map[tuple(count)].append(word)
        
        return list(anagram_map.values())
