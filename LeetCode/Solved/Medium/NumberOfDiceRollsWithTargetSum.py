'''
1155. Number of Dice Rolls With Target Sum

You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
'''

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # Base case of d == 1
        if d == 1:
            return (1 if f >= target else 0)
        
        # depth / number of remaining dice = total number of ways to reach target
        dicePossibilities = {}
        
        # Brute force approach, using DP with dice possibilities
        self.numDiceAvailable(dicePossibilities, d, 0, target, f)
        
        return dicePossibilities[(0,d)] % (1000000000 + 7)
        
    def numDiceAvailable(self, d: dict, depth: int, sum: int, target: int, f: int):
        if depth == 1:
            # Bottom layer. No more dice to roll.
            c = 0
            for n in range(1, f + 1):
                if sum + n == target:
                    c += 1
                    d[(sum + n, depth)] = 1
            return c
        
        elif (sum, depth) in d:
            return d[(sum, depth)]

        else:
            c = 0
            for n in range(1, f + 1):
                c += self.numDiceAvailable(d, depth - 1, sum + n, target, f)
            d[(sum, depth)] = c
            return c
                