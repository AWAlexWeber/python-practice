'''

1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

'''

# This is just a tree search, not too sure why its presented in this way
# There is probably some neat trick we can use

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Naive binary search solution
        node = self.searchNode(cloned, target)
        return node
        
    def searchNode(self, node: TreeNode, target: TreeNode) -> TreeNode:
        # Checking if none
        if node == None:
            return None
        
        if node.val == target.val:
            return node
        
        nodeLeft = (self.searchNode(node.left, target) if node.left != None else None)
        nodeRight = (self.searchNode(node.right, target) if node.right != None else None)
        
        if nodeLeft != None and nodeLeft.val == target.val:
            return nodeLeft
        elif nodeRight != None and nodeRight.val == target.val:
            return nodeRight
        return None