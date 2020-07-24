'''
100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.recursiveIsSameTree(p, q)

    def recursiveIsSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # Checking for null equalities
        if (p == None and q == None):
            return True

        elif (p == None or q == None):
            print("One is none but the other isnt!")
            return False

        # Checking for value equalities
        elif (p.val != q.val):
            return False

        else:
            return self.recursiveIsSameTree(p.left, q.left) and self.recursiveIsSameTree(p.right, q.right)

    # Tiny boy
    def tinyIsSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Recursive
        center = (p == None and q == None) or (p != None and q != None and p.val == q.val)
        left = (self.isSameTree(p.left, q.left) if p != None and q != None else p == None and q == None)
        right = (self.isSameTree(p.right, q.right) if p != None and q != None else p == None and q == None)
        return center and left and right

t1 = TreeNode(val=0)
s = Solution()