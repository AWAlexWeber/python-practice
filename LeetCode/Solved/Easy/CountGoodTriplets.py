'''
1534. Count Good Triplets


Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

 

Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
 

Constraints:

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000
'''

from typing import List

# This is kinda lame as in it is a brute force solution
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Iterating over everything via brute force solution
        # O(n^3)
        o = 0
        i, j, k = 0, 0, 0
        while i < len(arr):
            j = i + 1
            while j < len(arr):
                k = j + 1
                
                aa = abs(arr[i] - arr[j])
                
                if aa > a:
                    j = j + 1
                    continue
                
                while k < len(arr):
                    
                    ab = abs(arr[j] - arr[k])
                    ac = abs(arr[i] - arr[k])
                    
                    if aa <= a and ab <= b and ac <= c:
                        o += 1
                        
                    k += 1
                j += 1
            i += 1
        
        return o