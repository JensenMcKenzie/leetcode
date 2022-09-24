#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#
"""
Accepted
261/261 cases passed (29 ms)
Your runtime beats 95.04 % of python3 submissions
Your memory usage beats 96.83 % of python3 submissions (13.7 MB)
"""
# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        #Stores the max distance between 2 remainders of 1, and the last occurrence of a remainder of 1
        distance, last = 0, -1
        #Loop while n > 0
        while n > 0:
            #If the current digit/2 has a remainder of 1
            if n % 2 != 0:
                #If there has already been a remainder of 1 previously
                if last != -1:
                    #Set distance to the max of distance, or the current distance between the most recent remainders of 1
                    distance = max(distance, last)
                #Reset last
                last = 0
            #Increment last if there has already been a remainder of 1
            if last != -1:
                last += 1
            #Set n = n//2
            n//=2
        #Return the max distance
        return distance
# @lc code=end

