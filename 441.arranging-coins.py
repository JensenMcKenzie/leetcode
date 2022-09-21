#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
"""
Accepted
1335/1335 cases passed (48 ms)
Your runtime beats 85.31 % of python3 submissions
Your memory usage beats 56.61 % of python3 submissions (13.9 MB)
"""
# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Binary search starts at ends of range
        left, right = 0, n+1
        while left <= right:
            # Middle of the current range
            middle = (left + right)//2
            # If n is less than the current sum of m numbers, decrease the rear pointer
            if (middle*(middle +1))/2 > n:
                right = middle -1
            # If n is greater than the current sum of m numbers, increase the left pointer
            elif (middle*(middle +1))/2 < n:
                left = middle + 1
            # If n is equal to the current sum of m numbers, return m
            else:
                return middle
        # If we have coins which do not exactly equal the sum of m numbers, return the left pointer minus 1
        return left-1

# @lc code=end

