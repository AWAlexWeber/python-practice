'''
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''

from typing import List

import queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # BFS queue approach
        # This is just flood fill variant
        q = queue.Queue()
        total_oranges = 0
        total_rotten_oranges = 0
        
        # Getting all rotten oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    v = (r,c,1)
                    q.put(v)
                    total_oranges += 1
                    total_rotten_oranges += 1
                    
                elif grid[r][c] == 1:
                    total_oranges += 1
                    
        # Do we have no oranges and no rotten oranges?
        print(total_rotten_oranges)
        if total_rotten_oranges >= total_oranges:
            return 0
        
        visisted = set()
        time_elapsed = 0
        while not q.empty():
            
            # Popping our data
            (x,y,depth) = q.get()

            # Skip empty cells
            if grid[x][y] == 0:
                continue
            
            # Skip if already visisted
            if (x,y) in visisted:
                continue
            
            if grid[x][y] != 0:
                if grid[x][y] == 1:
                    total_rotten_oranges += 1
                    grid[x][y] = 2
                visisted.add((x,y))
                
            time_elapsed = max(time_elapsed, depth)
                
            # Adding neighbors
            # Trying to decrement x
            if x > 0 and (x - 1, y) not in visisted:
                q.put((x - 1, y, depth + 1))
            if x < len(grid) - 1 and ((x + 1, y)) not in visisted:
                q.put((x + 1, y, depth + 1))
            if y > 0 and (x, y - 1) not in visisted:
                q.put((x, y - 1, depth  + 1))
            if y < len(grid[0]) - 1 and ((x, y + 1)) not in visisted:
                q.put((x, y + 1, depth + 1))

        if total_rotten_oranges == total_oranges:
            return time_elapsed - 1
        return -1