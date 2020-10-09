'''
1080. Insufficient Nodes in Root to Leaf Paths

Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)

A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

 

Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1

Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22

Output: [5,4,8,11,null,17,4,7,null,null,null,5]
 

Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1

Output: [1,null,-3,4]

'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:  
        if root == None:
            return None
        
        canRootLeft = self.validSubtree(root.left, limit, root.val)
        canRootRight = self.validSubtree(root.right, limit, root.val)
        
        root.left = (root.left if canRootLeft else None)
        root.right = (root.right if canRootRight else None)
        
        if not canRootLeft and not canRootRight:
            return None
        else:
            return root
        
    def validSubtree(self, node: TreeNode, limit: int, currentVal: int) -> bool:
        # Handling base-case leafs
        if node == None:
            return (currentVal >= limit)
        
        canLeft = self.validSubtree(node.left, limit, node.val + currentVal)
        canRight = self.validSubtree(node.right, limit, node.val + currentVal)
        
        # Handling single-branch values
        if (node.left and not node.right):
            # Using our node left value
            canRight = canLeft
        elif (node.right and not node.left):
            canLeft = canRight
        
        node.left = (node.left if canLeft else None)
        node.right = (node.right if canRight else None)
        
        if not canLeft and not canRight:
            return False
        else:
            return canLeft or canRight