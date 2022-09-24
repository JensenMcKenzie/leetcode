#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sum = (nums*(nums+1))/2
        for i in nums:
            sum -= i
        
# @lc code=end

