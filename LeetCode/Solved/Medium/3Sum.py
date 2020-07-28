'''
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

from typing import List

class Solution:
    def badThreeSum(self, nums: List[int]) -> List[List[int]]:
        # Edge case
        if len(nums) <= 2:
            return []

        # First we sort our output
        # Given the default implementation, this has a worse case runtime of O(n^2)
        # We already need to do this, so all this does is increase our constant
        nums = sorted(nums)

        h = {}

        # O(n^2) to build our tuplet set
        for i in range(0, len(nums)-1):
            for j in range(i+1,len(nums)):
                v = nums[i] + nums[j]
                if v in h:
                    h[v].append([i,j])
                else:
                    h[v] = [[i,j]]

        out = []
        unique = set()

        # Iterating over every value again
        # O(n)
        for i in range(0, len(nums)-1):
            v = -nums[i]
            if v in h:
                for a in h[v]:
                    if i not in a:
                        u = sorted([nums[i], nums[a[0]], nums[a[1]]])
                        if str(u) not in unique:
                            out.append(u)
                            unique.add(str(u))
        
        return out

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The idea is that we create a system where we incrementally check every value between nums[i] and the end
        nums.sort()
        N, result = len(nums), []

        for i in range(N):
            # Skipping duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Tracking positions
            j, k = i + 1, N - 1
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1

                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1

        return result



s = Solution()
print(s.threeSum([-2,0,1,1,2]))