#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
'''
Accepted
38/38 cases passed (51 ms)
Your runtime beats 75.14 % of python3 submissions
Your memory usage beats 33.46 % of python3 submissions (14.5 MB)
'''
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstChars = {}
        for c in s:
            if c in firstChars:
                firstChars[c] += 1
            else:
                firstChars[c] = 1
        for c in t:
            if c in firstChars:
                if firstChars[c] -1 == 0:
                    firstChars.pop(c)
                else:
                    firstChars[c] -= 1
            else:
                return False
        return len(firstChars) == 0
# @lc code=end

