"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100"""
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        vals = []
        level = -1
        def get_children(root, vals, level):
            level += 1
            if len(vals) == level:
                vals.append(root.val)
            if root.right:
                vals = get_children(root.right, vals, level)
            if root.left:
                vals = get_children(root.left, vals, level)
            return vals
        return get_children(root, vals, level)

# Beats 99% :))))