# https://leetcode.com/problems/subarray-sum-equals-k/description/
# 560. Subarray Sum Equals K

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        cumulative_sum=0  #prefix sum
        sum_freq={0:1} # to handle the case when cumulative_sum-k=0
        for num in nums:
            cumulative_sum+=num

            # if_existing_cumulative_sum + k = current_cumulative_sum
            # Hence current_cumulative_sum-k is the needed cumulative_sum(array)
            if (cumulative_sum-k) in sum_freq:
                count+=sum_freq[cumulative_sum-k]
            if cumulative_sum in sum_freq:
                sum_freq[cumulative_sum]+=1
            else:
                sum_freq[cumulative_sum]=1
        return count

# Checking for Subarrays:

# For each element in the array, you calculate the cumulative sum up to that element.
# To determine if there exists a subarray that sums to k ending at the current element, you check if (cumulative_sum - k) exists in the hashmap.
# If (cumulative_sum - k) exists in the hashmap, it means there is a previous cumulative sum that, when subtracted from the current cumulative sum, equals k. This indicates that the subarray between the previous cumulative sum and the current cumulative sum sums to k.