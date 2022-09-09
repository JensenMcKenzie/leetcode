#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
from curses.ascii import isdigit


class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        n = False
        i = 0
        s = s.lstrip()
        if s == "":
            return 0
        if (s[0] == "+" or s[i] == '-') and 1 < len(s):
                if not isdigit(s[1]):
                    return 0
        if s[0] == '-':
            n = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        while i < len(s) and isdigit(s[i]):
            result = result * 10 + int(s[i])
            i+=1
        if result >= pow(2, 31) and n:
            return pow(-2, 31)
        elif result > pow(2, 31) -1:
            return pow(2, 31) -1
        if n:
            return result * -1
        return result
# @lc code=end

