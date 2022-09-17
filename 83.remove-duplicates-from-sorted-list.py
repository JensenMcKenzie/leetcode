#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
"""
Accepted
166/166 cases passed (45 ms)
Your runtime beats 91.84 % of python3 submissions
Your memory usage beats 30.06 % of python3 submissions (13.9 MB)
"""
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        old = head
        while head and head.next:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return old
# @lc code=end

