# Bubble sort is a terrible sorting algorithm that functions by iterating until the array is sorted
# Whenever you have two values that aren't sorted, it swaps them

# Bubblesort has some advantages; namely it has a best case of N and a space of 1. These are largely irrelevant most of the time

from typing import List

## Best ## Avrg ## Wrst ## Spce ##
## n     # n^2   # n^2 #  1   ##

def bubbleSort(arr: List[int]):
    isSort = False
    while not isSort:
        isSort = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                isSort = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

a = [5,2,6,8,9,0,1,3,4]
bubbleSort(a)
print(a)