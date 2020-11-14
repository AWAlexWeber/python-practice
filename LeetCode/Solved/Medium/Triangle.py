'''
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

import queue
from typing import List
from collections import defaultdict

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for y in range(len(triangle) - 2, -1, -1):
            left = triangle[y + 1][0]
            for x in range(y):
                triangle[y][x] += left if left < (right := triangle[y + 1][x + 1]) else right
                left = right
            triangle[y][y] += left if left < (right := triangle[y + 1][y + 1]) else right
        return triangle[0][0]
    
    def minimumTotalBFS(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return False
        
        # Classic BFS.
        q = queue.Queue()
        
        # Inserting our first level. (Depth, Index, Sum, direction)
        q.put((0, 0, triangle[0][0], ''))
        
        # Tracking our current depths so we don't keep going if our current sum isn't better.
        currentSums = defaultdict(lambda: defaultdict(lambda: float("inf")))
        
        # Calculating the minimum sum
        minSum = float("inf")
        totalDir = ''
        
        # Keeping track of our frontiner values, and which direction we took to get here
        
        while not q.empty():
            (i, d, s, dir) = q.get()
            
            # Wait, did someone find a better slot for us?
            # If so, we need to not keep going...

            # If we are at the maximum depth, check if our path here is better
            if d == len(triangle) - 1:
                if s < minSum:
                    minSum = s
                    totalDir = dir
                    
                
            # Otherwise, attempting to go left and right
            else:
                # Is this distance traveled worse then the pre-existing distance traveled?
                if s >= currentSums[d][i]:
                    continue
                
                if s + triangle[d + 1][i] < currentSums[d + 1][i]:
                    q.put((i, d + 1, s + triangle[d + 1][i], dir + 'L'))
                    currentSums[d + 1][i] = s + triangle[d + 1][i]
                if s + triangle[d + 1][i + 1] < currentSums[d + 1][i + 1]:
                    q.put((i + 1, d + 1, s + triangle[d + 1][i + 1], dir + 'R'))
                    currentSums[d + 1][i] = s + triangle[d + 1][i + 1]
                
        return minSum
