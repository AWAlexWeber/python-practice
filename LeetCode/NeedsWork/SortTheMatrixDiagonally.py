'''
1329. Sort the Matrix Diagonally

Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
'''
from typing import List

# This is a fairly bad brute force solution
# It's not that horrific considering the question, but it could be approved if the arrays were sorted with radix sort 
class Solution:
    def fasterDiagonalSort(self, A):
        m, n = len(A), len(A[0])
        def sort(i, j):
            ij = zip(range(i, m), range(j, n))
            vals = iter(sorted(A[i][j] for i, j in ij))
            for i, j in ij:
                A[i][j] = next(vals)
        for i in range(m): sort(i, 0)
        for j in range(n): sort(0, j)
        return A

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Iterating across every diagonal

        # O(n) where n is the number of rows
        for r in range(0, len(mat[0]) - 1):
            c, ru, a = 0, r, []
            while c < len(mat) and ru < len(mat[0]):
                a.append(mat[c][ru])
                c, ru = c + 1, ru + 1

            # Sorting
            a.sort()
            c, ru, i = 0, r, 0
            print(a)

            while c < len(mat) and ru < len(mat[0]):
                mat[c][ru] = a[i]
                c, ru = c + 1, ru + 1
                i += 1

        # O(n) where n is the number of columns
        for c in range(1, len(mat) - 1):
            cu, r, a = c, 0, []
            while cu < len(mat) and r < len(mat[0]):
                a.append(mat[cu][r])
                cu, r = cu + 1, r + 1

            # Sorting
            a.sort()
            cu, r, i = c, 0, 0

            while cu < len(mat) and r < len(mat[0]):
                mat[cu][r] = a[i]
                cu, r = cu + 1, r + 1
                i += 1

        return mat

s = Solution()
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(s.fasterDiagonalSort(mat))
print(s.diagonalSort(mat))