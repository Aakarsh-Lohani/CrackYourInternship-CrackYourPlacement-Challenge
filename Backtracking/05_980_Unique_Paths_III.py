# https://leetcode.com/problems/unique-paths-iii/description/
# 980. Unique Paths III

# Time Complexity : O(4(N∗M))
# Space Complexity : O(N∗M)
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        start_x = start_y = end_x = end_y = 0
        empty_squares = 0
        
        # Find start, end positions and count empty squares
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_x, start_y = r, c
                elif grid[r][c] == 2:
                    end_x, end_y = r, c
                if grid[r][c] != -1:
                    empty_squares += 1
        
        def dfs(x, y, count):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == -1:
                return 0
            if x == end_x and y == end_y:
                return 1 if count == empty_squares else 0
            
            # Mark the square as visited
            grid[x][y] = -1
            paths = dfs(x + 1, y, count + 1) + dfs(x - 1, y, count + 1) + dfs(x, y + 1, count + 1) + dfs(x, y - 1, count + 1)
            # Unmark the square (backtrack)
            grid[x][y] = 0
            
            return paths
        
        return dfs(start_x, start_y, 1)