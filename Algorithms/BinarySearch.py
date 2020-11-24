from typing import List
import math

# Binary search
# @param left: Left-most index we are searching in right now
# @param right: Right-most index we are searching in right now
# @param index: current central index
# @param list: List we are searching through
# @param target: The target value

def binarySearch(left: [int], right: [int], index: [int], list: [List], target: [int]) -> int:

    #print(left,index,right)

    if list[index] == target:
        return index
    elif list[index] < target:
        return binarySearch(index, right, int(index + (right - index)/2), list, target)
    else:
        return binarySearch(left, index, int( (index - left)/2 + left ), list, target)

    # 0 - 12 - 24
    # If its left, we become
    # 0 - 6 - 12
    # If its right we become
    # 6 - 9 - 12

# Binary search attempts to find something over a sorted datastructure by moving left or right depending on how close we are
# We assume an input of a sorted array
# The above is a recursive solution
l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
for n in l:
    o = binarySearch(0, len(l), int(len(l)/2), l, n)
    #print(o)

# Rebuilding binary search
def binarySearchTwo(nums: List[int], value: int, left: int, center: int, right: int) -> int:
    # Checking to see if we've reached our number
    if nums[center] == value:
        return center

    # Checking if our dimension is too small and we haven't found anything yet
    if (right - left) <= 1:
        return -1

    # Otherwise, going left or right depending on the number difference
    if nums[center] > value:
        # Going left
        newCenter = left + (center - left) // 2
        return binarySearchTwo(nums, value, left, newCenter, center)

    elif nums[center] < value:
        # Going right
        newCenter = center + (right - center) // 2
        return binarySearchTwo(nums, value, center, newCenter, right)

# Building a large random list
import random
runs = 1000
size = 50
for i in range(runs):
    testList = list()
    targetNumber = None
    randomSet = set()
    for x in range(size):
        rValue = random.randint(0,size)
        while rValue in randomSet:
            rValue = random.randint(0,size)
        randomSet.add(rValue)
        testList.append(rValue)
    testList = sorted(testList)

    # Selecting a random value
    randomIndex = random.randint(0,len(testList) - 1)
    randomValue = testList[randomIndex]

    if randomIndex != binarySearchTwo(testList, randomValue, 0, len(testList) // 2, len(testList)):
        print("ERROR")
        print(randomIndex, randomValue, binarySearchTwo(testList, randomValue, 0, len(testList) // 2, len(testList)))
        print(testList)