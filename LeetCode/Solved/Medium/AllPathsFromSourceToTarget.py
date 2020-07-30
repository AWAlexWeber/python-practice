'''
797. All Paths From Source to Target

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
'''

from typing import List

class Solution:
    # Recursive solution that creates new paths for each result
    # This is a slow solution
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.o = []
        self.traverse(graph, 0, [0])
        return self.o
        
    def traverse(self, graph: List[List[int]], index: int, path: List[int]):
        if len(graph[index]) <= 0:
            return self.o.append(path)
        for i in graph[index]:
            np = path[::]
            np.append(i)
            self.traverse(graph, i, np)

    # Faster(ish) solution
    def stillMediocreAllPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph) - 1
        paths = [[0]]
        ans = []
        while paths:
            path = paths.pop()
            for n in graph[path[-1]]:
                if n == N:
                    ans.append(path + [n])
                else:
                    paths.append(path + [n])
        return ans