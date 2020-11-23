'''
420. Strong Password Checker

A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
 

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0
 

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.
'''

import math
import sys

# Incomplete solution.
class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        # Length parameters. All modifications to size are required adjustments.
        lengthAdjustment = True if len(s) >= 6 and len(s) <= 20 else False
        
        # One lower case, one uppercase, one digit
        missingUpper, missingLower, missingDigit = 1, 1, 1
        
        # Tracking our repeating digit
        repeatDigit = list()
        prevRepeatDigit = ''
        prevRepeatDigitCount = 1
        
        # No repeting digits in a row
        for c in s:
            if c.islower():
                missingLower = 0
            if c.isupper():
                missingUpper = 0
            if c.isdigit():
                missingDigit = 0
        
            # Handling repeated characters
            if c == prevRepeatDigit:
                prevRepeatDigitCount += 1
                
            else:
                # Did we hit the maximal length?
                if prevRepeatDigitCount >= 3:
                    # This was too long and must be recorder
                    repeatDigit.append(prevRepeatDigitCount)
                prevRepeatDigitCount = 1
                prevRepeatDigit = c
        
        # Checking final repeated digit value
        if prevRepeatDigitCount >= 3:
                # This was too long and must be recorder
                repeatDigit.append(prevRepeatDigitCount)
                
        characterTypeFixes = (missingLower + missingUpper + missingDigit)
                
        # Making our final adjustments
        if lengthAdjustment:
            # Great; we don't need to adjust size.
            # This is the easiest to calculate. 
            numRepeatAdjust = 0
            for repeat in repeatDigit:
                numRepeatAdjust += math.floor(repeat / 3)
                
            # Is this number greater than the sum of number of missing digits?
            # If so, we don't worry about them since the repeat fixes will also fix those
            if numRepeatAdjust > characterTypeFixes:
                return numRepeatAdjust
            else:
                return characterTypeFixes
            
        # Handling if our length is greater than the required length.
        if not lengthAdjustment and len(s) < 6:
            numToAdd = 6 - len(s)
            
            if numToAdd > characterTypeFixes:
                return numToAdd
            
            elif numToAdd <= characterTypeFixes:
                return characterTypeFixes
            
        if not lengthAdjustment and len(s) > 20:
            moves = 0
            numToDelete = len(s) - 20
            
            # We will do this until we have achieved our desired length of 20, or ran out of repeats to delete.
            newRepeat = sorted(repeatDigit)
            
            # First we will perform deletions on the smallest sets of repeating numbers.
            for i, repeat in enumerate(newRepeat):
                repeatAdjustmentSize = (repeat - 2)
                if repeatAdjustmentSize < numToDelete:
                    numToDelete -= repeatAdjustmentSize
                    newRepeat[i] = 0
                    moves += repeatAdjustmentSize
                else:
                    # Take away as much as we can
                    moves += numToDelete
                    newRepeat[i] = (newRepeat[i] - numToDelete)
                    numToDelete = 0
                    
            # Once we've reduced, we will attempt to change as many numbers as needed from the character type fix set.
            numRepeatAdjust = 0
            for repeat in newRepeat:
                numRepeatAdjust += math.floor(repeat / 3)

            print(numToDelete, moves, numToDelete, newRepeat)
                
            # Is this number greater than the sum of number of missing digits?
            # If so, we don't worry about them since the repeat fixes will also fix those
            if numRepeatAdjust > characterTypeFixes:
                moves += numRepeatAdjust
            else:
                moves += characterTypeFixes
                moves += numToDelete
                
            return moves
                
                
# Working solution
class WorkingSolution:
    def strongPasswordChecker(self, s: str) -> int:
        if len(s) < 3:
            return 6-len(s)
        
        l,u,d = 1,1,1
        S = []
        for i in range(2):
            if 'a' <= s[i] <= 'z':
                l = 0
            elif 'A' <= s[i] <= 'Z':
                u = 0
            elif '0' <= s[i] <= '9':
                d = 0
            S.append(s[i])
                
        R = sys.maxsize
        def b(i, C, r, a):
            nonlocal s,S,R
            (l, u, d) = C
            if i == len(s):
                a = max(a, sum(C))
                if len(S) < 6:
                    a = max(a, 6 - len(S))
                elif len(S) > 20:
                    r += len(S) - 20
                R = min(R, r+a)
                return
            if s[i] == S[-1] == S[-2]:
                b(i+1, (l,u,d), r+1, a) # removed

                S.append(None)
                b(i+1, (l,u,d), r, a+1) # changed / appended if less than 6 symbols
                S.pop()
            else:
                if 'a' <= s[i] <= 'z':
                    l = 0
                elif 'A' <= s[i] <= 'Z':
                    u = 0
                elif '0' <= s[i] <= '9':
                    d = 0

                S.append(s[i])
                b(i+1, (l,u,d), r, a) # added as is
                S.pop()

        b(2, (l,u,d), 0, 0)
        return R