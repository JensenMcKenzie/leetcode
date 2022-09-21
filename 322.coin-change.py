#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        print(coins)
        count = 0
        while amount > 0 and len(coins) > 0:
            while amount - coins[-1] >= 0:
                amount -= coins[-1]
                count += 1
            coins.pop()
        print(count)
        return count if amount == 0 else -1
        
# @lc code=end

