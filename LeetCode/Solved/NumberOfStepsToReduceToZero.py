'''
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

 

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12
'''

# All this does is conver the integer value to binary
# IE if we are given 123,
# 1111011
# We count all the 1s, in this case 6. Each 1 represents a division of 2, so a step that we have to take
# We add the length of the entire string, as every bit represents a -1 we have to take
# The divisions being the 1s and the length being the -1 gives us an almost final answer, we - 1 since its 1 over by default
# Going to be honest this feels like one of those problems where you just have to know the trick
class Solution:
    def numberOfSteps (self, num: int) -> int:
        d = f'{num:b}'
        return d.count('1') - 1 + len(d)

s = Solution()
print(s.numberOfSteps(123))