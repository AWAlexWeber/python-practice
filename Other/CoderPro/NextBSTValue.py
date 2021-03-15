'''
Given a Balanced BST, return the next highest value present in the tree.
'''

from queue import Queue
from collections import defaultdict

# This is straightforward, going to convert it into an array such that the left value is (index*2)+1, and right value is (index*2)+2
class TreeNode:
    def __init__(self, val: int, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val, self.left, self.right = val, left, right

class TreeSerializer:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ''
        
        d = defaultdict(lambda: list())
        currentMaxDepth = 0
        q = Queue()
        q.put((0, root))

        while not q.empty():
            (depth, node) = q.get()
            if type(node) != str:
                currentMaxDepth = max(currentMaxDepth, depth)
                d[depth].append(node.val)
            
            else:
                d[depth].append(node)

            # If we are too deep we do not progress any further
            if depth > currentMaxDepth:
                continue

            if type(node) != str:
                if node.left:
                    q.put((depth + 1, node.left))
                else:
                    q.put((depth + 1, 'x'))
                if node.right:
                    q.put((depth + 1, node.right))
                else:
                    q.put((depth + 1, 'x'))
            
            else:
                q.put((depth + 1, 'x'))
                q.put((depth + 1, 'x'))

        output = list()
        for i in range(currentMaxDepth + 1):
            output.append(''.join(d[i]))
        return (''.join(output))

    def deserialize(self, data: str) -> TreeNode:
        if len(data) <= 0:
            return None

        def dfs(idx: int) -> TreeNode:
            # Creating the current node. Checking for null
            if data[idx] == 'x':
                return None

            node = TreeNode(data[idx])

            leftIdx = (idx*2) + 1
            rightIdx = (idx*2) + 2

            if leftIdx < len(data):
                node.left = dfs(leftIdx)
            
            if rightIdx < len(data):
                node.right = dfs(rightIdx)

            return node

        root = dfs(0)
        return root

s = TreeSerializer()
root = s.deserialize('4281x59xxxxx7xx')

class Solution:
    def nextHighestValue(self, root: TreeNode, targetVal: int) -> int:
        # Basically we are going to search this tree in order. When we find our node value, we pass up a true and make a comparison.
        outputVal = float('inf')
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if int(node.val) > targetVal:
                outputVal = min(outputVal, int(node.val))
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        return outputVal

    def nextInorderSuccessor(self, root: TreeNode, targetVal: int) -> int:
        # This one we will correctly implement in-order traversal.
        global output
        output = None

        def inOrder(node: TreeNode, didFind: bool=False):
            global output
            if node.left:
                didFind = inOrder(node.left, didFind)
            if didFind and not output:
                output = node.val
            if node.val == targetVal:
                didFind = True
            if node.right:
                didFind = inOrder(node.right, didFind)
            return didFind

        inOrder(root)
        return output
        
    
s = Solution()
print(s.nextInorderSuccessor(root, '7'))