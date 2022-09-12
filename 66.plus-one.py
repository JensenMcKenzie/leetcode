#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
"""
Accepted
111/111 cases passed (43 ms)
Your runtime beats 73.08 % of python3 submissions
Your memory usage beats 58.73 % of python3 submissions (13.8 MB)
"""
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in reversed(range(0, len(digits))):
            if digits[i] < 10:
                return digits
            if digits[i] == 10:
                digits[i] = 0
            if i-1 < 0:
                digits.insert(0, 1)
                return digits
            digits[i-1] += 1
# @lc code=end

