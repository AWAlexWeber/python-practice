# Here are the three main tree traversals

# In Order
# Pre Order
# Post Order

# In order traverses by going left, root right
# Pre order traverses by going root, left, right
# Post order traverses by going left, right, root

# Additionally, breadth first goes through every node at a level of depth before going to the next level

# Given a tree such as
#           4
#     3           5
# 1      2     6      7

# In order would be
# 1 3 2 4 6 5 7

# Pre order would be
# 4 3 1 2 5 6 7

# Post order would be
# 1 2 3 6 7 5 4

# Depth first would be
# 4 3 5 1 2 6 7

# Here are the implementations, given a tree node

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

# Generating our tree
t = TreeNode(4)
t.left = TreeNode(3, TreeNode(1), TreeNode(2))
t.right = TreeNode(5, TreeNode(6), TreeNode(7))

# Note that all of these algorithms use a recursive approach
# See morris tree traversal for a non-recursive approach to traversing (specifically in order)

# Traversing in-order
def inorder(node: TreeNode):
    if (node.left != None):
        inorder(node.left)
    print(node.val,end="")

    if (node.right != None):
        inorder(node.right)

inorder(t)
print("")

# Traversing pre-order
def preorder(node: TreeNode):
    print(node.val,end="")

    if (node.left != None):
        preorder(node.left)
    if (node.right != None):
        preorder(node.right)

preorder(t)
print("")

# Traversing post-order
def postorder(node: TreeNode):
    if (node.left != None):
        postorder(node.left)
    if (node.right != None):
        postorder(node.right)

    print(node.val,end="")

postorder(t)
print("")

# Traversing depth first
# This is accomplished through the use of a queue
def depthFirst(root: TreeNode):
    if root is None:
        return

    # Creating our queue
    q = []

    q.append(root)

    while(len(q) > 0):
        print(q[0].val,end="")
        node = q.pop(0)

        if not node.left == None:
            q.append(node.left)

        if not node.right == None:
            q.append(node.right)
    
depthFirst(t)