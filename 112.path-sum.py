#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Accepted
117/117 cases passed (57 ms)
Your runtime beats 71.5 % of python3 submissions
Your memory usage beats 92.01 % of python3 submissions (15 MB)
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, target, results):
            if root:
                if root.left == None and root.right == None:
                    if target-root.val == 0:
                        results.append(True)
                if root.left != None:
                    traverse(root.left, target-root.val, results)
                if root.right != None:
                    traverse(root.right, target-root.val, results)
        results = []
        traverse(root, targetSum, results)
        return any(results)

            
# @lc code=end

