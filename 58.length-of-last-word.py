#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
"""
Accepted
58/58 cases passed (36 ms)
Your runtime beats 83.29 % of python3 submissions
Your memory usage beats 80.64 % of python3 submissions (13.8 MB)
"""

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "":
            return 0
        last = s.strip().split(" ")[-1]
        return len(last)
# @lc code=end

