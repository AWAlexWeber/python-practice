"""
A binary search tree is simply a datastructure that helps enable binary search.
It is a tree where all values to the left are less than the root node, and all values to the right are greater

Implementation below uses node datastructure
"""

import queue

class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value, self.left, self.right = value, left, right

class BinarySearchTree:

    def __init__(self):
        self.size, self.head = 0, None

    def insert(self, value: int):
        # Recursively searching for the next possible value
        p, n = self.head, self.head

        while n != None:
            if n.value > value:
                p = n
                n = n.left
            elif n.value < value:
                p = n
                n = n.right
            # Not allowing duplicate keys
            elif n.value == value:
                return None

        # Inserting
        new = Node(value)
        if p and p.value > value:
            p.left = new
        elif p:
            p.right = new
        else:
            self.head = new
        
    def print(self):
        # BFS printing
        q = queue.Queue()
        q.put(self.head)

        while not q.empty():
            c = q.get()

            if c == None:
                print("null",end=", ")
                continue
            
            print(c.value,end=", ")
            q.put(c.left)
            q.put(c.right)

        print("")

b = BinarySearchTree()
for n in range(5,10):
    b.insert(n)
for n in range(5,0,-1):
    b.insert(n)
b.print()