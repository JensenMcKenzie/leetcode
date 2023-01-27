#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
"""
Accepted
485/485 cases passed (38 ms)
Your runtime beats 96.04 % of python3 submissions
Your memory usage beats 89.04 % of python3 submissions (14.5 MB)
"""
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s)- 1
        while start < end:
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and start < end:
                end -= 1
            if s[start] != s[end]:
                return False
            start +=1
            end -=1
        return True
# @lc code=end

