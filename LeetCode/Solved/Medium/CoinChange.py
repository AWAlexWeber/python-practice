'''
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Handling a couple of edge cases
        if amount == 0:
            return 0
        
        c = sorted(coins,reverse=True)
        
        if c[len(c) - 1] > amount:
            return -1
        
        # Greedy approach where we take the largest denomination
        visit = {}
        self.minCount = float("inf")
        self.greedy(c, amount, visit)
        
        if 0 in visit:
            return visit[0]
        else:
            return -1
        
    def greedy(self, coins: List[int], amount: int, visit: dict, count=0):
        """ Handling some base cases. """
        # Is this amount already in the visit set and is it better then what we got?
        if amount in visit and visit[amount] <= count:
            return
        
        # Did we go too deep?
        if count >= self.minCount:
            return
        
        # Did we hit zero?
        if amount == 0:
            self.minCount = min(self.minCount, count)
            
        """ Actually performing our deepening. """
        for coin in coins:
            # Base values
            newAmount = amount - coin
            newCount = count + 1
            
            # Is this an invalid new amount? (Less than zero)
            if newAmount < 0:
                continue
            
            # Skipping anywhere our newAmount is already accounted for
            if newAmount in visit and visit[newAmount] <= newCount:
                continue
                
            # Okay, actually performing our deepening.
            self.greedy(coins, newAmount, visit, newCount)
            
            # Adding us to the visisted set
            visit[newAmount] = newCount
            