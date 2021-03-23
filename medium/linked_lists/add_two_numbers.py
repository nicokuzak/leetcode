
""" You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        base = ListNode()
        head = base
        mod = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                head.next = ListNode(l2.val)
                head = head.next
                head.val, mod = add_nodes(head, None, mod)
                l2 = l2.next
            elif l2 is None:
                head.next = ListNode(l1.val)
                head = head.next
                head.val, mod = add_nodes(head, None, mod)
                l1 = l1.next
            else:
                head.next = ListNode(l1.val)
                head = head.next
                head.val, mod = add_nodes(head, l2, mod)
                l1 = l1.next
                l2 = l2.next
        if mod == 1:
            head.next = ListNode(1)  
        return base.next

def add_nodes(h, t, mod):
    h.val += mod
    if t is None:
        if h.val >= 10:
            h.val -= 10
            return h.val, 1
        return h.val, 0
    h.val += t.val
    if h.val >= 10:
        h.val -= 10
        return h.val, 1
    return h.val, 0