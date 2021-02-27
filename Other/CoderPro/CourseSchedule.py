'''
Course Schedule
'''

from collections import defaultdict
from typing import List
from queue import Queue

# Classic DAG question.
class Solution:
    def courseSchedule(self, numCourses: int, preqres: List[tuple]) -> List[int]:
        # First we need to build our edges. Assuming first index is prereq, second is class.
        edges = defaultdict(set)
        for edge in preqres:
            start, end = (edge)
            edges[start].add(end)

        # Okay we've built our edge.
        # Now what we are going to do is recurse through our data.
        visit = set()
        recurseStack = set()
        q = Queue()
        output = list()

        # DFS search for DAG
        def dfs(node):
            visit.add(node)
            recurseStack.add(node)
            for neighbor in edges[node]:
                if neighbor in recurseStack:
                    return False
                elif neighbor not in visit:
                    if not dfs(neighbor):
                        return False
            recurseStack.remove(node)
            output.append(node)
            return True

        for n in range(numCourses):
            if n not in visit:
                if not dfs(n):
                    return []

        # Adding our last values
        for n in range(numCourses):
            if n not in visit:
                output.append(n)

        return output[::-1]

s = Solution()
f = s.courseSchedule(8, [(0,1),(0,2),(1,2),(2,3),(1,3),(3,4),(4,5),(0,5),(6,0),(3,7),(7,4)])
print(f)
f = s.courseSchedule(3, [(0,1),(1,2),(2,0)])
print(f)