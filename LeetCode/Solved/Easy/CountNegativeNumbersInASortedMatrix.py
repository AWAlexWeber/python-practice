'''
1351. Count Negative Numbers in a Sorted Matrix

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
'''

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        for r in grid:
            for c in r:
                if int(c) > 0:
                    print("",end=" ")
                print(c,end="   ")
            print("")

        return self.visit(grid, len(grid) - 1, len(grid[0]) - 1, 0)
        
    def visit(self, grid: List[List[int]], r: int, c: int, d: int) -> int:
        # Getting current square
        val = 1 if grid[r][c] < 0 else 0
        
        # Visiting left if r - 1 is >= 0
        up = (self.visit(grid, r - 1, c, -1) if r - 1 >= 0 and val and d <= 0 else 0)
        
        # Visiting up if c - 1 is >= 0
        left = (self.visit(grid, r, c - 1, 1) if c - 1 >= 0 and val and d >= 0 else 0)

        # Visiting the diagonal
        diag = (self.visit(grid, r - 1, c - 1, 0) if c - 1 >= 0 and r - 1 >= 0 and val and d == 0 else 0)
        
        # Returning
        #print("Visiting " + str(r) + "," + str(c) + " val of " + str(val) + " (" + str(grid[r][c]) +") ")
        return val + left + up + diag

# A faster solution uses binary search in each row to find the index where it becomes negative
# As it is sorted, every index afterwards must be negative
class SolutionFaster(object):
    def countNegatives(self, grid):
        def bin(row):
            start, end = 0, len(row)
            while start<end:
                mid = start +(end -start) // 2
                if row[mid]<0:
                    end = mid
                else:
                    start = mid+1
            return len(row)- start
        
        count = 0
        for row in grid:
            count += bin(row)
        return(count)

s = Solution()
s.countNegatives([[5,1,0],[-5,-5,-5]])