'''
1409. Queries on a Permutation With Key

Given the array queries of positive integers between 1 and m, you have to process all queries[i] (from i=0 to i=queries.length-1) according to the following rules:

In the beginning, you have the permutation P=[1,2,3,...,m].
For the current i, find the position of queries[i] in the permutation P (indexing from 0) and then move this at the beginning of the permutation P. Notice that the position of queries[i] in P is the result for queries[i].
Return an array containing the result for the given queries.

 

Example 1:

Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1] 
Explanation: The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5]. 
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5]. 
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5]. 
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5]. 
Therefore, the array containing the result is [2,1,2,1].  
Example 2:

Input: queries = [4,1,2,2], m = 4
Output: [3,1,2,0]
Example 3:

Input: queries = [7,5,5,8,3], m = 8
Output: [6,5,0,7,5]
 

Constraints:

1 <= m <= 10^3
1 <= queries.length <= m
1 <= queries[i] <= m
'''

from typing import List

class FenwickTree:

    # @parmas an array sorted in ascending order
    # This parameter can be adjusted but its used when it comes to initalizing our array
    def __init__(self, l: List[int]):
        self.tree = [0] * (len(l) + 1)
        for i, n in enumerate(l):
            self.update(len(l), i, n)

    def update(self, n: int, i: int, v: int):
        i = i + 1
        while i <= n:
            self.tree[i] += v
            i += i & (-i)

    def getSum(self, i: int) -> int:
        s = 0
        i = i + 1

        while i > 0:
            s += self.tree[i]
            i -= i & (-i)

        return s



# Brute force solution in O(m^2) time
# Note that while this is a decent solution, there is something called a Fenwick tree which does a better job
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        o = []

        # Constructing our list
        l = []
        for n in range(m):
            l.append(n+1)

        for n in queries:
            i = l.index(n)
            v = l[i]
            l.pop(i)
            o.append(i)
            l.insert(0, v)

        return o

    # Solution using a fenwick tree
    def fenwickSoltion(self, queries: List[int], m: int) -> List[int]:
        # Building our insert array
        a, h = [0] * (2 * m + 1), {}
        f = FenwickTree(a)
        for i in range(1, m + 1):
            f.update(len(a), i + m, 1)
            h[i] = i + m + 1
        c = m


        print(f.tree)
        print(h)

        o = []

        for q in queries:
            # Popping our index
            i = h.pop(q)
            r = f.getSum(i-1)
            o.append(r - 1)

            # Reinserting
            h[q] = c
            f.update(len(a), i, -1)
            f.update(len(a), c - 1, 1)
            c -= 1

        return o

        
s = Solution()
print(s.fenwickSoltion([4,1,2,2],4))