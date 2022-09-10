#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Bind k to the length of the string, in case it is greater
        #Insert the back element at the front k times to get updated array
        for i in range(k%len(nums)):
            nums.insert(0, nums.pop())

# @lc code=end

