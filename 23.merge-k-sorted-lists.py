#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def SortedMerge(a, b):
        result = ListNode()
        tail = result
        while True:
            if a == None:
                tail.next = b
                break
            if b == None:
                tail.next = a
                break

            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            
            tail = tail.next
        return result.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        finish = len(lists) -1
        
        while finish > 0:
            lists[0] = SortedMerge(lists[0], lists[finish])
            finish -= 1
        return lists[0]
# @lc code=end

