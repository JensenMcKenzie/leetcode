#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        for i, c in enumerate(p):
            if c != s[i] and c != '.':
        
# @lc code=end

