'''
654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        if self.left != None:
            self.left.printTree()

        print(self.val)

        if self.right != None:
            self.right.printTree()

class Solution:

    # Recursive solution in O(n)
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        if len(nums) <= 0:
            return None

        i = v = -1
        for c, n in enumerate(nums):
            if n > v:
                v = n
                i = c

        node = TreeNode(v)
        node.left = self.constructMaximumBinaryTree(nums[0:i])
        node.right = self.constructMaximumBinaryTree(nums[i+1:])
        return node

s = Solution()
node = s.constructMaximumBinaryTree([3,2,1,6,0,5])
node.printTree()