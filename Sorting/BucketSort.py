# Bucket sort is a sorting algorithm that does not function off of comparisons
# As with most sorting algorithms that are not comparison-based, it requires some assumptions about the dataset
# Primarily with bucketsort, is that the input dataset is across a specific range and uniformly distributed. We should also not be able to use counting sort (or we don't want to, but count sort can be better)
# IE: Sort a set of random numbers generated between 1 and 10 would be uniformly distributed across a known range

# If we know the range is from N to M and uniformly distributed across N and M
# We define an array of size M - N, and for all values from N to M at index I, we insert it at I - N

# Note that the underlying complexity relies a lot on the underlying sorting algorithm
# In this case we use the poor sorting algorithm insertion sort just to demonstrate the algorithm more easily

# Complexity
# Time                      # Space
# Ω(n+k)	Θ(n+k)	O(n^2)	O(n)

from typing import List
import random

# Internal insertion sort
def insertionSort(arr: List[int]): 
    for i in range(1, len(arr)): 
        j = i - 1
        while j >=0 and arr[j] > arr[i]:  
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = arr[i]      
    return arr
              
# Bucket sorting
def bucketSort(arr: List[int], l: int, r: int): 
    buckets = [None] * (r - l)
    for n in range(0, r - l):
        buckets[n] = list()
          
    # Inserting into bucket
    for j in arr: 
        index_b = int(j - l) 
        buckets[index_b].append(j)

    # Sorting
    for i in range(0, r - l):
        buckets[i] = insertionSort(buckets[i])

    c = 0
    for bucket in buckets:
        for i in bucket:
            arr[c] = i
            c = c + 1

# Creating our test data
a = [0] * 50
for n in range(0, 50):
    a[n] = (random.randrange(100, 1000) / 10)

#print(a)
bucketSort(a,10,100)
print(a)