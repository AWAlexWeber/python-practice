'''
Given a tree, find the subtree with the maximum average. Return the root of the subtree.

A subtree of a tree is any node of that tree plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.

Examples
Example 1:
Input:


Output: 13
Example 2:
Input:


Output: 21
Explanation: For the node with value = 1 we have an average of (- 5 + 21 + 5 - 1) / 5 = 4.

For the node with value = -5 we have an average of (-5 / 1) = -5.

For the node with value = 21 we have an average of (21 / 1) = 21.

For the node with value = 5 we have an average of (5 / 1) = 5.

For the node with value = -1 we have an average of (-1 / 1) = -1.

So the subtree of 21 is the maximum.
'''

from typing import List

class TreeNode():
    def __init__(self, val: int=None, children: List['TreeNode']=list()):
        self.val = val
        self.children = children

class Solution():
    def subtreeWithMaximumAverage(self, root: TreeNode) -> TreeNode:
        # We're going to use the recursive approach; O(n) time, O(n) space because of recursive stack.
        # Could be simplified by taking an interative approach, removing recursive stack problems.
        self.maximalValue, self.maximalNode = float('-inf'), None
        self.recurse(root)

        return self.maximalNode

    def recurse(self, root: TreeNode) -> tuple:
        # Handling base-case
        curMaxValue, curNodeCount = float('-inf'), 0
        if len(root.children) <= 0:
            curMaxValue, curNodeCount = root.val, 1
        
        else:
            # Getting the values of all children subtrees
            subtreeTotal, subtreeCount = 0, 0
            for child in root.children:
                childValue = self.recurse(child)
                subtreeTotal += childValue[0]
                subtreeCount += childValue[1]

            subtreeTotal += root.val
            subtreeCount += 1

            curMaxValue = subtreeTotal / subtreeCount
            curNodeCount = subtreeCount

        if curMaxValue > self.maximalValue:
            self.maximalValue = curMaxValue
            self.maximalNode = root

        return (curMaxValue, curNodeCount)

''' Construcing our test case '''
root = TreeNode(1)
leftNode = TreeNode(-5)
leftLeftNode = TreeNode(1)
leftRightNode = TreeNode(2)
leftNode.children = [leftLeftNode, leftRightNode]
centerNode = TreeNode(13)
centerLeft = TreeNode(4)
centerRight = TreeNode(-2)
centerNode.children = [centerLeft, centerRight]
root.children = [leftNode, centerNode, TreeNode(4)]

rootTwo = TreeNode(1)
rootTwo.children = [TreeNode(-5), TreeNode(21), TreeNode(5), TreeNode(-1)]

s = Solution()
print(s.subtreeWithMaximumAverage(root).val)
print(s.subtreeWithMaximumAverage(rootTwo).val)