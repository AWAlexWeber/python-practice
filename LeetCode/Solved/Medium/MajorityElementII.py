'''
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
'''

from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Normal, O(n) time/space complexity
        v, o, h, l = set(), list(), defaultdict(lambda: 0), len(nums)
        for n in nums:
            h[n] += 1
            if h[n] > (l//3) and n not in v:
                o.append(n)
                v.add(n)
        return o