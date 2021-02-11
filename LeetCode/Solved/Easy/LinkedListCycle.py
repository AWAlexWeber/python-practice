'''
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Simplest approach is to have to pointers that traverse the list
        # One moves at twice the speed of the other.
        # This is the straightforward approach
        if not head:
            return False
        
        pointerOne = head
        pointerTwo = head.next
        
        # This will automatically terminate if we don't have a loop since we will reach the end.
        # This is also O(1) space complexity since we don't track visisted nodes
        # However the time complexity can be variable given we can have strange modulations.
        # A better time complex solution (which would be O(n)) would require O(n) space.
        # Since we are only iterating over O(n*c) times a constant, still O(n) but something to consider
        while pointerOne != pointerTwo and pointerOne and pointerTwo:
            pointerOne = pointerOne.next
            pointerTwo = pointerTwo.next
            if pointerTwo:
                pointerTwo = pointerTwo.next
                
        return pointerOne and pointerTwo and pointerOne == pointerTwo
            