'''
Given a linked list, return a linked list without the duplicates.
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
    def removeLinkedListDuplicates(self, root: Node):
        s, c, p = set(), root.next, root
        s.add(p.val)
        while c:
            if c.val in s:
                c = c.next
            else:
                s.add(c.val)
                p.next = c
                p = p.next

        p.next = c
            

linkedList = createLinkedList([1,1,2,3,4,5,5,6,1,5,1,2,6,8,9,0,4,2,1,4,6,8,9,0,1,2,3,5,1,2,3,4,5,6,7,8,9])
print(str(linkedList))
s = Solution()
s.removeLinkedListDuplicates(linkedList)
print(str(linkedList))