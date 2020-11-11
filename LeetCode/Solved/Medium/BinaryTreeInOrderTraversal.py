'''
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        # Non-recursive approach
        o = list()
        
        toIterate = list()
        toIterate.append(root)
        v = set()
        
        while len(toIterate) > 0:
            c = toIterate[len(toIterate) - 1]
            if c.left and c.left not in v:
                toIterate.append(c.left)
                v.add(c.left)
                continue
            o.append(c.val)
            toIterate.pop(len(toIterate) - 1)
            v.add(c)
            if (c.right and c.right not in v):
                toIterate.append(c.right)
                v.add(c.right)
            
        return o