#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        n = x < 0
        x = abs(x)
        while x > 0:
            first = x % 10
            result = result * 10 + first
            x //= 10
        if result > pow(2,31):
                return 0
        if n:
            result = -result
        return result
            
# @lc code=end

