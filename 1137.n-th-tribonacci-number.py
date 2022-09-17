#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
"""
Accepted
39/39 cases passed (54 ms)
Your runtime beats 32.24 % of python3 submissions
Your memory usage beats 97.05 % of python3 submissions (13.8 MB)
"""
# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        last = [0, 1, 1]
        if n <= 2:
            return last[n]
        for i in range(3, n+1):
            last.append(sum(last))
            last.pop(0)
        return last[-1]
# @lc code=end

