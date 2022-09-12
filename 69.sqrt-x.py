#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
"""
Accepted
1017/1017 cases passed (42 ms)
Your runtime beats 88.41 % of python3 submissions
Your memory usage beats 56.85 % of python3 submissions (13.8 MB)
"""
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

