'''
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

# Read this https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46

import math
from typing import List

# This solution works by lineraly checking each point
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Defining our A and B
        A = (nums1 if len(nums1) >= len(nums2) else nums2)
        B = (nums2 if len(nums1) >= len(nums2) else nums1)
        
        # Defining our lengths
        lenTotal = len(A) + len(B)
        lenLeft = math.ceil(lenTotal/2)
        
        # Defining our minimums and maximums
        minIndex = lenLeft - len(B) - 1
        maxIndex = lenLeft - 1
        
        # Defining if we are odd or even
        # If odd, we are checking if the value AT the position is the median
        # This is done by checking which one is greater
        isOdd = (False if lenTotal % 2 == 0 else True)
        
        # Iterating on all possible values (this will be replaced, I am just verifying my logic)
        for i in range(minIndex, maxIndex + 1):
            # Getting the value at i
            vali = A[i]
            j = self.getBPosition(i, lenLeft)

            # Is this our final position?
            if(self.isValidMedian(i,j,A,B)):
                if isOdd:
                    val = 0
                    if i < 0:
                        val = B[j]
                    elif j < 0:
                        val = A[i]
                    else:
                        val = max(A[i], B[j])
                    return val
                else:
                    return self.getMedianValue(i,j,A,B)
        
    def getBPosition(self, i: int, l: int) -> int:
        return l - i - 2
    
    def isValidMedian(self, i: int, j: int, A: List[int], B: List[int]) -> bool:
        # We have a couple of checks to make here
        isOdd = (False if (len(A) + len(B)) % 2 == 0 else True)
        
        if isOdd:
            
            val = 0
            if i < 0:
                val = B[j]
            elif j < 0:
                val = A[i]
            else:
                val = max(A[i], B[j])
            
            if i + 1 < len(A) and val > A[i+1]:
                return False
            elif j + 1 < len(B) and val > B[j+1]:
                return False
            else:
                return True
        
        else:
            # Both values must pass our requirement
            # Meaning the value in B must be less than the value in A
            # And the value in A must be less than the value in B + 1

            if not j < 0 and i + 1 < len(A) and B[j] > A[i+1]:
                return False
            elif not i < 0 and j + 1 < len(B) and A[i] > B[j+1]:
                return False
            else:
                return True
            
            
    def getMedianValue(self, i: int, j: int, A: List[int], B: List[int]) -> float:
        # Determining the average
        # But from whom are we collecting the average?
        maxLeft = 0
        if i < 0:
            maxLeft = B[j]
        elif j < 0:
            maxLeft = A[i]
        else:
            maxLeft = max(A[i], B[j])

        checkA = (A[i+1] if i + 1 < len(A) else None)
        checkB = (B[j+1] if j + 1 < len(B) else None)

        minRight = 0
        if checkA != None and checkB != None:
            minRight = min(checkA, checkB)
        elif checkA != None:
            minRight = checkA
        elif checkB != None:
            minRight = checkB

        # Determining our value
        return (maxLeft + minRight) / 2
        
        
        
        
        
##### Explanation ######
# This is a pretty complicated one, so lets first make an example to work with
# Array A [1, 3, 5, 7, 9, 11, 13, 15, 17] len = 9
# Array B [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] len = 11

# We perform a binary search across both arrays simulatenously
# Remember that we need both arrays to be the same size, so when we search through one array remember to adjust in the other one

# Let's make some definitions
# Let i be an arbitrary position within array a
# Let j be an arbitrary position within array b
# Let La = i, and Ra = lenA - i - 1
# Let Lb = j, and Rb = lenB - j - 1
# Substitute in our known values
# La = i, Ra = 8 - i
# Lb = j, Rb = 10 - j

# We know that La + Lb = Ra + Rb
# i + j = 8 - i + 10 - j
# 2i + 2j = 18
# i + j = 9

# For example if i = 5 (ie no values in i) then j = 4

# The actual solution now will have us perform a binary search on A (the smallest one) using the index i
# Our comparator becomes if A[i] < B[J]

# Let's try another example
# Array A [5, 7, 8, 9, 15, 20, 50]
# Array B [0, 4, 12, 16, 25, 35, 45, 55, 65, 75, 85]

# LenA = 7
# LenB = 11
# Total = 18

# i + j = 7 - i + 11 - j
# 2i + 2j = 18
# i + j = 8
# j = 8 - i
# J has been solved for
# Now we perform our binary search on A since A is smaller, until we find A[i] < B[j] AND B[j-1] < A[i]
# If A[i] > B[j] we search left
# If B[j-1] > A[i] we search right
# When we have reached a final solution in our binary tree, if the tree total length is even our final answer is both answers / 2
# If we reach our final index in the search array but its not an answer, use the value in array B of j but - 1

# So our median becomes 16
# Which we can visually inspect as being true
# 0 4 5 7 8 9 12 15 16 20 25 35 45 50 55 65 75 85

# A = [1, 3, 8, 9, 15]
# B = [7, 11, 18, 19, 21, 25]

# 2i + 2j = 5 + 6 
# 2i + 2j = 11
# i + j = 5.5
# If our modifier is not a whole number, we are selecting a DIRECT value (not adding and / 2)

# j = 5 - i