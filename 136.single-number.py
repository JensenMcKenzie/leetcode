#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
"""
Accepted
61/61 cases passed (137 ms)
Your runtime beats 95.54 % of python3 submissions
Your memory usage beats 83.61 % of python3 submissions (16.6 MB)
"""
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = 0
        for i in nums:
            number ^= i
        return number
# @lc code=end

