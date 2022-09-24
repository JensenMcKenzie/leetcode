#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
"""
Accepted
53/53 cases passed (281 ms)
Your runtime beats 71.04 % of python3 submissions
Your memory usage beats 66.58 % of python3 submissions (15.4 MB)
"""
# @lc code=start
class Solution:
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        i, j = 0, len(arr)-1
        while i + 1 < len(arr) and arr[i] < arr[i+1]: i+=1
        while j > 0 and arr[j] < arr[j-1]: j-=1
        return 0 < i == j < len(arr) - 1
# @lc code=end

