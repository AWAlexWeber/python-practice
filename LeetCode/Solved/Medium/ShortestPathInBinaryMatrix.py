'''
1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4

 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
'''

from queue import Queue
from typing import List

class Solution:
    def validNewPosition(self, grid: List[List[int]], x: int, y: int, mX: int, mY: int) -> bool:
        if x + mX < 0:
            return False
        if y + mY < 0:
            return False
        if x + mX >= len(grid):
            return False
        if y + mY >= len(grid[0]):
            return False
        
        if grid[x + mX][y + mY] == 1:
            return False
        
        return True
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # No edge weights and restrictive direction. We can simply apply BFS as it will be both optimal and complete. Could revisit and apply Djikstra/A*, but this is fine for now.
        
        # Checking some base-cases; Start or end is blocked.
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
            return -1
        
        # Using a queue to track our BFS frontier. 
        q = Queue()
        # X, Y, current cost
        q.put((0,0,0))
        
        maximalCost = float("inf")
        visit = set()
        
        while not q.empty():
            x, y, cost = q.get()
            
            # Is our current cost greater than or equal to maximal cost? If so, don't explore this node.
            if cost >= maximalCost:
                continue
                
            # Is this our target node?
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                # Reached our target. Setting maximal cost and exiting from this discovery.
                maximalCost = min(maximalCost, cost)
                continue
                
            # Alright, let's see if we can go left, diag, or down.
            for newX in range(-1, 2, 1):
                for newY in range(-1, 2, 1):
                    if newX == 0 and newY == 0:
                        continue
                        
                    if self.validNewPosition(grid, x, y, newX, newY) and (x + newX, y + newY) not in visit:
                        visit.add((x + newX,y + newY))
                        q.put((x + newX, y + newY, cost + 1))
            
        # Adding one to account for the starting node
        return -1 if maximalCost == float("inf") else maximalCost + 1
            