''' 
#5
# Very classic problem, two sum problem. Given an array of numbers and a target number, return two numbers within the array that sum to the target number.

For example, [1,2,3,4,5,6,7,8,9], and a target of 17, return [8,9]
'''

# Classic problem. Single pass by using a set as a way of checking against pairs. If target - current value exists, then current value + (target - current value) = target
# O(n) time complexity as we iterate over every value, O(n) space complexity (storing every value into a set)

from typing import List

class Solution():

    def twoSum(self, data: List[int], target: int) -> tuple:
        d = set()
        for n in data:
            if (target - n) in data:
                return [n, target - n]
            d.add(n)
        return [-1, -1]

    # Same problem but returns the index instead of the values
    def twoSumIndex(self, data: List[int], target: int) -> tuple:
        d = {}
        for n in range(len(data)):
            if (target - data[n]) in d:
                return [n, d[target-data[n]]]
            d[data[n]] = n

        return [-1,-1]

    # Brute force solution; O(n*n) time complexity, O(1) space complexity. Obviously not ideal
    def twoSumBruteForce(self, data: List[int], target: int) -> tuple:
        for i, n in enumerate(data):
            for j, m in enumerate(data):
                if i == j:
                    continue
                if n + m == target:
                    return [i, j]
        return [-1,-1]

s = Solution()
print(s.twoSum([1,2,3,4,5,6,7,8,9],9))
print(s.twoSumIndex([1,2,3,4,5,6,7,8,9],9))
print(s.twoSumBruteForce([1,2,3,4,5,6,7,8,9],9))