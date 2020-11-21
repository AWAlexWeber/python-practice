'''
904. Fruit Into Baskets

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
'''

from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) <= 0:
            return 0
        
        i = 0
        c = 0
        totalMax = 0
        while i != -1:
            currentSum, i = self.localMax(tree, i)
            totalMax = max(currentSum, totalMax)
        return totalMax
    
    def localMax(self, tree: List[int], i: int) -> (int, int):
        previousIndex = {tree[i]: i}
        s = set()
        s.add(tree[i])
        currentSum = 1
        i += 1
        
        while i < len(tree):
            
            if tree[i] not in s and len(s) == 2:
                # Time to leave
                break
                
            if tree[i] not in s:
                s.add(tree[i])
                previousIndex[tree[i]] = i
            
            if tree[i] != tree[i - 1]:
                previousIndex[tree[i]] = i
            
            currentSum += 1
            i += 1
        
        maxKey = -1
        if i != len(tree):
            for key in previousIndex:
                maxKey = max(previousIndex[key], maxKey)
        
        return currentSum, maxKey

    # Faster
    def totalFruitFaster(self, tree: List[int]) -> int:
        # i is latest pointer
        # j tracks the recently changed char start index
        # c tracks the recent char 
        # maxi tracks the max no fruits
        # tmp keeps temporary max no of truits
        
        i,j,maxi,tmp,c = 0,0,0, 0, tree[0]
        unique = set()
        while i < len(tree):
            if len(unique)>=2 and tree[i] not in unique:
                maxi = max(maxi, tmp)
                unique=set([tree[i],tree[j]])
                tmp = i-j+1
                c = tree[i]
                j = i
            else:
                if c != tree[i]:
                    j = i
                    c = tree[i]
                if tree[i] not in unique:
                    unique.add(tree[i])
                    # j = i
                tmp +=1
            i+=1
        return max(maxi,tmp)