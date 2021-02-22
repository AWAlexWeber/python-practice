'''

'''

from collections import defaultdict
from typing import List

class Solution():
    def minCostConnectNodes(self, nodes: int, edges: List[tuple], newEdges: List[tuple]) -> int:
        if nodes <= 1:
            return 0

        # First thing we need to do is build a way to track our connected graph.
        # We are going to use a dictionary of sets; key = node, value = set of nodes within the same graph
        # This means that as long as the length of our dictionary[0] != len(nodes), we don't have a completed graph.
        # We can also check if an edge doesn't combine a new graph because both nodes will already be in the same set.
        d = defaultdict(lambda: set())

        # Adding the initial values
        for n in range(1, nodes + 1):
            d[n].add(n)

        # Creating our graphs in d. O(k) where k is the number of starting edges
        for start, end in edges:
            d[start].add(start)
            d[start].add(end)
            d[end] = d[start]

        # Sorting our newEdges since we will ALWAYS pick the cheapest connector. 
        newEdges.sort(key = lambda t: t[2])

        # Now, while the length of our dictionary's set is not equal to the number of nodes, we add connections.
        # O(n * k)
        totalCost = 0
        for start, end, cost in newEdges:
            if len(d[1]) == nodes:
                return totalCost
            if end not in d[start]:
                # This edge creates a connection. 
                for node in d[end]:
                    if node in d[start]:
                        continue
                    d[start].add(node)
                d[end] = d[start]
                totalCost += cost
        return totalCost

s = Solution()
print(s.minCostConnectNodes(5, [], [[1,2,10],[2,1,10],[3,4,5],[4,3,1],[2,3,10],[2,4,15],[1,3,12],[4,5,10]]))
print(s.minCostConnectNodes(6, [[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))