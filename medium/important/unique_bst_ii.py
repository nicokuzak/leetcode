"""Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        return self.bst(1, n)
    
    
    def bst(self, start, end):
        if start > end:
            return [None]
        trees = []
        for val in range(start, end+1):

            left = self.bst(start, val-1)
            right = self.bst(val+1, end)
            for l in left:
                for r in right:
                    root = TreeNode(val)
                    root.left = l
                    root.right = r
                    trees.append(root)
        return trees