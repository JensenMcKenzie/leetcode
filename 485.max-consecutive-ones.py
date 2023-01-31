#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
'''
Accepted
42/42 cases passed (369 ms)
Your runtime beats 59.76 % of python3 submissions
Your memory usage beats 94.78 % of python3 submissions (14.2 MB)
'''
# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        index = 0
        while index < len(nums):
            running = 0
            while index < len(nums) and nums[index] == 1:
                running += 1
                index += 1
            m = max(running, m)
            index += 1
        return m
# @lc code=end

