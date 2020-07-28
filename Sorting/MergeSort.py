# Merge sort is a divide and conquer algorithm that functions by dividing an array in two, and sorting those components, then merging them back
# Its better than quicksort since it has a better lower bound, but it is not in place
# Additionally, its constant is larger than quicksort
## Best ## Avrg ## Wrst ## Spce ##
## nlogn # nlogn # nlogn # n ##

from typing import List

# This is my sort implementation made in a couple of minutes
def mergesort(arr: List[int], start: int, end: int) -> List[int]:
    # Checking if our size is 1 or zero
    if end - start == 0:
        return []
    elif end - start == 1:
        return [arr[start]]

    # Essentially we take the left side of this and right side and merge them together
    # Calculating the midpoint
    middle = int((end-start) / 2 + start)
    left = mergesort(arr, start, middle)
    right = mergesort(arr, middle, end)

    # Combining the two arrays
    out = []
    i = j = 0
    while i < len(left) or j < len(right):

        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1

        elif i < len(left):
            out.append(left[i])
            i += 1

        elif j < len(right):
            out.append(right[j])
            j += 1

    return out

# Slightly more efficient solution
def betterMergeSort(arr: List[int]): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        betterMergeSort(L) # Sorting the first half 
        betterMergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

a = [1,5,2,9,3,7,8,4,10,125]
betterMergeSort(a)
print(a)
a = [1,5,2,9,3,7,8,4,10,125]
print(mergesort(a,0,len(a)))

# 1 5 2 9 3 7 8 4 10 125