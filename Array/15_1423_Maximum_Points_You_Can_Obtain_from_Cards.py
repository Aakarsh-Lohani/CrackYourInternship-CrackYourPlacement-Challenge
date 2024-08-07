# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
# 1423. Maximum Points You Can Obtain from Cards

# Time Complexity : O(n)
# Space Complexity : O(1)
from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)
        minSubArraySum = sum(cardPoints[:n-k])
        currSubArraySum = minSubArraySum

        for i in range(n-k, n):
            currSubArraySum = currSubArraySum - cardPoints[i-n+k] + cardPoints[i]
            minSubArraySum = min(minSubArraySum, currSubArraySum)

        return total - minSubArraySum