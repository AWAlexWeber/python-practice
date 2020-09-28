'''
Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

from typing import List

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # Handling null
        if head == None:
            n = Node(insertVal)
            n.next = n
            return n
        
        # Handling a size one
        if head.next == head:
            n = Node(insertVal, head)
            head.next = n
            return n
                
        n = head
        while True:
            
            if n.next.val < n.val:
                # We've reached the end
                # Time to decide if we are going to insert here or just after
                if n.val <= insertVal:
                    # Our insert val is greater than or equal to the maximum value
                    # We will insert here
                    break
                    
                elif insertVal <= n.next.val:
                    # We will insert at the bottom
                    break
                    
            if n.val <= insertVal and n.next.val >= insertVal:
                break
                
            n = n.next
            
            # If we've ever reached the head, again, we have a circular array with all the same numbers
            if n == head:
                break
            
            
        # Inserting
        print(n.val)
        pointNext = n.next
        node = Node(insertVal, pointNext)
        n.next = node
        
        return head
            
        