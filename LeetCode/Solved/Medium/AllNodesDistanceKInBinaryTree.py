'''
863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

import queue

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # Reversing the tree
        q = queue.Queue()
        par = {}
        targetNode = None
        
        q.put((root, None))
        while not q.empty():
            n, p = q.get()
            par[n.val] = p
            if n.val == target.val:
                targetNode = n
                break
            else:
                if n.left:
                    q.put((n.left, n))
                if n.right:
                    q.put((n.right, n))
                    
        output = list()
        q = queue.Queue()
        q.put((targetNode, 0))
        v = set()
        while not q.empty():
            n, d = q.get()
            
            if not n:
                continue
            
            if n.val in v:
                continue
                
            if d > K:
                continue
                
            v.add(n.val)
            if d == K:
                output.append(n.val)
                continue
                
            else:
                if n.left:
                    q.put((n.left, d + 1))
                if n.right:
                    q.put((n.right, d + 1))
                if n.val in par:
                    q.put((par[n.val], d + 1))
                    
        return output
            