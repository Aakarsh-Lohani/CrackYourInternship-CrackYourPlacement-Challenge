# https://leetcode.com/problems/top-k-frequent-elements/description/
# 347. Top K Frequent Elements

# Faster
# Bucket sort
from typing import List
from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        count = Counter(nums)
        
        # Step 2: Create buckets where index represents frequency
        max_freq = max(count.values())
        buckets = [[] for _ in range(max_freq + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # Step 3: Collect the top k frequent elements
        result = []
        for freq in range(max_freq, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

# Example usage
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]

# slower
from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        count = Counter(nums)
        
        # Step 2: Use a heap to keep track of the top k elements
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Extract the elements from the heap
        return [num for freq, num in heap]