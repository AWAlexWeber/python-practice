'''
Cloudfront Caching AWS CloudFront wants to build an algorithm to measure the efficiency of its caching network. The network is represented as a number of nodes and a list of connected pairs. The efficiency of this network can be estimated by first summing the cost of each isolated set of nodes where each individual node has a cost of 1. To account for the increase in efficiency as more nodes are connected, update the cost of each isolated set to be the ceiling of the square root of the original cost and return the final sum of all costs. Example n = 10 nodes edges = [[1 2], [1 3], [2 4], [35], [7 8]] 7 10 2 3 8 4 5 There are 2 isolated sets with more than one node, {1, 2, 3, 4, 5} and {7, 8}. The ceilings of their square roots are 51/2 = 2.236 and ceil(2.236) = 3, 21/2 = 1.414 and ceil(1.414) = 2. The other three isolated nodes are separate and the square root of their weights is 11/2 = 1 respectively. The sum is 3 + 2 + (3 * 1) = 8.
'''

from typing import List
from collections import defaultdict
from queue import Queue
import math

class Solution():
    def cloudfrontCaching(self, nodes: int, edges: List[tuple]) -> int:
        # What we want to do is basically 'explore' each node and any/all of it's children, counting it up.
        # We are going to do that iteratively. Since this is a direct network we're going to assume there are no fan-out motifs which could break this.
        # If it's not a directed network we will need to go backwards on edges
        edgeDict = defaultdict(lambda: list())

        # Turning our edges into a dictionary for ease of use.
        for edge in edges:
            start, end = (edge)
            edgeDict[start].append(end)
            # If we are a directed graph, remove the following
            edgeDict[end].append(start)

        # Alright, now for everyone node we are going to explore it. Every node that we encounter gets added to the visited set and skipped in the future
        visit = set()
        totalCount = 0
        # Assuming we're starting at 1 because the example does not have a zero in it.
        for node in range(1, nodes+1):
            q = Queue()
            if node not in visit:
                q.put(node)
                visit.add(node)
            else:
                # Skipping since we've visisted this before
                continue

            totalNodeVisit = 0
            # Alright simple BFS on our current node, counting the total nodes
            while not q.empty():
                totalNodeVisit += 1
                n = q.get()
                for neighbor in edgeDict[n]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        q.put(neighbor)
            
            # Calculating the value
            outputVal = math.ceil(math.sqrt(totalNodeVisit))
            totalCount += outputVal

        return totalCount

s = Solution()
val = s.cloudfrontCaching(10, [[1,2],[1,3],[2,4],[3,5],[7,8],[3,8]])
print(val)