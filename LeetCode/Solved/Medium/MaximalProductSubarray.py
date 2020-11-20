'''
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Going to segment by zeros
        return max(self.findMax(nums), self.findMax(nums[::-1]))
    
    def findMax(self, nums: List[int]) -> int:
        maximalProduct = float("-inf")
        currentProduct = 1

        for i, n in enumerate(nums):
            # Increasing our current product by n.
            currentProduct *= n
            
            # Taking a look at the maximal product.
            maximalProduct = max(maximalProduct, currentProduct)
            
            if n == 0:
                j = i - 1
                backwardsMaximal = 1
                while j >= 0 and nums[j] != 0:
                    backwardsMaximal *= nums[j]
                    maximalProduct = max(maximalProduct, currentProduct)
                    j -= 1
                    
                # Resetting
                currentProduct = 1
        
        return maximalProduct