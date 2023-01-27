#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

'''
Accepted
30/30 cases passed (41 ms)
Your runtime beats 42.05 % of python3 submissions
Your memory usage beats 61.7 % of python3 submissions (13.8 MB)
'''

# @lc code=start
import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = [[] for i in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                r[i].append(int(math.factorial(i)/(math.factorial(j) * math.factorial(i-j))))
        return r
# @lc code=end

