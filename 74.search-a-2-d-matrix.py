#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix)-1
        while l < h:
            m = (h-l)//2
            if matrix[m][0] < target:
                l = m + 1
            if matrix[m][0] > target:
                h = m - 1
            if matrix[m][0] == target:
                return True
        print(l)
        p = l
        l = 0
        h = len(matrix)-1
        m = 0
        while l < h:
            m = (h-l)//2
            if matrix[p][m] < target:
                l = m + 1
            elif matrix[p][m] > target:
                h = m - 1
            else:
                return True
        return matrix[p][m] == target

        
# @lc code=end

