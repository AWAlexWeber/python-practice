'''
1305. All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # Let's do morris traversal across both roots at once
        # We append to output the smaller value
        i, j, o, l, r = 0, 0, [], self.fill(root1, []), self.fill(root2,[])
        while i < len(l) or j < len(r):
            if i < len(l) and j < len(r):
                if l[i] < r[j]:
                    o.append(l[i])
                    i += 1
                else:
                    o.append(r[j])
                    j += 1
            elif i < len(l):
                o.append(l[i])
                i += 1
            else:
                o.append(r[j])
                j += 1
        return o
        
        
    def fill(self, root: TreeNode, r: List[int]) -> List[int]:
        while root is not None: 
          
            if root.left is None: 
                r.append(root.val)
                root = root.right 
            else: 

                # Find the inorder predecessor of root 
                pre = root.left 
                while pre.right is not None and pre.right is not root: 
                    pre = pre.right 

                if pre.right is None: 

                    # Make root as right child of its inorder predecessor 
                    pre.right = root 
                    root = root.left         

                else: 
                    # Revert the changes made in the 'if' part to restore the  
                    # original tree. i.e., fix the right child of predecessor 
                    pre.right = None
                    r.append(root.val)
                    root = root.right 
                    
        return r