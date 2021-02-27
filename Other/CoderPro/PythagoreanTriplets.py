'''
Find pythagorean triplets.
'''

from typing import List
from collections import defaultdict

class Solution:
    # 'Better' Brute-Force O(n^2).
    def findPyTrip(self, nums: List[int]) -> List[tuple]:
        # First approach we're going to take is O(n^2).
        # Essentially it's just two-sum but for three.
        t = defaultdict(lambda: list())
        for i in range(len(nums)):
            for j in range(len(nums)):
                c = nums[i]**2 + nums[j]**2
                t[c].append((i,j))

        o = list()
        visit = set()
        for k in range(len(nums)):
            if nums[k]**2 in t:
                for c in t[nums[k]**2]:
                    if c[0] != k and c[1] != k:
                        visit_data = sorted([nums[c[0]], nums[c[1]], nums[k]])
                        if str(visit_data) not in visit:
                            o.append(visit_data)
                            visit.add(str(visit_data))
        
        return o

s = Solution()
print(s.findPyTrip([3,5,12,5,13]))