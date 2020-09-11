'''
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''
from typing import List

# DFS Approach
# It's functionally identical to the more popular BFS approach, but it is depth first in order to keep the list complexity code as simple as possible
# IE When we pop from our list, we want it to be O(1) and that only works if we pop from the tail. We also what insertion to be O(1) which is also only when you append to tail
# So for that reason we pop and append from our tail, making it DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Number of islands
        o = 0

        # Strategy here is to visit every node from top-left to bottom right. If a node has a value of 0, we skip.
        # If a node has a value of 1, we begin a DFS for that island, swapping all nodes to 0 and then incrementing the island count by 1

        # This is effectively going to be O(2n) as the worst case is we visit every node twice, which amortizes into O(n)
        # Where N is the total number of tiles. We can also represent it as O(2 * N * M) where n = rows and m = colums, which is O(n*m)
        for r, row in enumerate(grid):
            for c, tile in enumerate(row):
                if tile == '0':
                    continue

                else:
                    self.numIslandsDFS(grid, r, c)
                    o += 1

        return o
            


    def numIslandsDFS(self, grid, r, c):
        # Queue that tracks the next node to visit
        q = list()

        q.append((r,c))

        while len(q) > 0:
            # Popping off the current queue
            node = q.pop()

            # Visiting by setting to zero since we don't really care about preserving the board state
            y, x = node[0], node[1]
            grid[y][x] = '0'

            if x - 1 >= 0 and grid[y][x - 1] == '1':
                q.append((y, x - 1))
            if y - 1 >= 0 and grid[y - 1][x] == '1':
                q.append((y - 1, x))
            if x + 1 < len(grid[0]) and grid[y][x + 1] == '1':
                q.append((y, x + 1))
            if y + 1 < len(grid) and grid[y + 1][x] == '1':
                q.append((y + 1, x))

s = Solution()
grid = [
  ["0","0","0","0","0"],
  ["0","1","0","1","0"],
  ["0","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(s.numIslands(grid))