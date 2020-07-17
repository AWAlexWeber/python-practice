'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # We solve this problem by calculating a pairs target and storing it in the hash
        # The key ends up being the value that we are looking for, so if our num is in the hash we have a valid pair
        # IE If we have a target of 10 and a value of 8, we store 2 into the hash since its what we would need to finish the pair
        # Then if we find a 2, we return that result
        # O(n) time/space 
        hash = {}
        
        index = 0
        for num in nums:
            if hash.__contains__(num):
                return [hash[num], index]

            print(target-num)
            hash[target-num] = index

            index += 1

s = Solution()
print(s.twoSum([1,2,3,4,5,6,7,8,9,0], 6))