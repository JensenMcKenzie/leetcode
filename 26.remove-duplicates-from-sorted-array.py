#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
"""
Accepted
361/361 cases passed (91 ms)
Your runtime beats 93.91 % of python3 submissions
Your memory usage beats 96.43 % of python3 submissions (15.5 MB)
"""
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count


# @lc code=end

