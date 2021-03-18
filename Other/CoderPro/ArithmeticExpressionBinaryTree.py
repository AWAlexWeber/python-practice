'''
Given a binary tree representing an arithmetic expression return the value.
'''

class TreeNode:
    def __init__(self, value: int, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.value, self.left, self.right = value, left, right

class Solution:
    def arithmeticSum(self, root: TreeNode) -> int:
        arithmetic = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }

        # Essentially we do in order traversal again
        def inOrderDFS(node: TreeNode) -> int:
            if node.value in arithmetic:
                return arithmetic[node.value](inOrderDFS(node.left), inOrderDFS(node.right))
            else:
                return node.value

        return inOrderDFS(root)

n1 = TreeNode('*', TreeNode('+', TreeNode(3), TreeNode(2)), TreeNode('+', TreeNode(4), TreeNode(5)))

s = Solution()
print(s.arithmeticSum(n1))