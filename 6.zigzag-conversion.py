#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
from ntpath import join


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        arr = ["" for i in range(numRows)]
        d = 'd'
        row = 0
        for c in s:
            arr[row] += c
            if row == 0:
                d = 'd'
            elif row == numRows-1:
                d = 'u'
            if d == 'd':
                row += 1
            else:
                row -= 1
        return "".join(arr)
# @lc code=end

