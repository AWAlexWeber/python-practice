'''
Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

Examples
Example 1:
Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47

2 + 45 = 47

Example 2:
Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2

Example 3:
Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.
'''

from typing import List

class Solution():
    def twoSumUnique(self, nums: List[int], target: int) -> int:
        # We will use a set to track already visisted pairs.
        # We will use a sorted variant of nums to use two pointers
        nums.sort()
        i, q = 0, len(nums) - 1
        visit = set()
        while i < q:
            if nums[i] + nums[q] == target:
                if (nums[i],nums[q]) not in visit:
                    visit.add((nums[i],nums[q]))
                i, q = i + 1, q - 1
            elif nums[i] + nums[q] < target:
                i += 1
            else:
                q -= 1
        return len(visit)

    def twoSumUniqueImproved(self, nums: List[int], target: int) -> int:
        # Better solution that does not use a sort, O(n) time and O(n) space
        seen = set()
        complement = set()
        for num in nums:
            if target - num in complement:
                pair = (num, target - num) if num < target - num else (target - num, num)
                seen.add(pair)
            complement.add(num)
        return len(seen)

s = Solution()
print(s.twoSumUnique([1,1,2,45,46,46], 47))
print(s.twoSumUniqueImproved([1,1,2,45,46,46], 47))