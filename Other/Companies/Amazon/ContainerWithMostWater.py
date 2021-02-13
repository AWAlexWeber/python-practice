'''
Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''

from typing import List

class Solution:
    def maxArea(self, h: List[int]) -> int:
        i, j, c = 0, len(h) - 1, self.calcArea(h, 0, len(h) - 1)

        while i != j:
            c = max(c, self.calcArea(h, i, j))

            if h[i] < h[j]:
                i += 1
            else:
                j -= 1

        return c


    def calcArea(self, h: List[int], i: int, j: int) -> int:
        return min(h[i], h[j]) * (j - i)