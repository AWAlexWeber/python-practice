'''
1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.deepSum = 0
        self.maxDepth = 0
        
        self.search(root, 0)
        return self.deepSum
        
    # Recursive tree transversal, keeping track of our depth
    def search(self, node: TreeNode, depth: int):
        if node == None:
            return
        
        if self.maxDepth < depth:
            self.maxDepth = depth
            self.deepSum = node.val
            
        elif self.maxDepth == depth:
            self.deepSum += node.val
            
        # Going left and right
        self.search(node.left, depth + 1)
        self.search(node.right, depth + 1)