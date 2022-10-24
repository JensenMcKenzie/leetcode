#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#
"""
Accepted
62/62 cases passed (36 ms)
Your runtime beats 84.36 % of python3 submissions
Your memory usage beats 94.19 % of python3 submissions (13.8 MB)
"""
# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
# @lc code=end

