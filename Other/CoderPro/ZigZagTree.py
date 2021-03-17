
from collections import defaultdict
from queue import Queue
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        layer = defaultdict(lambda: list())
        q = Queue()
        q.put((0, root))
        
        while not q.empty():
            depth, node = q.get()
            layer[depth].append(node.val)
            
            if node.left:
                q.put((depth + 1, node.left))
            if node.right:
                q.put((depth + 1, node.right))
                
        output = list()
        for i in range(0, depth + 1):
            layerArray = layer[i]
            if i % 2 != 0:
                layerArray.reverse()
            output.append(layerArray)
        return output