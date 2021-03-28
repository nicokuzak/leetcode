"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = prev = cur = head
        if not head:
            return head
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                while cur.next is not None and cur.val == cur.next.val:
                    cur.next = cur.next.next
                prev.next = cur.next
                if cur == start:
                    start = prev.next
            else:
                prev = cur
            cur = cur.next
        return start