''' Invert a BST across the vertical axis '''

class Node:
    def __init__(self, val: int, left: 'Node'=None, right: 'Node'=None):
        self.val, self.left, self.right = val, left, right

    def __repr__(self):
        result = self.val
        result += f"{self.left}" if self.left else ''
        result += f"{self.right}" if self.right else ''
        return result

class Solution:
    def invertBST(self, root: Node) -> Node:
        # Handling some errors
        if not root:
            return None

        # Inverting our left and right
        elif not root.left and not root.right:
            return root

        else:
            leftSwap = root.left
            rightSwap = root.right
            root.left = rightSwap
            root.right = leftSwap
            self.invertBST(root.left)
            self.invertBST(root.right)
            return root

n = Node('a')
n.left = Node('b')
n.right = Node('c')
n.left.left = Node('d')
n.left.right = Node('e')
n.right.left = Node('f')

print(n)
print(Solution().invertBST(n))