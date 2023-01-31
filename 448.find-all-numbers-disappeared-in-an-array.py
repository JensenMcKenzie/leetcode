#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
'''
Accepted
33/33 cases passed (344 ms)
Your runtime beats 87.71 % of python3 submissions
Your memory usage beats 46.65 % of python3 submissions (24.3 MB)
'''
# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsList = {i for i in range(1, len(nums)+1)}
        for n in nums:
            if n in numsList:
                numsList.remove(n)
        return list(numsList)
        
# @lc code=end

