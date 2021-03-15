'''
Given a linked list, rotate it horizontally such that
1-2-3-4-5 after two rotations to the right becomes 4-5-1-2-3
'''

from typing import List

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value) + ' ' + ('' if not self.next else str(self.next))

class Solution:
    def rotateLeft(self, root: Node, rotations: int) -> Node:
        headPointer = root
        endPointer = root
        while endPointer.next:
            endPointer = endPointer.next
        endPointer.next = headPointer
        for i in range(rotations):
            headPointer = headPointer.next
            endPointer = endPointer.next
        endPointer.next = None
        return headPointer

    def rotateRight(self, root: Node, rotations: int) -> Node:
        headPointer, endPointer, totalLength = root, root, 0
        while endPointer.next:
            endPointer = endPointer.next
            totalLength += 1
        endPointer.next = headPointer
        for i in range(totalLength - rotations + 1):
            headPointer = headPointer.next
            endPointer = endPointer.next
        endPointer.next = None
        return headPointer


def createLinkedList(arr: List[int]) -> Node:
    head = Node(0)
    current = head
    for n in arr:
        current.next = Node(n)
        current = current.next
    return head.next

s = Solution()
linkedList = createLinkedList([1,2,3,4,5])
print(s.rotateLeft(linkedList, 2))
linkedList = createLinkedList([1,2,3,4,5])
print(s.rotateRight(linkedList, 2))