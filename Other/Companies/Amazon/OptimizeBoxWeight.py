'''
An Amazon Fulfillment Associate has a set of items that need to be packed into two boxes. Given an integer array of the item weights (arr) to be packed, divide the item weights into two subsets, A and B, for packing into the associated boxes, while respecting the following conditions:
The intersection of A and B is null.
The union A and B is equal to the original array.
The number of elements in subset Ais minimal.
The sum of A's weights is greater than the sum of B's weights.
Return the subset A in increasing order where the sum of A's weights is greater than the sum of B's weights. If more than one subset A exists, return the one with the maximal total weight.

Input Format For Custom Testing
STDIN   Function
6 -> arr[] size n = 6
5 -> arr[] = [5, 3, 2, 4, 1, 2]
3
2
4
1
2

Sample Output
4
5

Explanation
n = 6
arr = [5, 3, 2, 4, 1, 2]
The subset of A that satisfies the conditions is [4, 5]
A is minimal (size 2)
Sum(A) = (4 + 5) = 9 > Sum(B) = (1 + 2 + 2 + 3) = 8
The intersection of A and B is null and their union is equal to arr.
The subset A with the maximal sum is [4, 5].
'''

from typing import List

class Solution():
    def optimizeBoxWeight(self, nums: List[int]) -> List[int]:
        # Basic approach is to sort this, then sum up all elements. We have the sumA = 0, and add the far right value until sumA > sumB
        sumA, sumB, i = 0, sum(nums), len(nums) - 1
        nums.sort()
        while sumA <= sumB:
            sumB -= nums[i]
            sumA += nums[i]
            i -= 1
        return nums[i + 1:]

s = Solution()
print(s.optimizeBoxWeight([4,1,5,2,3,1,2]))
