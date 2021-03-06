from collections import defaultdict
import collections

class Node:
    def __init__(self, val: int, nextNode: 'Node'=None):
        self.val = val
        self.nextNode = nextNode

    def __repr__(self):
        return str(self.val) + " -> " + ("" if not self.nextNode else str(self.nextNode))

class Solution:
    def removeZeroSumConsecutiveNodes(self, node: Node) -> Node:
        # Tracking the total sums at each node while also tracking the sum by the node.
        # Node to sum points to the previous ndoe; this is important.
        nodeToSum = defaultdict(lambda: 0)

        # Return node
        outputNode = node

        # Iterate through all nodes starting at node
        # If we ever reach a total sum of zero, we 'reset' our entire process, setting our output node to the current node. We also reset our nodal sums.
        currentNode, currentSum = node, 0
        while currentNode:
            # Incrementing our current node value
            currentSum += currentNode.val
            if currentSum in nodeToSum:
                # Deleting everything between nodeToSum and the current node.
                nodeToSum[currentSum].nextNode = currentNode.nextNode

            elif currentSum != 0 and currentSum not in nodeToSum:
                nodeToSum[currentSum] = currentNode

            if currentSum == 0:
                # Deleting everything from the start to this node, while also reseting our dictionaries.
                nodeToSum = defaultdict(lambda: 0)
                outputNode = currentNode.nextNode
            
            currentNode = currentNode.nextNode

        return outputNode

class BetterSolution:
    def removeZeroSumSublists(self, node: Node) -> Node:
        sumToNode = collections.OrderedDict()
        sum = 0
        dummy = Node(0)
        dummy.next = node
        n = dummy
        while n:
            sum += n.val
            if sum not in sumToNode:
                sumToNode[sum] = n
            else:
                prev = sumToNode[sum]
                prev.next = n.next
                while list(sumToNode.keys())[-1] != sum:
                    sumToNode.popitem()
            n = n.next
        return dummy.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(-3)
n5 = Node(-2)
n6 = Node(5)

n1.nextNode = n2
n2.nextNode = n3
n3.nextNode = n4
n4.nextNode = n5
n5.nextNode = n6

s = Solution()
print(s.removeZeroSumConsecutiveNodes(n1))

n1 = Node(5)
n2 = Node(4)
n3 = Node(3)
n4 = Node(-3)
n5 = Node(-4)
n6 = Node(-5)

n1.nextNode = n2
n2.nextNode = n3
n3.nextNode = n4
n4.nextNode = n5
n5.nextNode = n6

s = Solution()
print(s.removeZeroSumConsecutiveNodes(n1))

n1 = Node(3)
n2 = Node(1)
n3 = Node(2)
n4 = Node(-1)
n5 = Node(-2)
n6 = Node(4)
n7 = Node(1)

n1.nextNode = n2
n2.nextNode = n3
n3.nextNode = n4
n4.nextNode = n5
n5.nextNode = n6
n6.nextNode = n7

s = Solution()
print(s.removeZeroSumConsecutiveNodes(n1))