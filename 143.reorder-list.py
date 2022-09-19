#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        old = head
        last = head
        while head:
            if not head.next:
                last = head
            head = head.next
        temp = old
        old.next = last
        old.next.next = temp.next
        final = old
        while old
# @lc code=end

