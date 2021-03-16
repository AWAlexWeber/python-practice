'''
Create a datastructure that returns the sum of all values between two indexes in O(1) time.
'''

from typing import List

class OptimizedListSum:
    def __init__(self, arr: List[int]):
        self.totalSum = sum(arr)
        self.leftSum = [0] * len(arr)
        self.rightSum = [0] * len(arr)
        for idx in range(len(arr) - 1):
            self.leftSum[idx + 1] = self.leftSum[idx] + arr[idx]

        for idx in range(len(arr) - 1, 0, -1):
            self.rightSum[idx - 1] = self.rightSum[idx] + arr[idx]

    def getSum(self, rangeTuple: tuple) -> int:
        left, right = rangeTuple[0], rangeTuple[1] - 1
        return self.totalSum - self.leftSum[left] - self.rightSum[right]

o = OptimizedListSum([1,2,3,4,5,6,7])
print(o.getSum((2,5)))