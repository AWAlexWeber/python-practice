# Selection sort 'selects' the smallest value, then swaps it with the value at i
# i moves from left to right

# This is the most classic sort that people work on, and it has O(n^2) time complexity on average. It does have a best case of O(n) if everything is already sorted

from typing import List

def selectionSort(arr: List[int]):

    i = 0
    while i < len(arr) - 1:
        j = i + 1
        minv = arr[i]
        mini = i
        while j < len(arr):
            if arr[j] < minv:
                minv = arr[j]
                mini = j
            j += 1
        arr[i], arr[mini] = arr[mini], arr[i]
        i = i + 1

l = [5,2,7,8,1,3,8,9,0,2,4,5,2,1,6,3,7,2,2]
print(l)
selectionSort(l)
print(l)