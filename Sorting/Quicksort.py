from typing import List

# Quicksort is an in-place divide/conquer algorithm
# Not stable, marginially faster than mergesort due to smaller constant but same complexity
# Has a worse case of O(n^2) when the input list is in reverse order, or some form where the pivot is choosen poorly
# Average/best of nlog(n). In general quicksort is an excellent algorithm to pick, if you can remove the worse-cases.

## Best ## Avrg ## Wrst ## Spce ##
## nlogn # nlogn # n^2   # logn ##

# @param list: The input list to sort of any variable type supporting comparators
# @param start: The start of the array
# @param end: The end of our sort scope, which will be the length on initialization
def quicksort(list, start, end):
    # Handling base case
    if start == end:
        return

    # Performing our pivot swap
    r = start
    q = start - 1
    p = end - 1

    # While our r which represnts our comparator is less than p which is our pivot
    # We will continually iterate over each element and swapping it to the left of the future pivot point
    # The future pivot point being denoted by q
    while r < p:

        # If the value at r is less than the value at our pivot
        # Remember that r iterates from the start to the end, or pivot point
        if list[r] < list[p]:

            # If we do have a value, we want to iterate our pivot point
            q += 1

            # Not swapping if p = r
            if q != r:
                t = list[r]
                list[r] = list[q]
                list[q] = t

        r += 1

    # We've completed this section, time to swap our pivot point and sort the remaining halves
    # We've put everything smaller than p to the left of q += 1, and everything greater to the right
    # We then will sort the remainders, making sure to move the pivot first
    q += 1
    t = list[q]
    list[q] = list[p]
    list[p] = t

    # Sorting left and right
    quicksort(list, 0, q)
    quicksort(list, q + 1, end)

#### Explanation ####
# Given that we input a list of [1,5,3,9,8,6,7,0,2,4] and pass it into quicksort
# We start off with the list, with a start of 0 and an end of the length, in this case 10
# Here are the following steps for the first sort
# r = 0, q = -1, p = 9
# While r < p, we increment p
# If list[r] < list[p], we increment our q and swap the position at r with the position at q
# Anytime our value is less than p, we don't actually do anything
# Basically what we are trying to do is move everything less than the pivot to the left and everything greater to the right
# 1 is < 4, p = 0, r = 0, do not swap
# 5 > 4, do nothing, increment r = 1
# 3 < 4, p = 1, r = 2, swap it so now our value at 1 = 3 (1, 3, 5, 9, 8, 6, 7, 0, 2, 4)
# Basically by not incrementing q when the value is less than, we select for all values that are > pivot and swap them with values that are less

def qs(arr: List[int], l: int, r: int):
    # Base case
    if r - l <= 1:
        return

    # Finding our pivot and sorting around it
    i, j, p = l, l - 1, arr[r - 1]

    while i < r - 1:
        # Swapping i and j + 1 if i is less than pivot
        if arr[i] < p:
            j += 1

            if j != i:
                arr[i], arr[j] = arr[j], arr[i]

        i += 1

    # Performing swap with the pivot
    j = j + 1
    arr[r - 1], arr[j] = arr[j], arr[r - 1]

    qs(arr, l, j)
    qs(arr, j, r)

# Run example
list = [1,5,3,9,8,6,7,0,2,4]
print(list)
quicksort(list, 0, len(list))
print(list)