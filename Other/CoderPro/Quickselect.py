'''
Find the kth largest/smallest number using only quickselect.
'''

from typing import List

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, k):
    k = len(arr) - k
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivotIndex = partition(arr, left, right)
        if pivotIndex == k:
            return arr[pivotIndex]
        elif pivotIndex > k:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1
    return -1

print(quickselect([1,2,5,6,2,7,9,0,1,3,4,6,1,3,7,2],5))