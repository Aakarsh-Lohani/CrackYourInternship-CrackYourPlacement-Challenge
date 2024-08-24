# https://leetcode.com/problems/remove-k-digits/description/
# 402. Remove K Digits

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0 and stack:
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or '0'