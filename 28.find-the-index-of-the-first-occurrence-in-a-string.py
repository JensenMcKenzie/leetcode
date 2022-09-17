#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j = 1
                while j < len(needle):
                    if i+j >= len(haystack):
                        break
                    if haystack[i+j] != needle[j]:
                        break
                    j+=1
                if j == len(needle): return i
        return -1
                    
# @lc code=end

