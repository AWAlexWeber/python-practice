'''
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
'''

from typing import List

# This answer is very bad; should really just use numpy
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Base cases that create some weird issues
        
        # Creating the matrix
        # This would be better with numpy
        matrix = list()
        for i in range(n):
            matrix.append([0] * n)
            
        # We have four movements that are required to be made
        # We must go right, down, left, up
        currentX, currentY = 0, 0
        xMax, yMax, xMin, yMin = n - 1, n - 1, 0, 0
        mode = "RIGHT"
        
        i = 1
        while True:
            # Did we hit the center?
            if currentX == n // 2 and currentY == n // 2:
                break
                
            # Did we hit the center on an even set?
            if n % 2 == 0 and (currentX == (n // 2) - 1 and currentY == (n // 2) - 1):
                break
            
            while mode == "RIGHT":
                # Check if we reached our limit
                if self.hitLimit(currentX, currentY, xMax, yMax, xMin, yMin):
                    mode = "DOWN"
                    continue
                else:
                    #print("RIGHT")
                    # Did not hit our limit yet
                    matrix[currentX][currentY] = i
                    currentX += 1
                    i += 1
                    
            currentX -= 1
            i -= 1
                    
            while mode == "DOWN":
                if self.hitLimit(currentX, currentY, xMax, yMax, xMin, yMin):
                    mode = "LEFT"
                    continue
                else:
                    #print("DOWN")
                    matrix[currentX][currentY] = i
                    currentY += 1
                    i += 1
                    
            currentY -= 1
            i -= 1
            
            while mode == "LEFT":
                if self.hitLimit(currentX, currentY, xMax, yMax, xMin, yMin):
                    mode = "UP"
                    continue
                else:
                    #print("LEFT")
                    matrix[currentX][currentY] = i
                    currentX -= 1
                    i += 1
                    
            currentX += 1
            i -= 1
            
            while mode == "UP":
                if self.hitLimit(currentX, currentY, xMax, yMax, xMin, yMin + 1):
                    mode = "RIGHT"
                    continue
                else:
                    #print("UP")
                    matrix[currentX][currentY] = i
                    currentY -= 1
                    i += 1
                
            currentY += 1
                    
            # Moving our range inwards
            currentX += 1
            xMax -= 1
            yMax -= 1
            xMin += 1
            yMin += 1
            
        # Checking if we need to fill in the remaining bit
        if n % 2 == 0:
            matrix[currentX][currentY] = i
            matrix[currentX + 1][currentY] = i + 1
            matrix[currentX + 1][currentY + 1] = i + 2
            matrix[currentX][currentY + 1] = i + 3
            
            
        matrix[currentX][currentY] = i
        
        # Flipping the matrix
        outputMatrix = list()
        
        for i in range(n):
            newRow = list()
            for y in range(n):
                newRow.append(matrix[y][i])
            outputMatrix.append(newRow)
        return outputMatrix
                    
    
    # Helper function for checking when we've hit a boundary
    def hitLimit(self, cX: int, cY: int, xMax: int, yMax: int, xMin: int, yMin: int) -> bool:
        if cX < xMin or cX > xMax:
            return True
        
        if cY < yMin or cY > yMax:
            return True
        
        return False