#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle -1
        return left
# @lc code=end

