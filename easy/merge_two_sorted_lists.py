"""Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        node = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                node.next = l2
                node = node.next
                l2 = l2.next
            elif l2 is None:
                node.next = l1
                node = node.next
                l1 = l1.next
            elif l1.val < l2.val:
                node.next = l1
                node = node.next
                l1 = l1.next
            else:
                node.next = l2
                node = node.next
                l2 = l2.next
            
        return head