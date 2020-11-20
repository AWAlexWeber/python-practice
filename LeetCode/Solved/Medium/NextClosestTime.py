'''
681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
'''

class Solution:
    def nextClosestTime(self, time: str) -> str:
        # Time
        t = list(time)
        
        # Collect a sorted set of the time values
        f = sorted(set(time))
        
        # This is basically a form of addition
        carry, i = True, 4
        while carry and i >= 0:
            # Skipping the semicolon
            if i == 2:
                i -= 1
                continue
            
            # Attempting to increment the value in time
            for v in f:
                if v == ':':
                    continue
                    
                if int(v) > int(t[i]):
                    if self.isValidDigit(int(v), int(i), t):
                        t[i] = v
                        carry = False
                        break
            if carry:
                # We did not find a replacement.
                # Using the lowest possible value
                t[i] = f[0]
                
            # Decremnting our i
            i -= 1
                
        return ''.join(t)
                
    def isValidDigit(self, v: int, i: int, t: list) -> bool:
        # Determinig if an integer is valid for the given index
        # 0 -> 0,1,2
        # 1 -> 0 through 9 if 0 is 0,1 else 0->3
        # 2 -> 0 through 5
        # 3 -> 9 through 9
        if i == 0:
            return (v >= 0 and v <= 2)
        elif i == 1:
            if int(t[0]) <= 1:
                return (v>= 0 and v <= 9)
            else:
                return (v>= 0 and v <= 3)
        elif i == 3:
            return (v >= 0 and v <= 5)
        elif i == 4:
            return (v >= 0 and v <= 9)
            
        