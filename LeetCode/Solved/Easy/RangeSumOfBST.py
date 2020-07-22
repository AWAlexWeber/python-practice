'''
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
'''

# NOTE THAT THIS MEANS THE ACTUAL NUMERIC INBETWEEN, NOT VISUALLY (IE VALUE OF LEFT NOT POSITIONAL VALUE)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.searchBST(root, L, R)
    
    def searchBST(self, node: TreeNode, L: int, R: int) -> int:
        o = (node.val if node.val >= L and node.val <= R else 0)
        if node.left != None:
            o += self.searchBST(node.left, L, R)
        if node.right != None:
            o += self.searchBST(node.right, L, R)
        return o
        