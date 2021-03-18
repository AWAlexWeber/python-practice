'''
Given a maze, where you start from the top left and go to the bottom right, how many paths are there through the maze such that you do not visit the same spot twice.
'''

from typing import List

class Solution:
    def numPaths(self, maze: List[List[int]]) -> int:
        # Basic DFS with backtracking.
        # We will also keep track of the total number of paths from any given index to allow memoization
        memo = {}
        if maze[-1][-1] == 1:
            return 0
        if maze[0][0] == 1:
            return 0
        
        memo[(len(maze) - 1, len(maze[0]) - 1)] = 1

        def canMove(i: int, j: int, moveX: int, moveY: int, maze: List[List[int]], visit: set) -> bool:
            if i + moveX < 0 or j + moveY < 0 or i + moveX >= len(maze) or j + moveY >= len(maze[0]):
                return False
            if (i + moveX, j + moveY) in visit:
                return False
            if (moveX == -1 and moveY == -1) or (moveX == 1 and moveY == 1) or (moveX == -1 and moveY == 1) or (moveX == 1 and moveY == -1):
                # Preventing diagonal movement.
                return False
            if maze[i + moveX][j + moveY] != 0:
                return False
            return True

        def dfs(maze: List[List[int]], memo: dict, visit: set, i: int, j: int) -> int:
            visit.add((i,j))
            if (i,j) in memo:
                visit.remove((i,j))
                return memo[(i,j)]
            else:
                # Attempting to move in all possible directions that we have not visited already.
                movements = [0,1]
                movementsAllowed = 0
                for moveX in movements:
                    for moveY in movements:
                        if canMove(i, j, moveX, moveY, maze, visit):
                            movementsAllowed += dfs(maze, memo, visit, i + moveX, j + moveY)

                visit.remove((i,j))
                memo[(i,j)] = movementsAllowed
                return movementsAllowed

        return dfs(maze, memo, set(), 0, 0)

s = Solution()
arr = [[0, 1, 0],[0, 0, 1],[0, 0, 0]]
print(s.numPaths([[0,0,0],[0,0,0]]))
arr = [[0, 1, 0],[0, 0, 1],[0, 0, 0]]
print(s.numPaths(arr))