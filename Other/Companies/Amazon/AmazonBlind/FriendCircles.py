'''

'''

from typing import List
from queue import Queue

class Solution():
    def friendCircles(self, friends: List[List[int]]) -> int:
        # Basically an adjacency matrix
        # Going to turn this into a graph problem; building list of edges and visisted set we traverse all possible friends counting the number of circles

        # First, building our graph
        edges = {}
        for index, row in enumerate(friends):
            edges[index] = set()
            for neighborIndex, neighbor in enumerate(row):
                if neighbor == 1:
                    edges[index].add(neighborIndex)

        # Now we perform BFS on all nodes
        visit = set()
        circles = 0
        for node in range(len(friends)):
            q = Queue()
            if node not in visit:
                q.put(node)
                circles += 1

            while not q.empty():
                visitNode = q.get()
                for neighbor in edges[visitNode]:
                    if neighbor not in visit:
                        q.put(neighbor)
                        visit.add(neighbor)

        return circles
            
s = Solution()
print(s.friendCircles([[1,1,0],[1,1,1],[0,1,1]]))