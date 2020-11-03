'''
505. The Maze II

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''

from typing import List
import queue

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # BFS using visisted set
        q = queue.Queue()
        
        q.put((start[0],start[1],0))
        visit = {}
        visit[start[0],start[1]] = 0
        
        min_depth = float("inf")
        did_visit = False
        
        while not q.empty():
            # Checking if this is the destination
            (x, y, depth) = q.get()
            
            # As it is BFS we can assume depth is the best depth possible
            if x == destination[0] and y == destination[1]:
                min_depth = min(min_depth, depth)
                did_visit = True
                continue
            
            # Getting all the possible positions to the left, right, up and down
            x_l = x
            while x_l > 0 and maze[x_l - 1][y] != 1:
                x_l -= 1
            x_r = x
            while x_r < len(maze) - 1 and maze[x_r  + 1][y] != 1:
                x_r += 1
            y_u = y
            while y_u > 0 and maze[x][y_u - 1] != 1:
                y_u -= 1
            y_d = y
            while y_d < len(maze[0]) - 1 and maze[x][y_d + 1] != 1:
                y_d += 1
            
                
            # Checking if these positions are in our visisted set, if they are do not add them
            if (x_l,y) not in visit or visit[(x_l,y)] > depth + abs(x - x_l):
                visit[(x_l,y)] = depth + abs(x - x_l)
                #print(0,x_l,y)
                q.put((x_l,y,depth + abs(x - x_l)))
                
            if (x_r,y) not in visit or visit[(x_r,y)] > depth + abs(x - x_r):
                visit[(x_r,y)] = depth + abs(x - x_r)
                #print(1,x_r,y)
                q.put((x_r,y,depth + abs(x - x_r)))
                
            if (x,y_u) not in visit or visit[(x,y_u)] > depth + abs(y - y_u):
                visit[(x,y_u)] = depth + abs(y - y_u)
                #print(2,x,y_u)
                q.put((x,y_u,depth + abs(y - y_u)))
                
            if (x,y_d) not in visit or visit[(x,y_d)] > depth + abs(y - y_d):
                visit[(x,y_d)] = depth + abs(y - y_d)
                #print(3,x,y_d)
                q.put((x,y_d,depth + abs(y - y_d)))
                
        if did_visit:
            return min_depth
        else:
            return -1