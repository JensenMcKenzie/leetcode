#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
"""
Accepted
16/16 cases passed (3047 ms)
Your runtime beats 5 % of python3 submissions
Your memory usage beats 60.41 % of python3 submissions (17.3 MB)
"""
class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        seen = []
        while head:
            print(head.val)
            if head in seen:
                return head
            seen.append(head)
            head = head.next
        return None

        
# @lc code=end

