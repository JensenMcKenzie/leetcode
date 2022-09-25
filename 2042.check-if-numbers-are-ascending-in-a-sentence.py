#
# @lc app=leetcode id=2042 lang=python3
#
# [2042] Check if Numbers Are Ascending in a Sentence
#
"""
Accepted
98/98 cases passed (34 ms)
Your runtime beats 90.18 % of python3 submissions
Your memory usage beats 57.53 % of python3 submissions (13.9 MB)
"""
# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = None
        for i in s.split(" "):
            if i.isnumeric():
                if not last:
                    last = i
                elif int(last) >= int(i):
                    return False
                elif int(last) < int(i):
                    last = i
        return True
# @lc code=end

