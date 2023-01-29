#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
'''
Accepted
1101/1101 cases passed (36 ms)
Your runtime beats 67.1 % of python3 submissions
Your memory usage beats 94.59 % of python3 submissions (13.7 MB)
'''
# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0 : return 0
        if num % 9 == 0 : return 9
        else : return (num % 9)
# @lc code=end

