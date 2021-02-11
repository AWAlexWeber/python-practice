'''
191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Constraints:

The input must be a binary string of length 32
'''

# Hamming weight is the number of 1s digits. Note that each 1 digit effectively represents an addition of 2^n where n is the distance from the right.
# We can calculate the hamming weight by iteratively removing a 2^n where we reduce n, only if 2^n is less than or equal to the current value.
# This approach takes O(floor(1 + log2(n))) where n is the input number. Technically O(1) since our size can only be a 32 bit integer

class Solution:
    def hammingWeight(self, n: int) -> int:
        # i: Maximal exponent that fits within our value n. Discover this at the start
        i = 0
        while 2**i <= n:
            i += 1
        i -= 1
        
        print(i,n)
        hammingWeight = 0
        
        while n > 0:
            print(n,i)
            if 2**i <= n:
                n -= 2**i
                hammingWeight += 1

            i -= 1
            
        return hammingWeight

s = Solution()
s.hammingWeight(128)