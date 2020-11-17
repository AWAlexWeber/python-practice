'''
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import queue

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # BFS using maximum at each level
        q = queue.Queue()
        q.put((root,0))
        
        currentDepth, maximalLayer, currentSum, maximalLayerSum = 0, 0, 0, float("-inf")
        
        while not q.empty():
            (n, d) = q.get()
            
            if d != currentDepth:
                currentDepth += 1
                if currentSum > maximalLayerSum:
                    maximalLayer = d
                    maximalLayerSum = currentSum
                currentSum = 0
                
            currentSum += n.val
        
            if n.left:
                q.put((n.left, d + 1))
            if n.right:
                q.put((n.right, d + 1))
                
        if currentSum > maximalLayerSum:
                maximalLayer = d + 1
                maximalLayerSum = currentSum
                
        return maximalLayer