'''
1197. Minimum Knight Moves

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300
'''

# This is just do you know how to do BFS

from queue import Queue
import math

class Solution:
    def getDistance(self, x1: int, y1: int, x2: int, y2: int) -> float:
        return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
    
    def getMoves(self):
        return ([-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2])
    
    def minKnightMoves(self, x: int, y: int, move_count: int=0) -> int:
        x, y = abs(x), abs(y)
        q = Queue()
        v = set()
        
        q.put((0,0,0))
        while True:
            curX, curY, count = q.get()
            if curX == x and curY == y:
                return count
            
            bestMove, bestDistance = None, float("inf")
            for move in self.getMoves():
                if curX + move[0] < -4 or curY + move[1] < -4:
                    continue
                    
                if (curX + move[0], curY + move[1]) in v:
                    continue
                    
                v.add((curX + move[0], curY + move[1]))
                q.put((curX + move[0], curY + move[1], count + 1))
                
        