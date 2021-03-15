'''
Given a grid of colors, find the size of the largset connected component.
'''

from typing import List
from queue import Queue

class Solution:
    def maxSize(self, arr: List[List[int]], color: int) -> int:
        visit = set()
        maxSize = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if (i,j) in visit:
                    continue

                if arr[i][j] != color:
                    continue

                else:
                    # Attempting to traverse
                    maxSize = max(maxSize, self.maxSizeAtIndex(arr, i, j, visit))

        return maxSize


    def maxSizeAtIndex(self, arr: List[List[int]], x: int, y: int, visit: set) -> int:
        q = Queue()
        currentMaxSize = 1
        q.put((x, y, 1))
        visit.add((x, y))

        while not q.empty():
            i, j, size = (q.get())

            for nextIndexI in [-1, 0, 1]:
                for nextIndexJ in [-1, 0, 1]:
                    if self.canVisit(arr, i + nextIndexI, j + nextIndexJ, arr[i][j], visit):
                        q.put((i + nextIndexI, j + nextIndexJ, size + 1))
                        visit.add((i + nextIndexI, j + nextIndexJ))
                        currentMaxSize += 1

        return currentMaxSize
            

    def canVisit(self, arr: List[List[int]], i: int, j: int, color: int, visit: set) -> bool:
        if i >= len(arr) or j >= len(arr[0]) or i < 0 or j < 0:
            return False
        if arr[i][j] != color:
            return False
        if (i,j) in visit:
            return False
        return True

s = Solution()
arr = [
    [0,1,0,1,1,1,1],
    [1,1,1,1,1,1,1]
]
print(s.maxSize(arr, 1))