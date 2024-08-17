# https://leetcode.com/problems/simplify-path/description/
# 71. Simplify Path

# Time Complexity : O(n)
# Space Complexity : O(n)
from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        """
        # first remove double slashes so that we have single delimiter to split directories
        path = path.replace('//', '/')
        path_stack = deque()
        for sub_path in path.split('/'):
            if sub_path:
                path_stack.append(sub_path)
        new_path_stack = deque()
        up_dir = 0
        while path_stack:
            sub_path = path_stack.pop()
            if sub_path == '..':
                up_dir += 1
                continue
            if sub_path != '.' and sub_path != '..' and up_dir == 0:
                new_path_stack.appendleft(sub_path)
            elif up_dir != 0 and sub_path != '.':
                up_dir -= 1
        new_path = '/'.join(new_path_stack)
        return f"/{new_path}"

            
