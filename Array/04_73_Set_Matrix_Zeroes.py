# https://leetcode.com/problems/set-matrix-zeroes/description/
# 73. Set Matrix Zeroes

# Time Complexity: O(m*n)
# Space Complexity: O(m+n)
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
    Do not return anything, modify matrix in-place instead.
    """


        rows_to_zero = set()
        cols_to_zero = set()

        # First pass to identify rows and columns to be zeroed
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows_to_zero.add(row)
                    cols_to_zero.add(col)

        # Second pass to set rows to zero
        for row in rows_to_zero:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0

        # Second pass to set columns to zero
        for col in cols_to_zero:
            for row in range(len(matrix)):
                matrix[row][col] = 0
        