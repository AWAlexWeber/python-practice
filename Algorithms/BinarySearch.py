from typing import List
import math

# Binary search
# @param left: Left-most index we are searching in right now
# @param right: Right-most index we are searching in right now
# @param index: current central index
# @param list: List we are searching through
# @param target: The target value

def binarySearch(left: [int], right: [int], index: [int], list: [List], target: [int]) -> int:

    print(left,index,right)

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
binarySearch(0, len(l), int(len(l)/2), l, 15)