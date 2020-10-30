'''
1192. Critical Connections in a Network

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
'''

# This is obviously asking for Tarjans of some sort.
# First we take a look at an O(V*V*E) solution using BFS and checking if the removal of a connection disables the network. This works but has poor complexity

from typing import List
import collections
import queue

class Solution:
    def criticalConnectionsBFS(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # First doing a quick O(n) precalculation to move all of the connections into a dictionary
        # This makes it more efficient for us to access the actual data values
        h, f = {}, list()
        for c in connections:
            # O(1) amortized
            if c[0] not in h:
                h[c[0]] = set()
            if c[1] not in h:
                h[c[1]] = set()
            h[c[0]].add(c[1])
            h[c[1]].add(c[0])

        for c in connections:
            # Removing this c from our graph
            h[c[0]].remove(c[1])
            h[c[1]].remove(c[0])

            if not self.path(h, c[0], c[1]):
                f.append(c)

            # Adding it back in
            h[c[0]].add(c[1])
            h[c[1]].add(c[0])

        return f
        

    def path(self, connections: dict, start: int, end: int):
        q = queue.Queue()

        # Attempting to find our path
        q.put(start)

        # Visit set
        v = set()

        while not q.empty() > 0:
            # Popping the top
            n = q.get()
            v.add(n)

            for c in connections[n]:
                if c in v:
                    continue

                q.put(c)

                if c == end:
                    return True

        return False

    # Tarjan's algorithm
    def criticalConnectionsTarjans(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Setting our visisted, etc metrics
        if not connections:
            return []

        # Building our edge-based dictionary
        def create_dict(c: List[List[int]]):
            d = collections.defaultdict(list)
            for u, v in c:
                d[u].append(v)
                d[v].append(u)
            return d

        # Getting our tarjan environment set up. Graph, v(isit), count, critical self explanatory. low contains all of the low ids in the form of (id,low) with the key of the node
        graph = create_dict(connections)
        v = [False] * n
        count = 0
        low = collections.defaultdict(dict)
        critical = []

        # Primary tarjan algo
        def tarjan(n, p):
            # Referencing our vars
            nonlocal graph, v, count, low, critical

            # If we've visisted, skip
            if v[n]:
                return
            v[n] = True

            low[n]['id'] = count
            low[n]['low'] = count

            count += 1

            # Going for each neighbor
            for n2 in graph[n]:
                if n2 == p:
                    continue
                
                tarjan(n2, n)

                if low[n]['id'] < low[n2]['low']:
                    critical.append([n,n2])
                low[n]['low'] = min(low[n]['low'], low[n2]['low'])

        tarjan(0,-1)

        return critical