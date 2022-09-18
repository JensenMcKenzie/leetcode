#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
Accepted
22/22 cases passed (61 ms)
Your runtime beats 88.96 % of python3 submissions
Your memory usage beats 66.72 % of python3 submissions (17.6 MB)
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast, slow = head.next, head
        while fast != slow or not fast or not slow:
            for i in range(2):
                if fast:
                    fast = fast.next
                else:
                    return False
            if slow:
                slow = slow.next
            else:
                return False
        return fast == slow
        
# @lc code=end

