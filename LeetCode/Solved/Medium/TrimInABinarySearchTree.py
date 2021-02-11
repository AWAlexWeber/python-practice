'''
669. Trim a Binary Search Tree

Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

 

Example 1:


Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
Example 2:


Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
Example 3:

Input: root = [1], low = 1, high = 2
Output: [1]
Example 4:

Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]
Example 5:

Input: root = [1,null,2], low = 2, high = 4
Output: [2]
 

Constraints:

The number of nodes in the tree in the range [1, 104].
0 <= Node.val <= 104
The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree.
0 <= low <= high <= 104
'''

# Summary; remember how binary search trees work! Everything to the left is SMALLER than the current node. same for the right!

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # Handling base case.
        if root == None:
            return root
        
        # Trimming left/right roots O(n).
        # Ensuring our starting node is within the bounds. We are able to ignore anything to the left
        # if it violates our boundary since anything further to the left must also violate. Same for the right.
        # This same logic is used when we perform the recurse
        while root and (root.val < low or root.val > high):
            if root.val < low:
                # We must go right.
                root = root.right
            if root.val > high:
                # We must go left.
                root = root.left
        
        # Recursively cleaning up the rest of the tree O(n)
        self.recurseBST(root, low, high, root)
        
        # Returning our final 'root'.
        return root
        
    def recurseBST(self, node: TreeNode, low: int, high: int, topAncestor: TreeNode=None):
        # Handling base case.
        if node == None:
            return
        
        if node.val < low or node.val > high:
            # Trimming this node;.
            if node.val < low:
                # Can we go right? If so, go right. Otherwise, set top ancestors left value to null
                if node.right:
                    self.recurseBST(node.right, low, high, topAncestor)
                else:
                    topAncestor.left = None
            elif node.val > high:
                if node.left:
                    self.recurseBST(node.left, low, high, topAncestor)
                else:
                    topAncestor.right = None
                
        # Valid node; we will simply recurse left and right, passing in this node as the new top ancestor.
        else:
            # Before we go any deeper, we are going to ensure that we're linked properly to the top ancestor
            # If our previous node was valid, this will do essentially nothing. But will link when we pass prune.
            if node != topAncestor:
                if node.val < topAncestor.val:
                    topAncestor.left = node
                else:
                    topAncestor.right = node
                
            # Going left/right
            self.recurseBST(node.left, low, high, node)
            self.recurseBST(node.right, low, high, node)
        