# A heap is a special datastructure, similar to a tree
# It is a complete binary tree, each node is smaller (or bigger) than the parent node
# ie [1,2,3,4,5,6,7,8,9]

# As a minheap would look like

#           1
#      2         3
#   4     5    6    7
# 8   9

# Note that any ordering is fine for the above minheap, as long as the values below are bigger
# A heap is a great way to maintain access to a specific value (in this case, the minimal value)
# During the heap process, we 'sort' each node by swapping it with the smallest if it is infact bigger

# A general implementation of a heap uses an array, where
# arr[i] = parent
# arr[i*2 + 1] = left node
# arr[i*2 + 2] = right node
# (this is for most trees)

# One of the really powerful parts of a heap is that building it is O(n)
# This is really fantastic if we have a predefined dataset

from typing import List
import random

def heapify(arr: List[int], i: int, length: int):
    max, l, r = i, (i * 2) + 1, (i * 2) + 2

    if l < length and arr[l] > arr[max]:
        max = l

    if r < length and arr[r] > arr[max]:
        max = r

    # Heapify if we have bigger children
    if not max == i:
        arr[i], arr[max] = arr[max], arr[i]
        heapify(arr, i, length)


# Creating our test data
a = [0] * 10
for n in range(0, 10):
    a[n] = random.randrange(0, 20)

for i in range(len(a)//2, 1, -1):
    heapify(a, i, len(a))

print(a)