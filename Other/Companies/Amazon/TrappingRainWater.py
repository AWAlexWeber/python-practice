'''
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
'''

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        i, j, f = 0, len(height) - 1, 0

        im = jm = 0

        while i < j:
            if height[i] < height[j]:
                if height[i] >= im:
                    im = height[i]
                else:
                    f += im - height[i]

                i += 1
                
            else:
                if height[j] > jm:
                    jm = height[j]
                else:
                    f += jm - height[j]

                j -= 1

        return f

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))