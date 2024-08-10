# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# 122. Best Time to Buy and Sell Stock II

# Time Complexity : O(n)
# Space Complexity : O(1)

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        share=False
        buy=0
        profit=0
        l=len(prices)
        for i in range(l-1):
            if prices[i+1]>prices[i]:
                if share==False:
                    buy=i
                    share=True
            elif prices[i+1]<prices[i]:
                if share==True:
                    profit+=prices[i]-prices[buy]
                    share=False
        if share==True:
            share=False
            profit+=prices[l-1]-prices[buy]
        return profit