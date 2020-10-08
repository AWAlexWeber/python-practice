'''
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

from queue import *
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        o, q = [], Queue()
        
        # Inserting the (depth, node)
        q.put((0, root))
        
        while not q.empty():
            (depth, n) = q.get()
            if len(o) <= depth:
                o.append(list())
                
            o[depth].append(n.val)
            
            # Going left, going right
            if n.left:
                q.put((depth + 1, n.left))
            if n.right:
                q.put((depth + 1, n.right))
            
        return o
            