#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
'''
Accepted
34/34 cases passed (48 ms)
Your runtime beats 31.01 % of python3 submissions
Your memory usage beats 56.66 % of python3 submissions (13.9 MB)
'''
# @lc code=start
import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1]
        for i in range(1,rowIndex+1):
            r.insert(len(r),int(math.factorial(rowIndex)/(math.factorial(i) * math.factorial(rowIndex-i))))
        return r
# @lc code=end

