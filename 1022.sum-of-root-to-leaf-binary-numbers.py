#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#
"""
Accepted
63/63 cases passed (67 ms)
Your runtime beats 38.66 % of python3 submissions
Your memory usage beats 84.44 % of python3 submissions (14.1 MB)
"""
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0
    def recursiveSum(self, root, sum):
        sum *= 2
        if root.val == 1:
            sum += 1
        if not root.left and not root.right:
            self.total += sum
            return
        if root.left:
            self.recursiveSum(root.left, sum)
        if root.right:
            self.recursiveSum(root.right, sum)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.recursiveSum(root, 0)
        return self.total
# @lc code=end

