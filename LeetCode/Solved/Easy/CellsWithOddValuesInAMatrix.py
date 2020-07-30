'''
1252. Cells with Odd Values in a Matrix
'''

from typing import List

# This is a very good solution, runs in O(n) where n is the number of indices
# Efficient solution
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        r = {}
        c = {}
        rn = cn = 0
        
        # Iterating over our index array
        for i in indices:
            rv = r.setdefault(i[0], 0) + 1
            rn += (1 if rv % 2 == 1 else -1)
            r[i[0]] = rv
            
            cv = c.setdefault(i[1], 0) + 1
            cn += (1 if cv % 2 == 1 else -1)
            c[i[1]] = cv
            
        # Calculating conflicts from the number of cn
        return cn * (n - rn) + rn * (m - cn)