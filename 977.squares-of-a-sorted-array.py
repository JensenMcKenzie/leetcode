#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
"""
Accepted
137/137 cases passed (239 ms)
Your runtime beats 89.93 % of python3 submissions
Your memory usage beats 92.67 % of python3 submissions (15.8 MB)
"""
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left, right = 0, len(nums)-1
        while left <= right:
            l, r = abs(nums[left]), abs(nums[right])
            if l >= r:
                result.insert(0, l*l)
                left += 1
            elif r > l:
                result.insert(0, r*r)
                right -= 1
        return result

# @lc code=end

