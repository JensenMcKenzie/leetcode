#
# @lc app=leetcode id=2124 lang=python3
#
# [2124] Check if All A's Appears Before All B's
#
"""
Accepted
216/216 cases passed (33 ms)
Your runtime beats 90.71 % of python3 submissions
Your memory usage beats 53.08 % of python3 submissions (13.9 MB)
"""
# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        """
        b = False
        for c in s:
            if not b and c == 'b':
                b = True
            if b and c == "a":
                return False
        return True
        """
        return 'ba' not in s
# @lc code=end

