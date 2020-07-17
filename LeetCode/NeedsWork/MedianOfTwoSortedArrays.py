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

import math
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    ## Checking null cases
    if nums1 == None or nums2 == None:
        return -1

    if len(nums1) <= 0 and len(nums2) <= 0:
        return -1

    # Ensuring that our first array is the smallest one
    l1 = (nums1 if len(nums1) < len(nums2) else nums2)
    l2 = (nums2 if len(nums1) < len(nums2) else nums1)

    # Okay, we will now determine our length
    leftLen = int(( len(l1) + len(l2) + 1 ) / 2)

    aMin = 0
    aMax = len(l1)

    while (aMin < aMax):
        print(aMin)
        print(aMax)
        aCount = aMin + int((aMax - aMin) / 2)
        bCount = leftLen - aCount

        x = (l1[aCount - 1] if aCount > 0 else None)
        y = (l2[bCount - 1] if bCount > 0 else None)

        xP = (l1[aCount] if aCount < len(l1) else None)
        yP = (l2[bCount] if bCount < len(l2) else None)

        if x > yP:
            aMax = aCount - 1

        elif y > xP:
            aMin = aCount + 1

        else:
            leftHalfEnd = -1

            if x == None:
                leftHalfEnd = y
            elif y == None:
                leftHalfEnd = x
            else:
                leftHalfEnd = max(x,y)

            if len(l1) + len(l2) % 2 != 0:
                return leftHalfEnd

            rightHalfStart = -1

            if xP == None:
                rightHalfStart = yP
            elif yP == None:
                rightHalfStart = xP
            else:
                rightHalfStart = max(xP,yP)

            return leftHalfEnd + rightHalfStart / 2.0
            

f = findMedianSortedArrays([1,2,3], [0,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
print(f)

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