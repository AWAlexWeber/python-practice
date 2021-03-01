''' Given a linked list, remove the kth last element.

ie if we wanted to remove the 3rd last element from 1 2 3 4 5 6 7 8 9 we would remove 7 and have 1 2 3 4 5 6 8 9
'''

class Node:
    def __init__(self, val: int, next: 'Node'=None):
        self.val, self.next = val, next

    def __repr__(self):
        return str(self.val) + " -> " + ("None" if not self.next else str(self.next))

class Solution:
    def removeKthLastElement(self, k: int, node: 'Node') -> 'Node':
        head = node
        length = 0
        while head:
            length += 1
            head = head.next

        # Okay we've found the total size
        removeIndex = length - k - 1
        if removeIndex < 0:
            # If we are trying to remove a node that doesn't exist, we return the origina linkedlist unmodified.
            return node

        if removeIndex == 0:
            # If we are removing the first node, just return what's after that. This is an edge case for handlign size 1 linked lists as well as the first value.
            output = node.next
            node.next = None
            return output

        # Iterating until we've reached our remove index
        head = node.next
        previous = node
        length = 1
        while head:
            if length == removeIndex:
                # Making the swap
                previous.next = head.next
                head.next = None
                break

            length += 1
            previous = head
            head = head.next

        return node

# Building our test linked list
root = Node(0)
node = root
for j in range(1,10):
    node.next = Node(j)
    node = node.next

s = Solution()
print(root)
f = s.removeKthLastElement(9, root)
print(f)