# https://leetcode.com/problems/non-overlapping-intervals/description/
# 435. Non-overlapping Intervals

# Time Complexity : O(NlogN)
# Space Complexity: (O(1))

from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        end, count = intervals[0][1], 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count