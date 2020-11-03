'''
1000. Minimum Cost to Merge Stones

There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

 

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
 

Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
'''

from typing import List

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        dp, N, Sum, H = {}, len(stones), {-1: 0}, {}
        for i in range(N):
            j, dp[i], H[i], Sum[i] = i, {}, {}, Sum[i - 1] + stones[i]       
            while j > -1:
                H[i][j] = (i-j+1)%(K-1)+(K-1)*(1//(1+(i-j+1)%(K-1)))
                if i - j < K - 1: dp[i][j] = 0    
                else:
                    dp[i][j] =  dp[i][i] + dp[i - 1][j]
                    for k in range(j + 1, i + 1):
                        if H[i][k] + H[k - 1][j] == H[i][j] or H[i][k] + H[k - 1][j] == K:
                            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k - 1][j])     
                    if H[i][j] == 1: dp[i][j] += Sum[i] - Sum[j - 1]
                j = j - 1           
        return dp[N-1][0]*(1//H[N-1][0]) - min(H[N-1][0]-1, 1)  
        
        
        """
        s = 0
        count = 0
        while True:
            # If we have one pile, let's return that value
            if len(stones) == 1:
                return s
            
            # Not possible to combine piles of stones
            if len(stones) < K:
                return -1
            
            
            # Finding the maximal number of stones
            max_sum = float("inf")
            stones_range = (0,K)
            current_sum = 0
            for i in range(len(stones)):
                current_sum += stones[i]
                if i >= K:
                    current_sum -= stones[i - K]
                print(current_sum,i,max_sum)
                if current_sum < max_sum and i >= K - 1:
                    max_sum, stones_range = current_sum, (i - K + 1, i)
                    
            # Creating a new list of stones in O(n) and using the sum of this range
            new_stones = list()
            i = 0
            while i < len(stones):
                if i == stones_range[0]:
                    new_stones.append(max_sum)
                    s += max_sum
                    i += K
                else:
                    new_stones.append(stones[i])
                    i += 1
                    
            stones = new_stones
            print(stones)
            
            count += 1
            if count > 5:
                return -1
                
        """