'''
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:


Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
'''

from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # In order for a rotation to even exist, the same value must occur in both A and B
        # Extra padded 0 at the front to make it easier to deal with off by one errors.
        aCount, bCount = [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]
        lenCount = [0,0,0,0,0,0,0]
        
        for i in range(0, len(A)):
            dA = A[i]
            dB = B[i]
            
            # If they're the same, we need to track that
            if dA == dB:
                lenCount[dA] += 1
            else:
                aCount[dA] += 1
                bCount[dB] += 1

        for i in range(0,7):
            # Check; the count must be greater or equal to the total length
            if aCount[i] + bCount[i] == len(A) - lenCount[i]:
                # Returning the bigger one minus total length
                return (len(A) - lenCount[i] - aCount[i] if aCount[i] > bCount[i] else len(A) - lenCount[i] - bCount[i])
            
        return -1

    # O(1) solution. Yes our other solution is already O(1), but this uses less space.
    def minDominoRotationsFaster(self, A: List[int], B: List[int]) -> int:
        def check(x):
            """
            Return min number of swaps 
            if one could make all elements in A or B equal to x.
            Else return -1.
            """
            # how many rotations should be done
            # to have all elements in A equal to x
            # and to have all elements in B equal to x
            rotations_a = rotations_b = 0
            for i in range(n):
                # rotations coudn't be done
                if A[i] != x and B[i] != x:
                    return -1
                # A[i] != x and B[i] == x
                elif A[i] != x:
                    rotations_a += 1
                # A[i] == x and B[i] != x    
                elif B[i] != x:
                    rotations_b += 1
            # min number of rotations to have all
            # elements equal to x in A or B
            return min(rotations_a, rotations_b)
    
        n = len(A)
        rotations = check(A[0]) 
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or A[0] == B[0]:
            return rotations 
        # If one could make all elements in A or B equal to B[0]
        else:
            return check(B[0])