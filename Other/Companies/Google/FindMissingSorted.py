'''
Given a sorted array that contains n numbers out of which except one value all the other values are repeated twice. Find the number in the array that occurs only once.
Do it with constant space and logn time.
'''

from typing import List
import random

class Solution:
    def findMissingDigit(self, nums: List[int]) -> int:
        # Attempts this by using binary search and the length of the subset to determine where the number is
        # We start in the center
        return self.binarySearch(nums, 0, len(nums), len(nums) // 2)

    def binarySearch(self, nums: List[int], left: int, right: int, center: int):
        # Attempts binary search until we find the correct value
        # First checking if this is the correct value
        centerLeftValue = (nums[center - 1] if center >= 1 else None)
        centerRightValue = (nums[center + 1] if center < len(nums) - 1 else None)

        if not (centerLeftValue == nums[center] and not centerLeftValue == None) and not (centerRightValue == nums[center] and not centerRightValue == None):
            return nums[center]

        elif right - left <= 1:
            return nums[left]

        else:
            # Checking what range to check.
            # First we need to find our pair value. It is going to be either to the left or the right
            centerLeft, centerRight = center, center
            if nums != 1 and nums[center - 1] == nums[center]:
                centerLeft = center - 1
            else:
                centerRight = center + 1

            # Oaky, we know the indexes of the two digits for the value we're currently sitting on.
            # What we want to do next is determine if we should go left or right
            # We do this by comparing remaining sizes between (left, centerLeft) and (centerRight, right).
            # One of those will be odd. Whichever one is odd, we go to the center of and perform another binary search
            widthLeft = centerLeft - left
            widthRight = right - centerRight - 1

            if widthLeft % 2 != 0:
                # Going left
                # Calculating our new center
                newCenter = left + ( center - left) // 2
                return self.binarySearch(nums, left, centerLeft, newCenter)

            elif widthRight % 2 != 0:
                # Going right
                # Calculating our new center
                newCenter = centerRight + 1 + ( center - left) // 2
                return self.binarySearch(nums, centerRight + 1, right, newCenter)

            else:
                print("Array dimensions are invalid.")
                return -1

        pass

d = list()
for x in range(0,50000):
    d.append(random.randrange(0,100))

print(d)
exit

s = Solution()
# Popping a random index
for i in range(100):
    # Generating random solutions
    data = list()
    for i in range(0,50):
        data.append(i)
        data.append(i)


    ans = data.pop(random.randint(0,50))
    if(ans != s.findMissingDigit(data)):
        print("INVALID", data)
        break

