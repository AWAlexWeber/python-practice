# Morris tree traversal is an in-order tree traversal algorithm that does not rely on recursion
# Using a non-recursive tree traversal algorithm can be useful for accessing a similar dataset at all times

# It accomplishes this by linking the furthest right node in the left subtree to the root
# The main goal here is to allow for us to, when we've completed iterating, to return to the 'root'
# The furthest right node in the left subtree would be the last node we would visit in an inorder traversal of a tree
# ie if we have something like:
#           10
#       5      30
#  -2      6       40
#    -2      8
#  -1
# Starting with an in-order traversal of our tree from 10
# Note that the tree is
# 10 -> 5, 30
# 5 -> -2, 6
# -2 -> -2
# -2 -> -1
# 6 -> 8
# 30 -> 40

# First we go left in 10, but when we finish going left we want to be able to get back to 10
# So what we do is we set the right node on 8 to point back to 10
# When we hit 8 and go right, it takes us back to 10
# Then we remove that fake link
# We do this for every sub-tree where there is a left node and a right most element
# In this tree's case we have the left-subtree starting with 5, and the left subtree starting with -2
# The right most node of our 5 left subtree is 8
# The right most node of our -2 left subtree is -2
# Therefor, the right node of 8 temporarily points to 10, and the right node of the second -2 temporarily points to -5
# Basically every right most node in a left subtree points to the parent of that sub tree

# Another, weird way to look at it is if we consider this graph
#           10
#          9
#         8
#        7
#       6

# Every node would temporarily have its right point to the tree above it
  
class TreeNode: 
    """A binary tree node"""
    def __init__(self, data, left=None, right=None): 
        self.data = data 
        self.left = left 
        self.right = right 

  
def morris_traversal(root: TreeNode): 
    """Generator function for iterative inorder tree traversal"""
  
    current = root 
      
    while current is not None: 
          
        if current.left is None: 
            print(current.data,end="")
            current = current.right 
        else: 
  
            # Find the inorder predecessor of current 
            pre = current.left 
            while pre.right is not None and pre.right is not current: 
                pre = pre.right 
  
            if pre.right is None: 
  
                # Make current as right child of its inorder predecessor 
                pre.right = current 
                current = current.left         
  
            else: 
                # Revert the changes made in the 'if' part to restore the  
                # original tree. i.e., fix the right child of predecessor 
                pre.right = None
                print(current.data,end="")
                current = current.right 

t = TreeNode(4)
t.left = TreeNode(3, TreeNode(1), TreeNode(2))
t.right = TreeNode(5, TreeNode(6), TreeNode(7))

morris_traversal(t)