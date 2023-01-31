#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
'''
Accepted
149/149 cases passed (33 ms)
Your runtime beats 67.55 % of python3 submissions
Your memory usage beats 93.7 % of python3 submissions (13.8 MB)
'''
# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        s = ""
        for i in range(len(num)):
            if num[i] == '0':
                s = s + "1"
            else:
                s = s + "0"
        return int(s, 2)

# @lc code=end

