#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#
'''
Accepted
92/92 cases passed (590 ms)
Your runtime beats 47.49 % of python3 submissions
Your memory usage beats 69.14 % of python3 submissions (15.1 MB)
'''
# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maxProduct = 0
        nums.sort()
        maxProduct = max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
        return maxProduct
# @lc code=end

