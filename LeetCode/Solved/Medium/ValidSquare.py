'''
593. Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
'''

from typing import List

import math
from collections import defaultdict
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Distance between p1 p2, p1 p3, p3, p4 must all be equal
        def dist_eq(p: List[int], d: List[int]):
            return math.sqrt(pow(d[0] - p[0], 2) + pow(d[1] - p[1], 2))
        h = defaultdict(lambda: 0)
        
        par, p = None, [p1, p2, p3, p4]
        for pa in p:
            for pb in p:
                if pa == pb:
                    continue
                # Checking for equality
                h[dist_eq(pa,pb)] += 1
        
        # There needs to be 8 / 4 occurences. Anything else is invalid
        l = list(h.keys())
        return len(l) == 2 and (h[l[0]] == 4 and h[l[1]] == 8 or h[l[1]] == 4 and h[l[0]] == 8)