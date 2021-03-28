"""Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= k <= 50"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        cur = head
        
        while cur and cur.val == val:
            cur = cur.next
        start = cur
        if not cur:
            return cur
        while cur.next:
            if cur.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
                if not cur.next:
                    break
            cur = cur.next
        return start