# https://leetcode.com/problems/gas-station/description/
# 134. Gas Station

# Time Complexity: O(N)
# Space Complexity: O(1)
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = total_cost = curr_gas = curr_cost = start_station = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            curr_gas += gas[i]
            curr_cost += cost[i]
            if curr_gas < curr_cost:
                start_station = i + 1
                curr_gas = curr_cost = 0
        return start_station if total_gas >= total_cost else -1