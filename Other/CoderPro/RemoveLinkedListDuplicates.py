'''
Given a linked list, return a linked list without the duplicates.
'''

def createLinkedList(arr: List[int]) -> Node:
    head = Node(0)
    current = head
    for n in arr:
        current.next = Node(n)
        current = current.next
    return head.next
