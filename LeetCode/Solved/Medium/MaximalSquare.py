'''
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

from typing import List
# This needs to be improved via DP

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Finding our first occurence of a 1, expanding it while we can
        maxArea = 0
        
        # This approach works because we will always find the top left corner first
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    maxArea = max(self.expandSquare(i, j, matrix), maxArea)
                    #print("MA:",maxArea)
        return maxArea
            
    def expandSquare(self, i: int, j: int, matrix: List[List[str]]) -> int:
        #print("S:",i,j)
        # Expanding the square in the -> and \/ direction.
        
        # Marking this square as 'visited' by setting it to 0. Keeps as at O(n)
        matrix[i][j] = "0"
        
        width, height = 1, 1
        
        # Expanding across all three directions
        while True:
            # Are we too wide?
            if i + width >= len(matrix) or j + height >= len(matrix[0]):
                return width * height
            
            # Expanding on the bottom.
            #print("Bottom")
            for w in range(j, j + height):
                #print(i+width,w)
                if matrix[i + width][w] == "0":
                    return width * height
                #matrix[i + width][w] = "0"

            # Expanding on the right.
            #print("Right")
            for h in range(i, i + width):
                #print(h,j+height)
                if matrix[h][j + height] == "0":
                    return width * height
                #matrix[h][j + height] = "0"

            # Expanding on the diagonal.
            if matrix[i + width][j + height] == "0":
                return width * height
            
            width, height = width + 1, height + 1
            
        return width * height