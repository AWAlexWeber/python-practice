'''
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''
from typing import List

# Good but not in place
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i, m, o = len(arr) - 2, arr[len(arr) - 1], [-1] * len(arr)
        
        for v in reversed(arr[:-1]):
            o[i] = m
            m = max(v,m)
            i -= 1
            
        return o

    def inPlaceReplace(self, arr: List[int]) -> List[int]:
        m, i = -1, len(arr) - 1
        while i >= 0:
            arr[i], m = m, max(m, arr[i])
            i -= 1
            
        return arr