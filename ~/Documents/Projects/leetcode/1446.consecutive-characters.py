#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxCount = 0
        count = 1
        for i in range(1, len(s)):
            print(i)
            if s[i] != s[i-1]:
                maxCount = max(count, maxCount)
                count = 1
            else:
                count += 1
        return max(count, maxCount)
# @lc code=end