# https://leetcode.com/problems/valid-parentheses/description/
# 20. Valid Parentheses

# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack_brackets=[]

        for b1 in s:
            if b1 in ["{","[","("]:
                stack_brackets.append(b1)
            elif b1 in ["}","]",")"]:
                if len(stack_brackets)>0:
                    b2=stack_brackets.pop()
                    pair=b2+b1
                    # print(pair)
                    if pair not in ["{}","[]","()"]:
                        return False
                else:
                    return False
        if len(stack_brackets)>0:
            return False
        return True