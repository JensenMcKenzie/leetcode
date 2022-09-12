#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

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

