"""Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        if head is None:
            return None
        cur = head
        track = []
        while cur.next is not None:
            track.append(cur)
            cur = cur.next
        cur.next = head
        track.append(cur)
        k = k % len(track)
        track[len(track)-k-1].next = None
        if k == 0:
            return head
        return track[len(track)-k]