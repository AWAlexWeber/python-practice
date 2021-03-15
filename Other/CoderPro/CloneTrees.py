'''
Given a binary search tree and a node within it, find the same node within a duplicate tree without making any sort of comparisons between node values
'''

from queue import Queue

class Node:
    def __init__(self, value: int, left: 'Node'=None, right: 'Node'=None):
        self.value, self.left, self.right = value, left, right

class Solution:
    def findDuplicateNode(self, root: Node, clone: Node, target: Node) -> Node:
        # We will perform some sort of traversal on our root node.
        # After we've found our target node, we will percolate up the final path
        traverse = list()
        travel = list()
        visit = set()

        # Calculating our path to our target node
        traverse.append(root)
        while len(traverse) > 0 and traverse[-1] != target:
            current_node = traverse[-1]
            if (not current_node.left or current_node.left in visit) and (not current_node.right or current_node.right in visit):
                if current_node.left:
                    visit.remove(current_node.left)
                if current_node.right:
                    visit.remove(current_node.right)
                traverse.pop()
                travel.pop()
                continue

            if current_node.left and current_node.left not in visit:
                visit.add(current_node.left)
                traverse.append(current_node.left)
                travel.append('left')
                continue

            elif current_node.right and current_node.right not in visit:
                visit.add(current_node.right)
                traverse.append(current_node.right)
                travel.append('right')
                continue

        if len(traverse) <= 0:
            return None

        current_clone_node = clone
        for move in travel:
            if move == 'left':
                current_clone_node = current_clone_node.left
            if move == 'right':
                current_clone_node = current_clone_node.right

        return current_clone_node

    def findDupImproved(self, root: Node, clone: Node, target: Node) -> Node:
        # Traversing both trees at the same time using BFS.
        qRoot, qClone = Queue(), Queue()

        qRoot.put(root)
        qClone.put(clone)

        while not qRoot.empty():
            rootNode = qRoot.get()
            cloneNode = qClone.get()

            if rootNode == target:
                return cloneNode

            if rootNode.left:
                qRoot.put(rootNode.left)
                qClone.put(cloneNode.left)

            if rootNode.right:
                qRoot.put(rootNode.right)
                qClone.put(cloneNode.right)

        return None

n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(8)
n5 = Node(12)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

m1 = Node(5)
m2 = Node(10)
m3 = Node(15)
m4 = Node(8)
m5 = Node(12)

m1.left = m2
m1.right = m3
m3.left = m4
m3.right = m5

s = Solution()
f = s.findDupImproved(n1, m1, n4)
print(f.value, n4.value)