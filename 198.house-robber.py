#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        last, current = 0, 0
        for n in nums:
            last, current = last, max(current + n, last + n)
        return current

# @lc code=end

