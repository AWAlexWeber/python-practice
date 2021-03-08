'''
Given a binary tree determine its depth
'''

class Node:
    def __init__(self, val: int, left: 'Node'=None, right: 'Node'=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    # Simple recursive problem.
    # Can solve either DFS or BFS, depends on the tree (if we expect a really wide but shallow go DFS since less space complexity, deep but thin go BFS).
    # We will solve dfs
    def binaryTreeDepth(self, root: Node) -> int:
        # Maximum value
        self.maxVal = 0

        if not root:
            return 0

        def dfs(node: Node, depth: int):
            # Limiting comparisons
            if not node.left and not node.right:
                self.maxVal = max(depth, self.maxVal)
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 1)
        return self.maxVal

s = Solution()

# Building test case
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.left = n2
n1.right = n4
n2.left = n3

print(s.binaryTreeDepth(n1))
