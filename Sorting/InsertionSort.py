# Insertion sort is an algorithm that functions by iterating from 0 to n where n is the size of the input dataset
# For every iteration of i from 0 to n, we then swap from i to 0 given a situation where the variable is swappable

## Best ## Avrg ## Wrst ## Spce ##
## n     # n^2   # n^2   #  1   ##

# Insertion sort is still bad, but it is stable and has a best case time complexity of n and a space complexity of 1

from typing import List

def insertionSort(arr: List[int]):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

a = [5,2,7,9,0,1,3,4,2,15,25,35]
insertionSort(a)
print(a)