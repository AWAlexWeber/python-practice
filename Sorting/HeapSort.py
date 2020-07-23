from typing import List

# Heapify is a fantastic, unstable, in-place sorting algorithm
# Its best use case is when we havent recieved all of the data yet or we need a worst case in-place algorithm thats unstable
# Beats merge/quick in space complexity which is always good

## Best ## Avrg ## Wrst ## Spce ##
## nlogn # nlogn # nlogn #  1   ##

# Heapify algorithm
# Heapify works by iteratively ensuring that each element maintains its left and right node as being 'smaller'
# Heapify does this for all nodes starting at the current node, and then 
# arr = array, length = length of array, index = current index of the heapify algorithm
def heapify(arr, length, index):
    # Calculating our left and right indexes
    left = 2 * index + 1
    right = 2 * index + 2

    # Calculating who is biggest
    largest = index

    if left < length and arr[largest] < arr[left]:
        largest = left

    if right < length and arr[largest] < arr[right]:
        largest = right

    if largest != index:
        # Need to swap!
        arr[largest], arr[index] = arr[index], arr[largest]

        heapify(arr, length, largest)


# Heapsort first heapifies every element, starting at half - 1
def heapsort(arr):

    # This creates an actual, proper balanced tree
    for i in range(int(len(arr) / 2 - 1), -1, -1):
        heapify(arr, len(arr), i)

    # Now what we want to do is to start 'popping' off the right-most element, reducing the size of our heap
    # We do this by swapping the head with the right side, reducing the size, then heapifying
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)