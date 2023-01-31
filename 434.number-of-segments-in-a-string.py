#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#
'''
Accepted
28/28 cases passed (23 ms)
Your runtime beats 97.63 % of python3 submissions
Your memory usage beats 44.1 % of python3 submissions (13.8 MB)
'''
# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        index = 0
        count = 0
        while index < len(s):
            if s[index] != " " and (index == 0 or s[index-1] == " "):
                count += 1
            index += 1
        return count
# @lc code=end

