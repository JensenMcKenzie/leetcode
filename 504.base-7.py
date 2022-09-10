#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        out = ""
        n = False
        if num < 0:
            n = True
        num = abs(num)
        while num > 0:
            out += str(num%7)
            num //= 7
        out = out[::-1]
        return '-' + out if n else out
        
# @lc code=end

