'''
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        h = {}
        self.r(root, h, 0)
        return [h[a] for a in h]
        
    def r(self, node: TreeNode, h: dict, depth: int):
        if node == None:
            return 
        
        if depth not in h:
            h[depth] = node.val
            
        self.r(node.right, h, depth + 1)
        self.r(node.left, h, depth + 1)


class SolutionTwo:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # Going to DFS, keeping track of how far right we are and our depth
        # The node visible at later n is the node that is the furthest to the right that we've visisted.
        # Dictionary to track node value and node distance to the right. Key is depth, value is (node value, distance)
        visit = {}
        
        def dfs(node, depth=0, dist=0):
            if depth not in visit or depth > visit[depth][1]:
                visit[depth] = (node.val, dist)
            if node.left:
                dfs(node.left, depth + 1, dist - 1)
            if node.right:
                dfs(node.right, depth + 1, dist + 1)
        
        dfs(root)
        output = [visit[key][0] for key in visit.keys()]
        return output
        