''' Given a set of points, return the one that is the closest to the origin. '''

from heapq import heappush, heappop
from typing import List
import math

class Solution:
    def kClosestPoints(self, points: List[tuple], k: int):
        distance = list()
        def calcDistance(point: tuple) -> int:
            return math.sqrt(point[0]**2 + point[1]**2)

        for point in points:
            heappush(distance, (calcDistance(point), point))

        output = list()
        for i in range(k):
            output.append(heappop(distance)[1])
        
        return output

s = Solution()
print(s.kClosestPoints([(1,1),(5,5),(7,-9),(3,5),(12,15),(4,1),(3,7)], 3))

        
