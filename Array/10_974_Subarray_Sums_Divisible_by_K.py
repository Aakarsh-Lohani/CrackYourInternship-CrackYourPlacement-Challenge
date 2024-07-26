# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
# 974. Subarray Sums Divisible by K


# Time Complexity : O(n)
# Space Complexity : O(n)
#Faster
from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}  # for the subarray with sum = 0
        prefix = 0
        total = 0
        for num in nums:
            prefix = (prefix + num) % k
            if prefix < 0:  # handle negative numbers
                prefix += k
            total += count.get(prefix, 0)
            count[prefix] = count.get(prefix, 0) + 1
        return total
    
#slower
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        cumulative_sum=0
        mod_freq={0:1}

        for num in nums:
            cumulative_sum+=num
            rem = cumulative_sum%k
            if rem<0:
                rem+=k

            if rem in mod_freq:
                count+=mod_freq[rem]
                mod_freq[rem]+=1
            else:
                mod_freq[rem]=1
        return count