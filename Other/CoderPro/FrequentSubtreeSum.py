'''
Return the most frequent subset sum.
'''

from collections import defaultdict

class Node:
    def __init__(self, value: int, left: 'Node'=None, right: 'Node'=None):
        self.value, self.left, self.right = value, left, right

class Solution:
    def freqSubtreeSum(self, root: Node) -> int:
        # Essentially just post-order traversal
        counterDict = defaultdict(lambda: 0)

        def dfs(node: Node, d: dict) -> int:
            if not node:
                return 0
            
            value = dfs(node.left, counterDict) + dfs(node.right, counterDict) + node.value
            counterDict[value] += 1
            return value

        dfs(root, counterDict)

        maxSum, maxCount = 0, 0
        for k in counterDict.keys():
            if counterDict[k] > maxCount:
                maxCount, maxSum = counterDict[k], k

        return maxSum

n1 = Node(3, Node(1), Node(-3))
s = Solution()
print(s.freqSubtreeSum(n1))