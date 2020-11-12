'''
545. Boundary of Binary Tree

Given the root of a binary tree, return the values of its boundary in an anti-clockwise direction starting from the root.

The Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

The left boundary is defined as the path from the root to the left-most node.

The right boundary is defined as the path from the root to the right-most node.

If the root doesn't have a left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree and does not apply to any subtrees.

The left-most node is defined as a leaf node you could reach when you always first travel to the left subtree if it exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined in the same way with left and right exchanged.

 

Example 1:


Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are nodes 3 and 4.
The right boundary is nodes 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Example 2:


Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary is nodes 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # Base case
        if root == None:
            return []
        
        self.result = [root.val]
        
        if root.left:
            self.bounds(root.left, self.result)
        if root.left or root.right:
            self.leafs(root)
        if root.right:
            self.bounds(root.right, [], dir=False)
        
        return self.result
        
    # Helper function
    def bounds(self, node: TreeNode, data: List[int], dir=True):
            # Attempting to get values
            while node and (node.left or node.right):
                data.append(node.val)
                node = node.left or node.right if dir else node.right or node.left
            
            # Otherwise not right
            if not dir:
                while data:
                    self.result.append(data.pop())
        
    # Helper function
    def leafs(self, node: TreeNode):
        if node:
            self.leafs(node.left)
            self.leafs(node.right)
            if not node.left and not node.right:
                self.result.append(node.val)
            
        
# Secondary solution
class Solution2:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # Base case of empty root
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        # Getting left boundary
        moveLeft, self.o = root.left, list([root.val])
        while moveLeft:
            if not moveLeft.left and not moveLeft.right:
                break
            
            # Visting this node
            self.o.append(moveLeft.val)
            
            # Attempting to go left
            if moveLeft.left:
                moveLeft = moveLeft.left
            elif moveLeft.right:
                moveLeft = moveLeft.right
                
        self.recurseLeaves(root)
        
        # Getting right side boundary
        rightBoundary = list()
        moveRight = root.right
        while moveRight:
            if not moveRight.right and not moveRight.left:
                break
                
            rightBoundary.append(moveRight.val)
            if moveRight.right:
                moveRight = moveRight.right
            elif moveRight.left:
                moveRight = moveRight.left
                
        return self.o + rightBoundary[::-1]
                
    def recurseLeaves(self, node: TreeNode):
        if not node.left and not node.right:
            self.o.append(node.val)
            return
        else:
            if node.left:
                self.recurseLeaves(node.left)
            if node.right:
                self.recurseLeaves(node.right)
            return