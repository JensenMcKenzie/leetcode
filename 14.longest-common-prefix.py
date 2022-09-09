#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        common = strs[0]
        for i in range(1, len(strs)):
            for j, c in enumerate(common):
                if j >= len(strs[i]):
                    common = common[:j]
                    break
                if c != strs[i][j]:
                    common = common[:j]
                    break
        return common
                    
# @lc code=end

