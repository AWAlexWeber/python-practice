'''
1512. Number of Good Pairs

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''


from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    match = {}
    out = 0

    # O(n)
    for i in nums:
        match[i] = match.setdefault(i, 0) + 1

        if match[i] > 1:
            out += match[i] - 1

    return out

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = {}
        o = 0
        for n in nums:
            h[n] = (h[n] + 1 if n in h else 0)
            o += h[n]
        
        return o

s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))