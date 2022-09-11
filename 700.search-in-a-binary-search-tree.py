#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from re import search


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Recursion
        #if root is None or root.val == val:
        #    return root
        #return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)
        
        #Iterative approach, faster runtime
        while root != None:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else:
                return root
        return None
# @lc code=end

