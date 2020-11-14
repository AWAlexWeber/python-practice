'''
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

from typing import List

# Slow
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permuteList = list()
        self.permutateAll([], nums)
        return self.permuteList
        
    def permutateAll(self, prev: List[int], nums: List[int]):
        if len(nums) == 0:
            self.permuteList.append(prev)
            return
        
        for i in range(len(nums)):
            o = prev.copy()
            o.append(nums[i])
            f = nums.copy()
            f.pop(i)
            self.permutateAll(o, f)

# Faster
class FastSolution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output