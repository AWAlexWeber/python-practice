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

t1 = TreeNode(val=0)
s = Solution()