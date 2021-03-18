'''
Given a decimal value, return the number of 1s in its binary representation.
'''

import math

class Solution:
    def numberOfOnes(self, k: int) -> int:
        # A 1 represents a 2 to the power. So essentially we will start with the largest 2^n, subtract it and decrement n.
        # We will do this until k reaches zero then return that value
        n, count = math.floor(math.log(k, 2)), 0
        while k > 0:
            if 2**n <= k:
                k -= 2**n
                count += 1
            else:
                n -= 1

        return count 

s = Solution()
print(s.numberOfOnes(126362))