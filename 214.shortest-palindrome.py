#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        p = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[j] != s[i]:
                j = p[j-1]
            if s[j] == s[i]:
                j += 1
            p[i] = j
        return p
# @lc code=end