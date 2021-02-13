''' Given a tree, validate whether or not it is a binary search tree or not'''

from typing import List
from queue import Queue

# Can take a bit of a pseudo alpha-beta minimax pruning approach.
# Alpha-beta pruning is a modified version of minimax pruning, which is a game-theory ai algorithm for choice optimization.
# Effectively we recurse downwards and keep track of our minimum value and our maximum value
# For example:
#    5
#  2   7
# 1 4 4 6
# 
# In the above example, there is no minimum nor maximum value at the root (5), so everything is good
# When we go left, we set our maximal value to the parent, and when we go right we set our minimal value to our parent. 
# When we visit 2, our maximal value is 5 and our minimal value is negative infinity.
# When we visit 1, our maximal value is now 2 and our minial value is negative infinity.
# When we visit 4 from two, our maximal value is now 5 and our minimal value is now 2. 4 is between those, so we are good.
# When we visit 7, our minimal value is 5 and our maximal value is infinity, so we are good.
# When we visit 4, our maximal value is now 7 and our minimal value is 5. 4 is not within that range, so invalid
# When we go to 6, our minimal value is 7. 6 does not work

class TreeNode():

    def __init__(self, left=None, right=None, value=0):
        self.left, self.right, self.value = left, right, value

class Solution():
    def isValidBinarySearchTree(self, root: TreeNode):
        # Emptry tree is not a valid BST
        if not root:
            return False

        # Passing the root into our alphaBeta recurse.
        return self.alphaBetaRecurse(root, float('inf'), float('-inf'))

    def alphaBetaRecurse(self, node: TreeNode, maximal: int, minimal: int) -> bool:
        # Handling none
        if not node:
            return True

        # Checking against our maximal/minimal values
        if node.value >= maximal or node.value <= minimal:
            return False

        else:
            # Going left; we need to set the maximal value to our current value
            return self.alphaBetaRecurse(node.left, node.value, minimal) and self.alphaBetaRecurse(node.right, maximal, node.value)


# Building our test cases
def buildTree(tree: List[int]) -> TreeNode:
    if len(tree) <= 0:
        return None

    # Using a queue for BFS traversal
    q, root, s = Queue(), TreeNode(value=tree[0]), 1
    q.put(root)

    while not q.empty() and s < len(tree):
        node = q.get()

        # Making a new node while s is not none
        if tree[s]:
            nextNode = TreeNode(value=tree[s])
            node.left = nextNode
            q.put(nextNode)
            
        s += 1

        if tree[s]:
            nextNode = TreeNode(value=tree[s])
            node.right = nextNode
            q.put(nextNode)

        s += 1

    return root

# Test cases
badTree = buildTree([5,2,7,1,4,4,6])
goodTree = buildTree([5,2,7,1,4,6,8])
smallTree = buildTree([1])
noTree = buildTree([])

# Comparing against solution
s = Solution()
print(s.isValidBinarySearchTree(badTree))
print(s.isValidBinarySearchTree(goodTree))
print(s.isValidBinarySearchTree(smallTree))
print(s.isValidBinarySearchTree(noTree))