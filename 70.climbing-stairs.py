#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
"""
Accepted
45/45 cases passed (27 ms)
Your runtime beats 97.59 % of python3 submissions
Your memory usage beats 56.97 % of python3 submissions (13.8 MB)
"""
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        last = [1,2]
        count = 1
        if n <= 0:
            return 0
        if n <= 2:
            return last[n-1]
        for i in range(2,n):
            #Perform pop first, for 0 index, then new 0 index is old 1 index
            #This accomplishes the same result slighty quicker by making use of the pop return value
            count = last.pop(0) + last[0]
            last.append(count)
        return count

# @lc code=end

