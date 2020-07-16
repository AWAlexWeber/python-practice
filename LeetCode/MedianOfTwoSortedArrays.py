from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # Pre-calculating length
    t = len(nums1) + len(nums2)

    # Moving in nums1 while value in nums1 is less than the value in nums2 at index
    l = 0
    r = 0

    lend = False
    rend = False

    # We need to move until we've reached the midway point
    while l + r < t / 2 - 1:

        print(l,r)

        if nums1[l] < nums2[r]:
            if l + 1< len(nums1):
                l+=1
            else:
                r+=1
                lend = True
        else:
            if r + 1 < len(nums2):
                r += 1
            else:
                l += 1
                rend = True

    if lend:
        return nums2[r]

    if rend:
        return nums1[l]

    if t % 2 == 0:
        return (nums1[l] + nums2[r]) / 2

    if nums1[l] < nums2[r]:
        return nums1[l]

    return nums2[r]

#print(findMedianSortedArrays(nums1=[1,2], nums2=[3,4]))
print(findMedianSortedArrays(nums1=[1, 3, 5, 9, 11, 13, 13, 13, 13, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], nums2=[7]))

# [1, 3, 5, 9, 11, 13]
# [7]

# l = 0
# r = 0
# while l + r < 7 / 2 = 3

# l = 3
# r = 0
