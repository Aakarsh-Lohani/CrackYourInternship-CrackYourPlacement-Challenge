# https://leetcode.com/problems/longest-repeating-character-replacement/
# 424. Longest Repeating Character Replacement

# Two Pointer - Faster (still check for better solution)
# Time Complexity : O(n) (Check)
# Space Complexity : O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        c_frequency = {}
        longest_str_len = 0
        for r in range(len(s)):
            
            if not s[r] in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1
            
            # Replacements cost = cells count between left and right - highest frequency
            cells_count = r - l + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_str_len = max(longest_str_len, cells_count)
                
            else:
                c_frequency[s[l]] -= 1
                if not c_frequency[s[l]]:
                    c_frequency.pop(s[l])
                l += 1
        
        return longest_str_len
		
        

# Sliding Window
# Slow
# Time Complexity : O(n) (Check)
# Space Complexity : O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        res=0
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            while (r-l+1) - max(count.values())>k:
                count[s[l]] -=1
                l+=1
            res=max(res, r-l+1)
        return res
        