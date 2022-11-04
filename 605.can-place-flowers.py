#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
'''
Accepted
124/124 cases passed (178 ms)
Your runtime beats 89.36 % of python3 submissions
Your memory usage beats 30.95 % of python3 submissions (14.5 MB)
'''
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False
# @lc code=end

