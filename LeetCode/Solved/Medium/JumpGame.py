'''
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
'''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return True
        
        # DP approach?
        # Do DFS, save every output into hash of the index.
        # Try all numbers in descending order.
        m = {}
        self.jumpDeeper(0, nums, m)
        return m[0]
        
    def jumpDeeper(self, index: int, nums: List[int], m:dict={}) -> bool:
        # Handling DP
        if index in m:
            return m[index]
        
        # Is this the end
        if index == len(nums) - 1:
            return True
        
        if index >= len(nums):
            return False
        
        # Starting at the highest value, going downwards to -> 1
        for j in range(nums[index], 0, -1):
            jo = index + j
            m[jo] = self.jumpDeeper(jo, nums, m)
            if m[jo]:
                m[index] = True
                return True
            
        m[index] = False
        return False
    
    # Kadane's algorithm solution, very interesting
    def canJumpDeeper(self, nums):
        m, i, l = 0, 0, len(nums)
        while i <= m:
            
            m = max(m, i+nums[i])
            if(m >= l-1):
                return True
            i += 1
            
        return False
    