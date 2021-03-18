'''
Find all elements in a binary tree that are in the same row as another element with a target value.
'''

from queue import Queue

class Node:
    def __init__(self, value: int, left: 'Node'=None, right: 'Node'=None):
        self.value, self.left, self.right = value, left, right

class Solution:
    def cousins(self, root: Node, cousin: int):
        q = Queue()
        q.put((0,root))
        currentDepth, currentDepthList = 0, list()
        didFind = False

        while not q.empty():
            depth, node = q.get()

            if depth > currentDepth:
                if didFind:
                    currentDepthList.remove(cousin)
                    return currentDepthList
                else:
                    currentDepth, currentDepthList = depth, list()

            if node.value == cousin:
                didFind = True

            currentDepthList.append(node.value)

            if node.left:
                q.put((depth + 1, node.left))
            if node.right:
                q.put((depth + 1, node.right))

    

        if currentDepth == depth:
            currentDepthList.remove(cousin)
            return currentDepthList
        return list()

n1 = Node(5, Node(3, Node(8), Node(12)), Node(4, Node(2), Node(1)))

s = Solution()
print(s.cousins(n1, 8))