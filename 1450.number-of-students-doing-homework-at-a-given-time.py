#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#
'''
Accepted
111/111 cases passed (28 ms)
Your runtime beats 99.35 % of python3 submissions
Your memory usage beats 61.58 % of python3 submissions (13.8 MB)
'''
# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        if len(startTime) == 0:
            return 0
        startTime[0] = 1 if startTime[0] <= queryTime and endTime[0] >= queryTime else 0
        for i in range(1, len(endTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                startTime[0] += 1
        return startTime[0]
# @lc code=end

