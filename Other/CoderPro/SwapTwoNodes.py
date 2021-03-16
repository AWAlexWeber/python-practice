'''
Swap every two nodes.
'''

from typing import List

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next=next

    def __repr__(self):
        return (str(self.val) + ("" if not self.next else ' -> ' + str(self.next)))

def createLinkedList(arr: List[int]) -> Node:
    head = Node(0)
    current = head
    for n in arr:
        current.next = Node(n)
        current = current.next
    return head.next

class Solution:
    def swapTwoNodes(self, root: Node) -> Node:
        # Creating a fake node to ensure we don't lose track of our primary node
        fakeHead = Node(0)
        fakeHead.next = root

        left, middle, right = fakeHead, fakeHead.next, fakeHead.next.next
        while right:
            middle.next = right.next
            right.next = middle
            left.next = right

            left, middle = middle, middle.next
            if not middle:
                break
            right = middle.next

        return fakeHead.next

s = Solution()
f = createLinkedList([1,2,3,4,5,6,7,8,9,10,11,12])
print(f)
o = s.swapTwoNodes(f)
print(o)