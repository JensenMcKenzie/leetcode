#
# @lc app=leetcode id=2119 lang=python3
#
# [2119] A Number After a Double Reversal
#
"""
Accepted
129/129 cases passed (49 ms)
Your runtime beats 52.55 % of python3 submissions
Your memory usage beats 95.64 % of python3 submissions (13.7 MB)
"""
# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num % 10 or num == 0
# @lc code=end

