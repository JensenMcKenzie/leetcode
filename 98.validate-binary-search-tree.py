#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursiveSearch(left, last, root, oldroot):
            if not root:
                return True
            print(root.val, oldroot)
            if (left and last < root.val) or (not left and last > root.val) or last == root.val or (left and root.val >= oldroot) or (not left and root.val <= oldroot):
                return False
            else:
                return recursiveSearch(True, root.val, root.left, oldroot) and recursiveSearch(False, root.val, root.right, oldroot)
        return recursiveSearch(True, root.val, root.left, root.val) and recursiveSearch(False, root.val, root.right, root.val)
# @lc code=end

