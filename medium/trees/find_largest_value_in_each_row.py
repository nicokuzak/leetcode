"""Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        d = {}
        stack = [[root, 0]]
        while stack != []:
            cur, lvl = stack.pop()
            if lvl in d.keys():
                d[lvl] = max(d[lvl], cur.val)
            else:
                d[lvl] = cur.val
            if cur.left:
                stack.append([cur.left, lvl+1])
            if cur.right:
                stack.append([cur.right, lvl+1])
        return [v for k,v in d.items()]