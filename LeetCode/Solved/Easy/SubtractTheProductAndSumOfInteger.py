'''
1281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
'''

class Solution:
    # Naive solution (but it works!)
    def subtractProductAndSum(self, n: int) -> int:
        # O(k) where k is the length of n
        ca = []
        for c in str(n):
            ca.append(c)
            
        p = 1
        s = 0
        
        for c in ca:
            p *= int(c)
            s += int(c)
            
        return p - s
        
s = Solution()
print(s.subtractProductAndSum(234))