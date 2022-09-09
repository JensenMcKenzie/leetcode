#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new = ListNode()
        returnList = new
        toAdd = []
        while head != None:
            for i in range(k):
                toAdd
                head = head.next
            new.next = head
            new = new.next
            
        return returnList.next
# @lc code=end

