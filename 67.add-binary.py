#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
'''
Accepted
294/294 cases passed (29 ms)
Your runtime beats 93.78 % of python3 submissions
Your memory usage beats 97.78 % of python3 submissions (13.8 MB)
'''

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
        
            
            
        
# @lc code=end

