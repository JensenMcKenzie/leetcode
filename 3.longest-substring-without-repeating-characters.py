#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        start = 0
        maxLen = 0
        for end in range(len(s)):
            if s[end] in lastSeen:
                start = max(start,lastSeen[s[end]] + 1)
            lastSeen[s[end]] = end
            maxLen = max(maxLen, end-start + 1)
        return maxLen
        
# @lc code=end

