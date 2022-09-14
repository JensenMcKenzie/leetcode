#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
"""
Accepted
92/92 cases passed (34 ms)
Your runtime beats 90.01 % of python3 submissions
Your memory usage beats 72.22 % of python3 submissions (13.8 MB)
"""
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['[','{', '(']:
                stack.append(c)
            elif c == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif c == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            elif c == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
        return len(stack) == 0
# @lc code=end

