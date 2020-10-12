'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Finding the first a[i] < a[i+1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i + 1]:
                # Found first a[i] < a[i+1]
                # Finding the next-greatest value above nums[i]
                n = nums[i]
                k, ki = math.inf, -1
                for j in range(i + 1, len(nums)):
                    if nums[j] > n and nums[j] <= k:
                        ki, k = j, nums[j]
                        
                # Found the next-greatest value
                # Swapping
                nums[i], nums[ki] = nums[ki], nums[i]
                
                # Swap complete
                # Reversing all elements between i + 1 and len(nums)
                remainLength = ((len(nums)) - (i + 1)) // 2
                c = 1
                for j in range(i + 1, i + remainLength + 1):
                    # Perform swap
                    nums[j], nums[len(nums) - c] = nums[len(nums) - c], nums[j]
                    c += 1
                return
        # If we made it this far, we never found a non-decreasing value
        c = 1
        for j in range(0, len(nums) // 2):
            # Perform swap
            nums[j], nums[len(nums) - c] = nums[len(nums) - c], nums[j]
            c += 1
        return
                        