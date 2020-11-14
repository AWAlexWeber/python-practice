'''
695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

from typing import List
import queue

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Basic flood fill
        maxArea, v = 0, set()
        
        # Positional validation function
        def isValid(x: int, y: int) -> bool:
            if x < 0 or y < 0:
                return False
            if x >= len(grid) or y >= len(grid[0]):
                return False
            if (x,y) in v:
                return False
            if grid[x][y] != 1:
                return False
            return True
        
        # Helper function
        def attemptMaxArea(i: int, j: int):
            if (i,j) in v:
                return -1
            else:
                # Actually making this attempt.
                # BFS for all points
                
                # Localized maximum
                localMaximum = 0
                
                # Creating our queue, inserting the starting point
                q = queue.Queue()
                
                if isValid(i, j):
                    q.put((i,j))
                    v.add((i,j))
                
                while not q.empty():
                    # Getting current node
                    (x, y) = q.get()
                    localMaximum += 1
                    
                    if isValid(x + 1, y):
                        q.put((x + 1, y))
                        v.add((x + 1,y))
                    if isValid(x - 1, y):
                        q.put((x - 1, y))
                        v.add((x - 1,y))
                    if isValid(x, y + 1):
                        q.put((x, y + 1))
                        v.add((x, y + 1))
                    if isValid(x, y - 1):
                        q.put((x, y - 1))
                        v.add((x, y - 1))
                        
                return localMaximum
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxArea = max(maxArea, attemptMaxArea(i,j))
                
        return maxArea

# Much faster solution
class SolutionFaster:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_island_area = 0
    
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                
                if(grid[x][y]==1):

                    dfsq = [(x,y)]
                    island_area = 0

                    while dfsq:
                        cx, cy = dfsq.pop(0)
                        if(grid[cx][cy]==1):
                            island_area+=1
                            grid[cx][cy] = 0
                            if(cx > 0):
                                dfsq.append((cx-1,cy))
                            if(cy > 0):   
                                dfsq.append((cx,cy-1))
                            if(cx < len(grid) - 1):
                                dfsq.append((cx+1,cy))
                            if(cy < len(grid[x]) - 1):
                                dfsq.append((cx,cy+1))
                
                    max_island_area = max(max_island_area, island_area)
                
                
        return max_island_area