'''
Given a tree, write a function to serialize it into a string and then deserialize it.
'''

from queue import Queue
from collections import defaultdict

# This is straightforward, going to convert it into an array such that the left value is (index*2)+1, and right value is (index*2)+2
class TreeNode:
    def __init__(self, val: int, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val, self.left, self.right = val, left, right

class Solution:
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

s = Solution()
root = s.deserialize('13425x7xx2xxxxx')
print(s.serialize(root))