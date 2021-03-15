'''
Given a tree, check if it exists within a larger tree.
'''

from queue import Queue

class Node:
    def __init__(self, value: int, left: 'Node'=None, right: 'Node'=None):
        self.value, self.left, self.right = value, left, right

class Solution:
    def findSubtree(self, largerTree: Node, subtree: Node) -> Node:
        # We need to explore the larger tree until we find the root of the subtree.
        # Then we need to check that it matches children
        queue = Queue()
        queue.put(largerTree)
        visit = set()

        while not queue.empty():
            node = queue.get()
            if node.value == subtree.value and node not in visit:
                visit.add(node)
                if self.attemptSubtreeSearch(node, subtree, visit):
                    return node

            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

    def attemptSubtreeSearch(self, node: Node, subtree: Node, visit: set) -> bool:
        queue = Queue()
        queue.put((node, subtree))
        while not queue.empty():
            currentNode, compareNode = queue.get()
            if currentNode.value != compareNode.value:
                return False

            if compareNode.left and not currentNode.left or compareNode.right and not currentNode.right:
                return False

            if compareNode.left:
                queue.put((currentNode.left, compareNode.left))
            if compareNode.right:
                queue.put((currentNode.right, compareNode.right))
        
        return True

s = Solution()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
f4 = Node(8)

n1.left = n4
n1.right = n5
n4.left = n3
n4.right = n2
n5.left = n6
n5.right = n7
n7.left = f4

f1 = Node(5)
f2 = Node(6)
f3 = Node(7)
f1.left = f2
f1.right = f3

print(s.findSubtree(n1, f1))