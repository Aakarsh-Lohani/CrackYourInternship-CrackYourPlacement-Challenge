# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 121. Best Time to Buy and Sell Stock

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        costprice=prices[0]
        profit=0
        for price in prices:
            if price<costprice:
                costprice=price
            elif price>costprice and price-costprice>profit:
                profit= price-costprice
        return profit