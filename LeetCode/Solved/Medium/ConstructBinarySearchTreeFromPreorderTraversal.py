'''
1008. Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.buildTree(0, len(preorder), preorder, TreeNode(preorder[0]))
    
    # i = start, f = end
    def buildTree(self, i: int, f: int, preorder: List[int], node: TreeNode) -> TreeNode:
        # Returning us if its just us
        if f - i == 0:
            return None
        elif f - i == 1:
            return node
        
        # Finding the middle point
        e = i + 1
        while e < f and preorder[e] < preorder[i]:
            e += 1
        
        # Building our left and right nodes
        node.left = (None if e - i + 1 <= 0 else self.buildTree(i + 1,e, preorder, TreeNode(preorder[i+1])))
        node.right = (None if f - e <= 0 else self.buildTree(e, f, preorder, TreeNode(preorder[e])))
        return node