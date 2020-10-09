'''
Binary search is a search algorithm usually used on a sorted sequence to quickly find an element with a given value. In this problem we will evaluate how binary search performs on data that isn't necessarily sorted. An element is said to be binary searchable if an element can be found provided the pivot is chosen everytime as the middle element - like in a regular binary search.
We need to find total number of elements which are binary searchable.

Example 1:

[2, 1, 3, 4, 6, 5] - 3 is searchable, 2 is searchable, 1 not searchable, 6 is searchable, 4 is seachable, 5 is not searchable 
Output: 4
Example 2:

Input: [1, 3, 2]
Output: 2
Explanation: 3 and 1 are searchable - you look for 3 - find it in the middle, look for 1 - you search the left half....search for 2, you look for it in the left half but didn't find.
'''

from typing import List
import math

def numBinarySearchable(nums: List[int]) -> int:
    # Need to perform binary search through all possible routes
    # Can either do this recursively/backtracking or with a BFS queue
    return canBinarySearch(nums, 0, len(nums), (len(nums) - 1) // 2, -math.inf, math.inf)

def canBinarySearch(nums: List[int], left: int, right: int, index: int, alpha: int, beta: int) -> int:
    #print(left,index,right,alpha,beta)
    # Alpha represents the minimal value this must be (must be greater than alpha) for when we search right
    # Beta represents the maximal value this must be (must be less than beta) for when we search left
    v = (1 if nums[index] > alpha and nums[index] < beta else 0)

    # If our dimensions is less than or equal to 1, we just return v
    if right - left <= 1:
        return v

    # Calculating new left point
    leftCenter = (index - left) // 2 + left
    rightCenter = (right - index) // 2 + index

    return v + canBinarySearch(nums, left, index, leftCenter, alpha, nums[index]) + canBinarySearch(nums, index, right, rightCenter, nums[index], beta)

print(numBinarySearchable([2, 3, 10, 40, 50, 8, 2, 3, 10, 40, 50]))