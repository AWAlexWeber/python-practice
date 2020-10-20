'''
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

class Solution:
    def numTrees(self, n: int) -> int:
        return self.catalan(n)
        '''
        # 1) DP Approach using memoization using an array instead of a dictionary
        h = [0] * (n + 1)
        h[0], h[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                h[i] += h[j-1] * h[i-j]

        return h[n]
        '''
    
    # Catalan approach
    def catalan(self, n: int):
        c = 1
        for i in range(0, n):
            c = c * 2*(2*i+1)/(i+2)
            
        return int(c)