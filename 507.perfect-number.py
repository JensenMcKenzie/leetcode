#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#
"""
Accepted
98/98 cases passed (45 ms)
Your runtime beats 84.44 % of python3 submissions
Your memory usage beats 9.59 % of python3 submissions (13.9 MB)
"""
# @lc code=start
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        for i in range(2,int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum += i + int(num/i)
        return sum == num and num != 1
# @lc code=end

