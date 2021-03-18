'''
Given a binary tree, remove any branch that does not contain a target value somewhere in its leaves
'''

class Node:
    def __init__(self, value: int, left: 'Node'=None, right: 'Node'=None):
        self.value, self.left, self.right = value, left, right
    def __repr__(self):
        return f"{self.value}, ({self.left.__repr__()}), ({self.right.__repr__()})"

class Solution:
    def pruneTree(self, root: Node, target: int) -> Node:
        def dfsPrune(node: Node) -> bool:
            isLeft = (False if not node.left else dfsPrune(node.left))
            isRight = (False if not node.right else dfsPrune(node.right))

            if not isLeft:
                node.left = None
            if not isRight:
                node.right = None
            
            return isLeft or isRight or (node.value == target)

        if not dfsPrune(root):
            return None
        else:
            return root

n1 = Node(1)
n2 = Node(2)
n3 = Node(1)
n4 = Node(2)

n1.left = n2
n1.right = n3
n2.left = n4

print(str(n1))
s = Solution()
s.pruneTree(n1, 2)
print(str(n1))