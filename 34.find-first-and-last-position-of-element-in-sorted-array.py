#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
"""
Accepted
88/88 cases passed (124 ms)
Your runtime beats 63.33 % of python3 submissions
Your memory usage beats 92.16 % of python3 submissions (15.4 MB)
"""
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums)-1
        result = [-1, -1]
        while start <= end:
            middle = (start + end)//2
            if nums[middle] == target:
                result = [middle, middle]
                if middle-1 >= 0:
                    while middle-1 >= 0 and nums[middle-1] == target:
                        result[0] -= 1
                        middle -=1
                middle = (start + end)//2
                if middle+1 < len(nums):
                    while middle+1 < len(nums) and nums[middle+1] == target:
                        result[1] += 1
                        middle += 1
                return result
            elif nums[middle] < target:
                start = middle+1
            elif nums[middle] > target:
                end = middle-1
        return result
# @lc code=end

