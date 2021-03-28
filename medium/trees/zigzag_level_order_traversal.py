"""Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100"""

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        if not root.left and not root.right:
            return [[root.val]]
        self.d = {}
        def zigzag(root, level):
            if not root:
                return
            if level not in self.d.keys():
                self.d[level] = [root.val]
            else:
                if level % 2 == 0:
                    self.d[level].append(root.val)
                else:
                    self.d[level] = [root.val] + self.d[level]
            zigzag(root.left, level+1)
            zigzag(root.right, level+1)
        zigzag(root, 0)
        return [v for k,v in self.d.items()]
        