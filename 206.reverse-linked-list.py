#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
"""
Accepted
28/28 cases passed (35 ms)
Your runtime beats 96.25 % of python3 submissions
Your memory usage beats 28.06 % of python3 submissions (15.5 MB)
"""
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head:
            next = head.next
            head.next = previous
            previous = head
            head = next
        return previous
# @lc code=end

