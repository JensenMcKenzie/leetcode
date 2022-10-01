#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
"""
Accepted
15/15 cases passed (144 ms)
Your runtime beats 65.8 % of python3 submissions
Your memory usage beats 66.21 % of python3 submissions (17.6 MB)
"""
# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [nums[0]]
        for i in range(1, len(nums)):
            self.arr.append(self.arr[i-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.arr[right] - self.arr[left-1]
        return self.arr[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end