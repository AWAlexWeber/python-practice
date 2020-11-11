'''
33. Search in Rotated Sorted Array

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 'Naive' solution. This is correct, but problem should specify restrictions on using this
        """
        # Finding pivot point and target
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
        """
        
        # Better solution using binary search to find the pivot, then binary search on the remaining half.
        
        # Helper inner function
        def find_pivot(l: int, r: int, nums: List[int]):
            if nums[l] < nums[r]:
                return 0
            
            while l <= r:
                p = (l + r) // 2
                if nums[p] > nums[p + 1]:
                    return p + 1
                else:
                    if nums[p] < nums[l]:
                        r = p - 1
                    else:
                        l = p + 1
                        
        # Secondary helper inner function
        def search(l: int, r: int, t: int, nums: List[int]):
            """
            Binary search
            """
            while l <= r:
                p = (l + r) // 2
                if nums[p] == t:
                    return p
                else:
                    if target < nums[p]:
                        r = p - 1
                    else:
                        l = p + 1
            return -1
        
        # Handling some base cases
        n = len(nums)
        
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1 
        
        # Finding the rotational idnex
        r = find_pivot(0, n - 1, nums)
        
        # if target is the smallest element
        if nums[r] == target:
            return r
        
        # if array is not rotated, search in the entire array
        if r == 0:
            return search(0, n - 1, target, nums)
        
        if target < nums[0]:
            # search on the right side
            return search(r, n - 1, target, nums)
        
        # search on the left side
        return search(0, r, target, nums)