'''
Given two rectangles defined by their corners, return the area of the intersection.
'''

from typing import List

class Solution:
    def rectangleIntersection(self, rectangleOne: List[tuple], rectangleTwo: List[tuple]) -> int:
        # We need to first check to see if these rectangles overlap at all.
        topCorner = (min(rectangleOne[1][0], rectangleTwo[1][0]), min(rectangleOne[1][1], rectangleTwo[1][1]))
        bottomCorner = (max(rectangleOne[0][0], rectangleTwo[0][0]), max(rectangleOne[0][1], rectangleTwo[0][1]))

        print(bottomCorner,topCorner)
        returnArea = (topCorner[0] - bottomCorner[0]) * (topCorner[1] - bottomCorner[1])
        return max(returnArea, 0)

s = Solution()
print(s.rectangleIntersection([(0,0),(2,2)],[(1,1),(3,3)]))