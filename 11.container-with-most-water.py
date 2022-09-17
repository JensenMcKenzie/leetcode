#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
"""
Accepted
60/60 cases passed (839 ms)
Your runtime beats 83.19 % of python3 submissions
Your memory usage beats 78.34 % of python3 submissions (27.4 MB)
"""
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        area = 0
        while left < right:
            area = max(area, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
# @lc code=end

