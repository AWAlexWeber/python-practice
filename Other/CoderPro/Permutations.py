''' 
#7
Given an array of random numbers, return all permutations.
[1,2,3] -> [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
'''

# Easiest approach may be to select one element from the list, remove it, then recurse inwards.
# Given that its permutation, our time complexity is already going to be n! so we don't need to worry about being super efficient here.

from typing import List

# Recursive, big space complexity. TODO: Replace with iterative solution.

class Solution():
    def permutations(self, nums: List[int]) -> List[List[int]]:
        self.finalOutput = list()
        self.recursePermutate([], nums)
        return self.finalOutput

    def recursePermutate(self, output: List[int], nums: List[int]):
        # Handling base case; our nums is empty
        if len(nums) <= 0:
            self.finalOutput.append(output)
            return

        # This function should, for every value in nums, attempt to add it to output and then go one deeper. Note we will have to make a copy.
        for index, value in enumerate(nums):
            newOutput = output[:]
            newNums = nums[:]

            newNums.pop(index)
            newOutput.append(value)

            self.recursePermutate(newOutput, newNums)

s = Solution()
print(s.permutations([1,2,3]))