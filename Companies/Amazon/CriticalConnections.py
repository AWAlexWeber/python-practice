'''
Amazon wants to pilot hardware replacements in data center AMZN525, to increase the reliability of the network. AMZN525 has a "connected" network of data servers i.e. every server can communicate with the rest of the network. The data servers are connected by point-to-point cables to establish "critical" or "non-critical" connections. A connection is considered "critical" if its removal results in a disconnected network of servers. Amazon wants to significantly increase the reliability of its Data Centers by replacing the critical connections with far more reliable cables.

Write a method that returns critical connections in AMZN525.

Input:
The input to the method consists of three arguments -
numOfServers an integer representing number of servers in the data center;
numOfConnections an integer representing number of connections between the servers;
connections a list of pairs of integers representing the connections between the two servers.

Output
Return a list of pairs of integers representing the critical connections. If there are no critical connectionr, return a list with an empty pair - not just an empty list.

Constraints
0 <= numOfServers <= 10^5
0 <= numOfConnections <= 10^5
1 <= connections[i][j] <= numOfServers
0 <= i <= numOfConnections
0 <= j <2

Example
Input:
numOfServers=5
numOfConnections=5
connections=[[1,2],[1,3],[3,4],[1,4],[4,5]]

Output:
[[1,2],[4,5]]
'''

import queue
from typing import List

class Solution:

    # Remove each connection, check for a path
    # O(n^2) total (not as efficient as something like Tarjan's)
    def criticalConnections(self, numOfServers: int, numOfConnections: int, connections: List) -> List[int]:
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

        # O(n^2) where n is the number of connections
        for c in connections:
            # Removing this c from our graph
            h[c[0]].remove(c[1])
            h[c[1]].remove(c[0])

            # Maximum of O(n)
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

s = Solution()
print(s.criticalConnections(4, 4, [[0,1],[1,2],[2,0],[1,3]]))




