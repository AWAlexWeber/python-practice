'''
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        currentMax = self.calcArea(height,l,r)

        while l != r:
            currentMax = max(currentMax, self.calcArea(height, l, r))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return currentMax


    def calcArea(self, height: List[int], l: int, r: int) -> int:
        maxHeight = min(height[l], height[r])
        return maxHeight * (r - l)



s = Solution()
print(s.maxArea([1,3,2,5,25,24,5]))
#print(s.maxArea([2,3,4,5,18,17,6]))
#print(s.maxArea([1,2,3,4,5,11,11,1,2,1,2,4,5,3]))
print(s.maxArea([1,8,6,2,5,4,8,3,7]))