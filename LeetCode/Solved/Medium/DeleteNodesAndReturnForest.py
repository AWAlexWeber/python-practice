'''
1110. Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import queue

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # Checking for base cases
        if root == None:
            return list()
        
        # Converting our list to a set because it's easier to check if our value is in it
        toDeleteSet = set(to_delete)
        
        # Creating an output list
        outputList = list()
        
        # Now, what we're going to do is perform BFS. If our current node is in to delete, we will add its children.
        # Before we add its children, if its children are inthen we simply just continue.
        # Once we've added, we delete our parent connection.
        q = queue.Queue()
        
        # Checking if we want to add our root node to our output list.
        # This is the only manual check we need to perform.
        if root.val not in toDeleteSet:
            outputList.append(root)
            
        # Inserting root into our queue and beginning BFS.
        # Format for our tuple is (node, parent node). Need to track parent node to decouple it.
        q.put((root, None))
        
        while not q.empty():
            node, parent = q.get()
            
            # If this is in our delete, we simply disconnect it.
            if node.val in toDeleteSet:
                # Have to manually check which direction we went
                if parent:
                    if parent.left and node.val == parent.left.val:
                        # Disconnecting our left side of the parent since we match the parents left value.
                        parent.left = None

                    elif parent.right and node.val == parent.right.val:
                        # Disconnecting the right side since the right side of the parent matches us.
                        parent.right = None

                    else:
                        print("Error - Invalid selected parent.")
                    
                # Now that we've made our deletion, we check to see if our children are in the to delete set
                # Note that if they are, we do not add them
                if node.left and node.left.val not in toDeleteSet:
                    # Add left
                    outputList.append(node.left)
                    
                if node.right and node.right.val not in toDeleteSet:
                    outputList.append(node.right)
                    
            # Now we simply BFS to the next set of nodes, if they exist
            if node.left:
                q.put((node.left, node))
            if node.right:
                q.put((node.right, node))
                
        return outputList