# https://leetcode.com/problems/excel-sheet-column-title/description/
# 168. Excel Sheet Column Title

# Time Complexity : O(log n) = O(log(base26)n)
# Space Complexity : O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title=""
        while columnNumber>0:
            columnNumber -= 1  # Adjust for 0-based indexing
            rem = columnNumber % 26  # Find the remainder (0-25)
            title = chr(rem + 65) + title  # Convert remainder to corresponding ASCII character and prepend to the result
            columnNumber = columnNumber // 26  # Move to the next digit
        return title