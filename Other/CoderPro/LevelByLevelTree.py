'''
Given a tree, print it in level-order
'''

from queue import Queue

class Node:
    def __init__(self, value: int, left: 'Node'=None, right: 'Node'=None):
        self.value, self.left, self.right = value, left, right

class Solution:
    def printLevelByLevel(self, root: Node):
        q = Queue()
        q.put((root, 0))
        levelList, currentLevel = list(), 0

        while not q.empty():
            node, depth = q.get()
            if depth != currentLevel:
                print(*levelList)
                levelList, currentLevel = list(), depth

            levelList.append(node.value)

            if node.left:
                q.put((node.left, depth + 1))

            if node.right:
                q.put((node.right, depth + 1))

        print(*levelList)


n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(8)
n5 = Node(12)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

s = Solution()
s.printLevelByLevel(n1)