'''
Given a SORTED matrix, return if a value exists within it.
By sorted, each row is sorted and every value in a row is less than the value in the next row.
'''

from typing import List

class Solution:
    def matrixSearch(self, arr: List[List[int]], target: int) -> bool:
        # Essentially binary search but in two dimensions.
        left, mid, right = 0, len(arr) // 2, len(arr)

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= target and arr[mid][len(arr[mid]) - 1] >= target:
                break
            elif arr[mid][len(arr[mid]) - 1] < target:
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, len(arr[mid])
        while left <= right:
            midVal = (left + right) // 2
            if arr[mid][midVal] > target:
                right = midVal - 1
            elif arr[mid][midVal] < target:
                left = midVal + 1
            else:
                return True

        return False


s = Solution()
arr = [[1,3,5,8],[10,11,15,16],[24,25,30,31]]
for row in arr:
    for value in row:
        print(s.matrixSearch(arr, value))