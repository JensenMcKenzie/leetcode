#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, s: int) -> int:
        low, high = 0, s
        while low <= high:
            m = (low + high)//2
            if m * m> s:
                high = m-1
            elif m * m < s:
                low = m+1
            else:
                return m
        return high


# @lc code=end

