'''
894. All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

 

Note:

1 <= N <= 20
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print(self):
        n = self
        print(n.val, end=" ")
        if n.left:
            n.left.print()
        if n.right:
                n.right.print()

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        # Handling an even number of trees
        if N % 2 == 0:
            return []

        # Initializing our permutation set and the base case
        self.perm = {}

        # Base case; we know these are defined values and they help us build our actual permutation set
        self.perm[0] = list()
        self.perm[1] = list()
        self.perm[0].append(None)
        self.perm[1].append(TreeNode(0))

        if N == 1:
            return self.perm[1]
        elif N == 0:
            return self.perm[0]

        # Building our permutation set using dynamic programming and memoization
        self.buildPermutationSet(N)

    def buildPermutationSet(self, n: int):
        # Initializing our left-right variables
        l, r = 1, n - 2

        # Initializing our current permutation set
        currentPermSet = list()

        # Moving until our left value is less than 2 of N; indicating a full left branch
        while l < n - 1 and r > 0:
            if l not in self.perm:
                self.buildPermutationSet(l)

            if r not in self.perm:
                self.buildPermutationSet(r)

            for ln in self.perm[l]:
                for rn in self.perm[r]:
                    node = TreeNode(0)
                    node.left = ln
                    node.right = rn
                    currentPermSet.append(node)

            l, r = l + 2, r - 2
        
        self.perm[n] = currentPermSet

s = Solution()
s.allPossibleFBT(1)