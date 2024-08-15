# https://leetcode.com/problems/basic-calculator-ii/description/
# 227. Basic Calculator II

# Time Complexity : O(n)
# Space Complexity : O(n)
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        # Initialize the stack, current number, and opr
        stack = []
        curr = 0
        opr = '+'
        
        for i, c in enumerate(s):
            if c.isdigit():
                curr = curr * 10 + int(c)
            
            if c in "+-*/" or i == len(s) - 1:
                if opr == '+':
                    stack.append(curr)
                elif opr == '-':
                    stack.append(-curr)
                elif opr == '*':
                    stack[-1] = stack[-1] * curr
                elif opr == '/':
                    
                    stack[-1] = int(stack[-1] / curr)
                
                
                curr = 0
                opr = c
        
        return sum(stack)
