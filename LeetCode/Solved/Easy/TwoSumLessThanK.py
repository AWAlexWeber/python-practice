'''
1099. Two Sum Less Than K

Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
'''

from typing import List

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        # O(N log N) assuming some sort of comparison sort with O(1) space-complexity (quick sort)
        i, j, s, A = 0, len(A) - 1, -1, sorted(A)
        
        while i != j:
            s = max(A[i] + A[j], s) if A[i] + A[j] < K else s
            i, j = i + 1 if A[i] + A[j] <= K else i, j - 1 if A[i] + A[j] > K else j
            
        return s