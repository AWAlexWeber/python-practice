# A fenwick tree, or binary indexed tree, is a special datastructure that helps us solve some problems
# Given an array from 0...n-1
# We would like to compute the sum of the first i elements, or modify the value of a specificed element on the array arr[i] = x where 0 <= i <= n-1

# The size of our binary indexed tree is equal to n where n is the size of the input array
# O(logn) time for
# Find sum of first i elements
# Update value of a specific element

from typing import List

class FenwickTree:

    # @parmas an array sorted in ascending order
    # This parameter can be adjusted but its used when it comes to initalizing our array
    def __init__(self, l: List[int]):
        self.tree = [0] * (len(l) + 1)
        for i, n in enumerate(l):
            self.update(len(l), i, n)

    def update(self, n: int, i: int, v: int):
        i = i + 1
        while i <= n:
            self.tree[i] += v
            i += i & (-i)

    def getSum(self, i: int) -> int:
        s = 0
        i = i + 1

        while i > 0:
            s += self.tree[i]
            i -= i & (-i)

        return s

f = FenwickTree([2,1,1,3,2,3,4,5,6,7,8,9])
print(f.tree)
print(f.getSum(4))